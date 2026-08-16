#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import hashlib, json, re, subprocess, sys, zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
errors = []
checks = []

def ok(name, detail="PASS"):
    checks.append({"check": name, "status": "PASS", "detail": detail})

def fail(name, detail):
    errors.append(f"{name}: {detail}")
    checks.append({"check": name, "status": "FAIL", "detail": str(detail)})

def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def inventory():
    data = json.loads((ROOT / "SHA256SUMS.json").read_text(encoding="utf-8"))
    expected = {r["path"]: r for r in data["files"]}
    actual = {
        p.relative_to(ROOT).as_posix()
        for p in ROOT.rglob("*")
        if p.is_file()
        and p.name not in {"SHA256SUMS.json", "SHA256SUMS.txt"}
        and "__pycache__" not in p.parts
        and p.suffix != ".pyc"
    }
    if set(expected) != actual:
        fail("inventory_coverage", f"missing={sorted(actual-set(expected))}; extra={sorted(set(expected)-actual)}")
    else:
        ok("inventory_coverage", f"{len(actual)} files")
    bad = [
        rel for rel, rec in expected.items()
        if not (ROOT / rel).is_file()
        or (ROOT / rel).stat().st_size != rec["size_bytes"]
        or sha(ROOT / rel) != rec["sha256"]
    ]
    if bad:
        fail("inventory_values", ",".join(bad))
    else:
        ok("inventory_values", f"{len(expected)} hashes/sizes")

def workbook():
    p = ROOT / "AF_v6_2_External_Pilot_Aggregation_Workbook.xlsx"
    try:
        with zipfile.ZipFile(p) as z:
            if z.testzip():
                raise AssertionError(z.testzip())
            wb_xml = z.read("xl/workbook.xml").decode("utf-8", errors="ignore")
            for marker in ('fullCalcOnLoad="1"', 'forceFullCalc="1"', 'calcMode="auto"'):
                if marker not in wb_xml:
                    raise AssertionError(f"missing {marker}")
            ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
            tree = ET.fromstring(z.read("xl/workbook.xml"))
            names = [s.attrib["name"] for s in tree.findall(".//m:sheet", ns)]
            for required in ["Vocabulary","Study_Readiness","Perturbation_Register","Reliability_Results","Stage_A","Independence","Burden_Log"]:
                if required not in names:
                    raise AssertionError(f"missing {required}")
            nodes = []
            for name in z.namelist():
                if name.startswith("xl/worksheets/sheet") and name.endswith(".xml"):
                    xml = z.read(name).decode("utf-8", errors="ignore")
                    nodes += re.findall(r'<(?:\w+:)?dataValidation\b.*?</(?:\w+:)?dataValidation>|<(?:\w+:)?dataValidation\b[^>]*/>', xml)
            lists = sum('type="list"' in x and "formula1" in x for x in nodes)
            inert = sum("type=" not in x and "formula1" not in x for x in nodes)
            if lists < 100 or inert:
                raise AssertionError(f"list={lists}; inert={inert}")
            active_binding = any(
                b"AF v6.2" in z.read(name)
                for name in z.namelist()
                if name.startswith("xl/worksheets/sheet") and name.endswith(".xml")
            )
            if not active_binding:
                raise AssertionError("AF v6.2 binding absent from worksheet records")
        ok("workbook_container", f"{len(names)} sheets; list validations={lists}; inert={inert}; calc metadata and AF-v6.2 binding present")
    except Exception as exc:
        fail("workbook_container", exc)

def logic():
    result = subprocess.run(
        [sys.executable, "test_reference_logic_v6_2.py"],
        cwd=ROOT, text=True, capture_output=True
    )
    count = (ROOT / "test_reference_logic_v6_2.py").read_text(encoding="utf-8").count("def test_")
    if result.returncode:
        fail("reference_tests", (result.stdout + result.stderr)[-3000:])
    else:
        ok("reference_tests", f"{count} reference tests passed")

def validate_record(record, schema):
    props = schema["properties"]
    required = set(schema["required"])
    errors_local = []
    missing = [k for k in required if k not in record]
    if missing:
        errors_local.append(f"missing {missing}")
    extra = set(record) - set(props)
    if schema.get("additionalProperties") is False and extra:
        errors_local.append(f"extra {sorted(extra)}")
    for key, rule in props.items():
        if key not in record:
            continue
        value = record[key]
        if "const" in rule and value != rule["const"]:
            errors_local.append(f"{key} const")
        if "enum" in rule and value not in rule["enum"]:
            errors_local.append(f"{key} enum")
        typ = rule.get("type")
        types = typ if isinstance(typ, list) else [typ] if typ else []
        if types:
            valid = False
            for t in types:
                if t == "string" and isinstance(value, str): valid = True
                elif t == "integer" and isinstance(value, int) and not isinstance(value, bool): valid = True
                elif t == "boolean" and isinstance(value, bool): valid = True
                elif t == "null" and value is None: valid = True
            if not valid:
                errors_local.append(f"{key} type")
        if isinstance(value, str) and rule.get("minLength", 0) and len(value) < rule["minLength"]:
            errors_local.append(f"{key} minLength")
        if isinstance(value, int):
            if "minimum" in rule and value < rule["minimum"]: errors_local.append(f"{key} minimum")
            if "maximum" in rule and value > rule["maximum"]: errors_local.append(f"{key} maximum")
    if record.get("admission_status") == "admitted":
        if not (isinstance(record.get("second_reviewer_id"), str) and record.get("second_reviewer_id")
                or isinstance(record.get("adjudicator_id"), str) and record.get("adjudicator_id")):
            errors_local.append("independent admission")
        for key in ["reversal_capable","perturbed_relation","record_version"]:
            if key not in record:
                errors_local.append(f"admitted missing {key}")
    return errors_local

def schema_examples():
    try:
        schema = json.loads((ROOT / "perturbation_record_v6_2.schema.json").read_text(encoding="utf-8"))
        valid = json.loads((ROOT / "perturbation_record_valid_v6_2.json").read_text(encoding="utf-8"))
        valid_errors = validate_record(valid, schema)
        if valid_errors:
            raise AssertionError(f"valid example failed: {valid_errors}")
        hostile = json.loads((ROOT / "perturbation_record_hostile_v6_2.json").read_text(encoding="utf-8"))
        rejected = sum(bool(validate_record(item["record"], schema)) for item in hostile)
        if rejected != len(hostile):
            raise AssertionError(f"hostile rejected {rejected}/{len(hostile)}")
        ok("perturbation_schema", f"valid=1; hostile_rejected={rejected}; stable record component={schema['properties']['record_version']['const']}")
    except Exception as exc:
        fail("perturbation_schema", exc)

def hostile():
    data = json.loads((ROOT / "workbook_hostile_tests_v6_2.json").read_text(encoding="utf-8"))
    bad = [x["id"] for x in data["tests"] if not x.get("pass")]
    if bad:
        fail("hostile_replay", ",".join(bad))
    else:
        ok("hostile_replay", f"{len(data['tests'])} hostile/reconciliation tests passed")

def semantic():
    try:
        logic_text = (ROOT / "reference_logic_v6_2.py").read_text(encoding="utf-8")
        required = [
            "Stage-A non-admissible - unpatchable for stated claim",
            "Stage-A non-admissible - patchable",
            "Indeterminate - insufficient evidence",
            "Adequate - control-dependent",
        ]
        if not all(x in logic_text for x in required):
            raise AssertionError("reference logic vocabulary/precedence incomplete")
        if logic_text.index('Material defect - unpatchable for stated claim') > logic_text.index('burden=="Indeterminate"'):
            raise AssertionError("unpatchable does not precede indeterminate")
        if 'AF-SB-RELATION-v6.0' not in logic_text:
            raise AssertionError("stable relation component missing")
        vocab = json.loads((ROOT / "stage_a_status_vocabulary_v6_2.json").read_text(encoding="utf-8"))
        if vocab.get("schema_version") != "6.2" or vocab.get("release") != "AF-v6.2":
            raise AssertionError("vocabulary release binding missing")
        ok("semantic_precedence", "established defects precede unresolved evidence; stable component and v6.2 vocabulary verified")
    except Exception as exc:
        fail("semantic_precedence", exc)

def active_version():
    allowed_stable = "AF-SB-RELATION-v6.0"
    bad = []
    for p in ROOT.iterdir():
        if p.is_file() and p.suffix.lower() in {".md",".json",".py",".csv",".txt"} and p.name not in {"SHA256SUMS.json","SHA256SUMS.txt","verify_supplement_v6_2.py"}:
            text = p.read_text(encoding="utf-8", errors="ignore").replace(allowed_stable, "")
            if "AF v6.0" in text or "AF-v6.0" in text or "v6_0" in text or "v6.0" in text:
                bad.append(p.name)
    if bad:
        fail("active_version_binding", ",".join(bad))
    else:
        ok("active_version_binding", "AF-v6.2 active; stable AF-SB-RELATION-v6.0 allowlisted")

for fn in (inventory, workbook, logic, schema_examples, hostile, semantic, active_version):
    try:
        fn()
    except Exception as exc:
        fail(fn.__name__, repr(exc))

report = {
    "release": "AF-v6.2-release-hardening-supplement",
    "status": "PASS" if not errors else "FAIL",
    "checks": checks,
    "errors": errors,
}
print(json.dumps(report, indent=2))
sys.exit(0 if not errors else 1)
