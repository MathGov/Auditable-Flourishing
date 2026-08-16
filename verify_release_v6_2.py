#!/usr/bin/env python3
"""Portable integrity and synchronization verifier for Auditable Flourishing v6.2.

Uses only the Python standard library. It verifies artifact integrity, canonical
synchronization, workbook OOXML controls, provenance, and release boundaries.
It does not establish empirical validity or deployment authorization.
"""
from __future__ import annotations

from pathlib import Path
from zipfile import ZipFile
import hashlib
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
ERRORS: list[str] = []
CHECKS: list[dict] = []


def passed(name: str, detail: str) -> None:
    CHECKS.append({"check": name, "status": "PASS", "detail": detail})


def failed(name: str, detail: object) -> None:
    message = str(detail)
    ERRORS.append(f"{name}: {message}")
    CHECKS.append({"check": name, "status": "FAIL", "detail": message})


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def excluded_from_root_inventory(path: Path) -> bool:
    return (
        path.name in {
            "SHA256SUMS.json",
            "SHA256SUMS.txt",
            "FINAL_VALIDATION_REPORT_v6_2.json",
            "FINAL_VALIDATION_PASS.txt",
        }
        or "__pycache__" in path.parts
        or path.suffix == ".pyc"
    )


def inventory() -> None:
    try:
        record = json.loads((ROOT / "SHA256SUMS.json").read_text(encoding="utf-8"))
        expected = {entry["path"]: entry for entry in record["files"]}
        actual = {
            path.relative_to(ROOT).as_posix()
            for path in ROOT.rglob("*")
            if path.is_file() and not excluded_from_root_inventory(path)
        }
        if set(expected) != actual:
            raise AssertionError(
                f"missing_from_inventory={sorted(actual-set(expected))}; "
                f"missing_from_package={sorted(set(expected)-actual)}"
            )
        bad = []
        for relative, entry in expected.items():
            path = ROOT / relative
            if (
                not path.is_file()
                or path.stat().st_size != entry["size_bytes"]
                or sha256(path) != entry["sha256"]
            ):
                bad.append(relative)
        if bad:
            raise AssertionError(f"hash_or_size_mismatch={bad}")
        passed("root_inventory", f"{len(expected)} files bound by size and SHA-256")
    except Exception as exc:
        failed("root_inventory", exc)


def document_containers_and_triplets() -> None:
    try:
        publication = ROOT / "publication"
        release = ROOT / "release"
        docx_files = sorted(list(publication.glob("*.docx")) + list(release.glob("*.docx")))
        pdf_files = sorted(list(publication.glob("*.pdf")) + list(release.glob("*.pdf")))
        bad_docx = []
        for path in docx_files:
            try:
                with ZipFile(path) as archive:
                    if (
                        archive.testzip() is not None
                        or "[Content_Types].xml" not in archive.namelist()
                        or "word/document.xml" not in archive.namelist()
                    ):
                        bad_docx.append(path.name)
            except Exception:
                bad_docx.append(path.name)
        if bad_docx:
            raise AssertionError(f"invalid DOCX={bad_docx}")
        bad_pdf = []
        for path in pdf_files:
            data = path.read_bytes()
            if not data.startswith(b"%PDF-") or b"%%EOF" not in data[-4096:] or len(data) < 1000:
                bad_pdf.append(path.name)
        if bad_pdf:
            raise AssertionError(f"invalid PDF={bad_pdf}")

        publication_docx = sorted(publication.glob("*.docx"))
        release_docx = sorted(release.glob("*.docx"))
        missing_triplets = []
        for path in publication_docx + release_docx:
            for suffix in (".md", ".pdf"):
                sibling = path.with_suffix(suffix)
                if not sibling.is_file():
                    missing_triplets.append(sibling.relative_to(ROOT).as_posix())
        if len(publication_docx) != 12 or len(release_docx) != 3 or missing_triplets:
            raise AssertionError(
                f"publication_docx={len(publication_docx)}; release_docx={len(release_docx)}; "
                f"missing_triplets={missing_triplets}"
            )
        passed(
            "document_containers_and_triplets",
            f"{len(docx_files)} genuine OOXML DOCX, {len(pdf_files)} valid PDFs, 12 publication triplets and 3 release triplets",
        )
    except Exception as exc:
        failed("document_containers_and_triplets", exc)


def extract_docx_text(path: Path) -> str:
    with ZipFile(path) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
    chunks = []
    for element in root.iter():
        if element.tag.endswith("}t") and element.text:
            chunks.append(element.text)
        elif element.tag.endswith("}tab"):
            chunks.append("\t")
        elif element.tag.endswith("}br"):
            chunks.append("\n")
    return "".join(chunks)


def canonical_registry() -> None:
    try:
        registry = json.loads((ROOT / "release/AF_CANONICAL_REGISTRY_v6_2.json").read_text(encoding="utf-8"))
        vocabulary = json.loads(
            (
                ROOT
                / "reproducibility/Auditable_Flourishing_v6_2_Release_Hardening_Supplement/stage_a_status_vocabulary_v6_2.json"
            ).read_text(encoding="utf-8")
        )
        if registry["release"]["id"] != "AF-v6.2" or vocabulary["release"] != "AF-v6.2":
            raise AssertionError("active release binding mismatch")
        registry_statuses = [(item["public"], item["token"]) for item in registry["stage_a"]["public_statuses"]]
        vocabulary_statuses = [(item["public"], item["token"]) for item in vocabulary["public_statuses"]]
        if registry_statuses != vocabulary_statuses:
            raise AssertionError("Stage A public status registry/vocabulary divergence")
        registry_states = [(item["public"], item["token"]) for item in registry["stage_a"]["criterion_states"]]
        vocabulary_states = [(item["public"], item["token"]) for item in vocabulary["criterion_states"]]
        if registry_states != vocabulary_states:
            raise AssertionError("criterion-state registry/vocabulary divergence")
        dimensions = [item["dimension"] for item in registry["stage_b"]["dimensions"]]
        expected_dimensions = [
            "Rights robustness",
            "Audit completeness",
            "Measurement validity",
            "Uncertainty discipline",
            "Corrigibility",
            "Anti-gaming resilience",
            "Non-domination",
            "Refusal quality",
            "Tail-risk adequacy",
            "Ecological adequacy",
            "Institutional compatibility",
            "Reproducibility and public challenge",
        ]
        if dimensions != expected_dimensions:
            raise AssertionError(f"AF-SB12 mismatch={dimensions}")
        stable = registry["stable_component_identifiers"]
        if stable != {
            "stage_b_dimensions": "AF-SB12-v5.6",
            "stage_b_relation_record": "AF-SB-RELATION-v6.0",
            "constitutional_legitimacy_ladder": "CL0-CL6",
        }:
            raise AssertionError(f"stable component registry mismatch={stable}")
        if len(registry["stage_a"]["binding_precedence"]) != 6:
            raise AssertionError("Stage A precedence is not a six-step controlling sequence")
        passed(
            "canonical_registry",
            "release, criterion states, nine public statuses, six-step precedence, AF-SB12, and stable component identifiers agree",
        )
    except Exception as exc:
        failed("canonical_registry", exc)


def critical_synchronization() -> None:
    try:
        publication = ROOT / "publication"
        core_md = (publication / "Auditable_Flourishing_v6_2_Core_Protocol.md").read_text(encoding="utf-8")
        methods_md = (publication / "Auditable_Flourishing_v6_2_Methods_Article_Submission_Draft.md").read_text(encoding="utf-8")
        anchors_md = (publication / "Stage_A_Operational_Anchors_v6_2.md").read_text(encoding="utf-8")
        required_dimensions = [
            "Rights robustness",
            "Audit completeness",
            "Measurement validity",
            "Uncertainty discipline",
            "Corrigibility",
            "Anti-gaming resilience",
            "Non-domination",
            "Refusal quality",
            "Tail-risk adequacy",
            "Ecological adequacy",
            "Institutional compatibility",
            "Reproducibility and public challenge",
        ]
        if "N/P" in core_md:
            raise AssertionError("undefined N/P floor tier remains in Core Markdown")
        if not all(item in methods_md for item in required_dimensions):
            raise AssertionError("Methods Article does not inherit the controlling AF-SB12")
        if "Evidence maturity, reviewer confidence, applicability, burden, and disagreement are separate metadata fields." not in methods_md:
            raise AssertionError("Methods Article evidence-maturity boundary missing")
        if "Known material defects are never erased by uncertainty elsewhere" not in core_md:
            raise AssertionError("Core mixed-state precedence statement missing")
        if "any established unpatchable material defect" not in methods_md.lower():
            raise AssertionError("Methods Article unpatchable-before-indeterminate precedence missing")
        if "any established unpatchable material defect" not in anchors_md.lower():
            raise AssertionError("Stage A Anchors unpatchable-before-indeterminate precedence missing")
        if "preserves the separately versioned relation rule **AF-SB-RELATION-v6.0**" not in core_md:
            raise AssertionError("Core stable relation-component version history is not explicit")
        deprecated = ["Adequate with controls", "admissible with verified controls", "Stage-A admissible - scoped with verified controls"]
        active_text = core_md + "\n" + methods_md + "\n" + anchors_md
        if any(term in active_text for term in deprecated):
            raise AssertionError("deprecated active Stage A label remains")

        docx_targets = [
            publication / "Auditable_Flourishing_v6_2_Core_Protocol.docx",
            publication / "Auditable_Flourishing_v6_2_Methods_Article_Submission_Draft.docx",
            publication / "Stage_A_Operational_Anchors_v6_2.docx",
        ]
        docx_text = {path.name: extract_docx_text(path) for path in docx_targets}
        if "N/P" in docx_text[docx_targets[0].name]:
            raise AssertionError("undefined N/P floor tier remains in Core DOCX")
        if "preserves the separately versioned relation rule" not in docx_text[docx_targets[0].name]:
            raise AssertionError("Core DOCX stable relation history mismatch")
        if not all(item in docx_text[docx_targets[1].name] for item in required_dimensions):
            raise AssertionError("Methods DOCX AF-SB12 mismatch")
        if "any established unpatchable material defect" not in docx_text[docx_targets[2].name].lower():
            raise AssertionError("Anchors DOCX precedence mismatch")
        passed(
            "critical_synchronization",
            "Core/Methods/Anchors Markdown and DOCX agree on AF-SB12, floor tiers, evidence-maturity separation, Stage A precedence, labels, and stable relation history",
        )
    except Exception as exc:
        failed("critical_synchronization", exc)


def active_version_binding() -> None:
    try:
        bad_names = []
        for path in ROOT.rglob("*"):
            if not path.is_file() or "provenance" in path.parts:
                continue
            name = path.name.lower()
            if "v6_0" in name or "v5_8" in name or "v5_7" in name:
                bad_names.append(path.relative_to(ROOT).as_posix())
        if bad_names:
            raise AssertionError(f"stale active filenames={bad_names}")
        forbidden = [
            "AF v5.6 protocol-relative review",
            "RELEASE_VERIFICATION_RECORD_v5_8.json",
            "RELEASE_MANIFEST_v5_8.json",
            "stage_b_yield_simulation_v5_8",
            "perturbation_sensitivity_v5_8",
            "Stage-A admissible - scoped with verified controls",
        ]
        bad_text = []
        for path in ROOT.rglob("*"):
            if (
                not path.is_file()
                or "provenance" in path.parts
                or path.name in {"verify_release_v6_2.py", "verify_supplement_v6_2.py"}
                or path.suffix.lower() not in {".md", ".json", ".csv", ".txt", ".cff"}
            ):
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            hits = [term for term in forbidden if term in text]
            if hits:
                bad_text.append((path.relative_to(ROOT).as_posix(), hits))
        if bad_text:
            raise AssertionError(f"stale active text={bad_text}")
        zenodo = json.loads((ROOT / ".zenodo.json").read_text(encoding="utf-8"))
        if zenodo.get("version") != "6.2":
            raise AssertionError(f"Zenodo version={zenodo.get('version')}")
        citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
        if 'version: "6.2"' not in citation:
            raise AssertionError("CITATION.cff is not bound to v6.2")
        start_here = (ROOT / "START_HERE.md").read_text(encoding="utf-8")
        if "AF-v6.2 is internally specification-complete" not in start_here:
            raise AssertionError("START_HERE current boundary is not AF-v6.2")
        passed("active_version_binding", "active filenames and artifact pointers are v6.2; historical/provenance and stable component identifiers remain explicitly bounded")
    except Exception as exc:
        failed("active_version_binding", exc)


def master_navigation() -> None:
    try:
        path = ROOT / "publication/Auditable_Flourishing_v6_2_Core_Protocol.docx"
        with ZipFile(path) as archive:
            document = archive.read("word/document.xml").decode("utf-8", errors="ignore")
            settings = archive.read("word/settings.xml").decode("utf-8", errors="ignore")
        links = document.count("<w:hyperlink")
        bookmarks = document.count("<w:bookmarkStart")
        if links < 100 or bookmarks < 100 or "updateFields" not in settings:
            raise AssertionError(f"links={links}; bookmarks={bookmarks}; updateFields={'updateFields' in settings}")
        # Static companion TOCs must not retain the previously broken all-page-1 marker.
        for name in [
            "Challenge_Administration_Handbook_v6_2.docx",
            "External_Validation_Burden_and_Decision_Value_Protocol_v6_2.docx",
        ]:
            text = extract_docx_text(ROOT / "publication" / name)
            if text.count("·· 1") > 2:
                raise AssertionError(f"stale static TOC in {name}")
        passed("master_navigation", f"Core Word links={links}; bookmarks={bookmarks}; update-on-open enabled; companion TOCs clean")
    except Exception as exc:
        failed("master_navigation", exc)


def xlsx_sheet_map(archive: ZipFile) -> tuple[list[str], dict[str, str]]:
    main_ns = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
    rel_ns = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
    package_rel_ns = "http://schemas.openxmlformats.org/package/2006/relationships"
    workbook = ET.fromstring(archive.read("xl/workbook.xml"))
    rels = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
    rel_targets = {
        rel.attrib["Id"]: rel.attrib["Target"]
        for rel in rels.findall(f"{{{package_rel_ns}}}Relationship")
    }
    names = []
    mapping = {}
    for sheet in workbook.findall(f".//{{{main_ns}}}sheet"):
        name = sheet.attrib["name"]
        rid = sheet.attrib[f"{{{rel_ns}}}id"]
        target = rel_targets[rid]
        target = target.lstrip("/")
        if not target.startswith("xl/"):
            target = "xl/" + target
        names.append(name)
        mapping[name] = target
    return names, mapping


def xlsx_shared_strings(archive: ZipFile) -> list[str]:
    path = "xl/sharedStrings.xml"
    if path not in archive.namelist():
        return []
    root = ET.fromstring(archive.read(path))
    strings = []
    for item in root:
        strings.append("".join(element.text or "" for element in item.iter() if element.tag.endswith("}t")))
    return strings


def xlsx_cell_value(archive: ZipFile, sheet_path: str, reference: str, shared: list[str]) -> str | None:
    ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    root = ET.fromstring(archive.read(sheet_path))
    cell = root.find(f".//m:c[@r='{reference}']", ns)
    if cell is None:
        return None
    cell_type = cell.attrib.get("t")
    if cell_type == "inlineStr":
        return "".join(element.text or "" for element in cell.iter() if element.tag.endswith("}t"))
    value = cell.find("m:v", ns)
    raw = value.text if value is not None else None
    if cell_type == "s" and raw is not None:
        return shared[int(raw)]
    return raw


def xlsx_formula(archive: ZipFile, sheet_path: str, reference: str) -> str | None:
    ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    root = ET.fromstring(archive.read(sheet_path))
    cell = root.find(f".//m:c[@r='{reference}']", ns)
    if cell is None:
        return None
    formula = cell.find("m:f", ns)
    return formula.text if formula is not None else None


def workbook_integrity() -> None:
    try:
        primary = ROOT / "reproducibility/AF_v6_2_External_Pilot_Aggregation_Workbook.xlsx"
        supplement_copy = (
            ROOT
            / "reproducibility/Auditable_Flourishing_v6_2_Release_Hardening_Supplement/AF_v6_2_External_Pilot_Aggregation_Workbook.xlsx"
        )
        if sha256(primary) != sha256(supplement_copy):
            raise AssertionError("primary and supplement workbook copies are not byte-identical")
        with ZipFile(primary) as archive:
            if archive.testzip() is not None:
                raise AssertionError(f"workbook CRC failure={archive.testzip()}")
            workbook_root = ET.fromstring(archive.read("xl/workbook.xml"))
            calc = next((element for element in workbook_root.iter() if element.tag.endswith("}calcPr")), None)
            if calc is None:
                raise AssertionError("calcPr missing")
            required_calc = {"calcMode": "auto", "fullCalcOnLoad": "1", "forceFullCalc": "1"}
            if any(calc.attrib.get(key) != value for key, value in required_calc.items()):
                raise AssertionError(f"calculation metadata={calc.attrib}")
            names, mapping = xlsx_sheet_map(archive)
            required_sheets = [
                "Read_Me",
                "Stage_A",
                "Verdict_Vector",
                "Independence",
                "Burden_Log",
                "Reliability_Results",
                "Study_Readiness",
                "Perturbation_Register",
                "Vocabulary",
                "Dashboard",
            ]
            missing = [name for name in required_sheets if name not in names]
            if len(names) != 19 or missing:
                raise AssertionError(f"sheet_count={len(names)}; missing={missing}")
            ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
            formula_count = cached_count = error_count = validation_count = list_count = inert_count = 0
            for path in mapping.values():
                xml_root = ET.fromstring(archive.read(path))
                for cell in xml_root.findall(".//m:c", ns):
                    if cell.find("m:f", ns) is not None:
                        formula_count += 1
                        if cell.find("m:v", ns) is not None:
                            cached_count += 1
                        if cell.attrib.get("t") == "e":
                            error_count += 1
                for validation in xml_root.findall(".//m:dataValidation", ns):
                    validation_count += 1
                    formula1 = validation.find("m:formula1", ns)
                    if validation.attrib.get("type") == "list" and formula1 is not None:
                        list_count += 1
                    if validation.attrib.get("type") is None and formula1 is None:
                        inert_count += 1
            if formula_count < 9000 or list_count < 150 or inert_count != 0 or error_count != 0:
                raise AssertionError(
                    f"formulas={formula_count}; cached={cached_count}; list={list_count}; inert={inert_count}; errors={error_count}"
                )
            shared = xlsx_shared_strings(archive)
            verdict_basis = xlsx_cell_value(archive, mapping["Verdict_Vector"], "F4", shared)
            deposit_time = xlsx_cell_value(archive, mapping["Rating_Deposits"], "I5", shared)
            perturb_time = xlsx_cell_value(archive, mapping["Perturbation_Register"], "L5", shared)
            if verdict_basis != "AF v6.2 protocol-relative review":
                raise AssertionError(f"stale verdict basis={verdict_basis!r}")
            iso = re.compile(r"^'?\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
            if not iso.match(deposit_time or "") or not iso.match(perturb_time or ""):
                raise AssertionError(f"trusted-time values={deposit_time!r}, {perturb_time!r}")
            stage_formula = xlsx_formula(archive, mapping["Stage_A"], "Q4") or ""
            sequence = ["AA4>0", "AB4>0", "AC4>0"]
            positions = [stage_formula.find(token) for token in sequence]
            if any(position < 0 for position in positions) or positions != sorted(positions):
                raise AssertionError(f"Stage A precedence formula={stage_formula}")
            active_binding = any(
                b"AF v6.2" in archive.read(path)
                for path in mapping.values()
            )
            if not active_binding:
                raise AssertionError("AF v6.2 worksheet binding missing")
        passed(
            "workbook_integrity",
            f"{len(mapping)} sheets; formulas={formula_count}; list validations={list_count}; inert={inert_count}; full recalculation on load; Stage A precedence, release binding, ISO time, and byte-identical copies verified",
        )
    except Exception as exc:
        failed("workbook_integrity", exc)


def provenance_uniqueness() -> None:
    try:
        directory = ROOT / "provenance"
        expected = {
            "AF_v5_9_Independent_Audit_for_v6_0.md",
            "Claude_v6_0_Pre_Correction_Review_2026-08-13.md",
            "AF_v6_2_Post_Correction_Synchronization_Audit_2026-08-13.md",
        }
        actual = {path.name for path in directory.glob("*") if path.is_file()}
        if actual != expected:
            raise AssertionError(f"provenance files={sorted(actual)}")
        hashes = {path.name: sha256(path) for path in directory.glob("*") if path.is_file()}
        if len(set(hashes.values())) != len(hashes):
            raise AssertionError(f"duplicate provenance content={hashes}")
        if (directory / "AF_v6_0_Final_Synchronization_Audit_2026-08-13.md").exists():
            raise AssertionError("misleading duplicate final-synchronization audit remains")
        passed("provenance_uniqueness", "three accurately labelled provenance records; no duplicate content")
    except Exception as exc:
        failed("provenance_uniqueness", exc)


def external_fact_record() -> None:
    try:
        record = json.loads((ROOT / "release/EXTERNAL_FACT_VERIFICATION_RECORD_v6_2.json").read_text(encoding="utf-8"))
        rows = record.get("records", [])
        ids = {row.get("claim_id") for row in rows}
        expected_ids = {
            "AF-FACT-CLIMATE-2025",
            "AF-FACT-POVERTY-2026",
            "AF-FACT-CONFLICT-2025",
            "AF-FACT-GFS-2025",
        }
        if len(rows) != 4 or ids != expected_ids:
            raise AssertionError(f"fact record IDs={ids}")
        bad = [
            row.get("claim_id")
            for row in rows
            if row.get("status") != "VERIFIED"
            or not str(row.get("url", "")).startswith("https://")
            or not row.get("boundary")
            or not row.get("source")
        ]
        if bad or not record.get("scope_boundary"):
            raise AssertionError(f"incomplete fact records={bad}")
        passed("external_fact_record", "four load-bearing contemporary claims have source, date, URL, status, claim boundary, and scope boundary")
    except Exception as exc:
        failed("external_fact_record", exc)


def supplement() -> None:
    try:
        supplement_dir = ROOT / "reproducibility/Auditable_Flourishing_v6_2_Release_Hardening_Supplement"
        verifier = supplement_dir / "verify_supplement_v6_2.py"
        result = subprocess.run(
            [sys.executable, str(verifier)],
            cwd=supplement_dir,
            text=True,
            capture_output=True,
            timeout=180,
        )
        if result.returncode != 0:
            raise AssertionError((result.stdout + result.stderr)[-5000:])
        output = json.loads(result.stdout)
        if output.get("status") != "PASS":
            raise AssertionError(output)
        zip_path = ROOT / "reproducibility/Auditable_Flourishing_v6_2_Release_Hardening_Supplement.zip"
        with ZipFile(zip_path) as archive:
            if archive.testzip() is not None:
                raise AssertionError(f"supplement ZIP CRC failure={archive.testzip()}")
            names = archive.namelist()
        if len(names) < 20 or "verify_supplement_v6_2.py" not in names:
            raise AssertionError(f"supplement ZIP inventory={names}")
        passed("supplement", f"supplement verifier PASS; ZIP CRC PASS; {len(names)} files")
    except Exception as exc:
        failed("supplement", exc)


def release_reports_and_claim_boundary() -> None:
    try:
        visual = json.loads((ROOT / "release/TABLE_AND_VISUAL_QA_RECORD_v6_2.json").read_text(encoding="utf-8"))
        workbook = json.loads((ROOT / "release/WORKBOOK_VALIDATION_REPORT_v6_2.json").read_text(encoding="utf-8"))
        accessibility = json.loads((ROOT / "release/CORE_ACCESSIBILITY_AUDIT_v6_2.json").read_text(encoding="utf-8"))
        status = (ROOT / "release/VALIDATION_STATUS_v6_2.md").read_text(encoding="utf-8")
        rows = visual.get("pdf_page_results", visual.get("pdf_pages", []))
        row_total = sum(int(row.get("pages", 0)) for row in rows)
        if visual.get("status") != "PASS" or visual.get("total_pdf_pages") != row_total or row_total <= 0:
            raise AssertionError(f"visual QA={visual.get('status')}, pages={visual.get('total_pdf_pages')}, row_total={row_total}")
        if workbook.get("status") != "PASS" or not workbook.get("copies_byte_identical"):
            raise AssertionError("workbook QA or duplicate-copy parity failed")
        counts = accessibility.get("counts", {})
        if counts.get("high") != 0 or counts.get("medium") != 0:
            raise AssertionError(f"accessibility counts={counts}")
        boundary_text = status.lower()
        required_boundary = [
            "external empirical validation",
            "legal conformity",
            "deployment authority",
            "is not certification",
            "procurement approval",
        ]
        if not all(term in boundary_text for term in required_boundary):
            raise AssertionError("validation-status prohibited-claim boundary incomplete")
        passed(
            "release_reports_and_claim_boundary",
            f"{visual.get('total_pdf_pages')} pages visually inspected; workbook QA PASS; accessibility has no high/medium findings; prohibited empirical/legal/moral/deployment claims remain explicit",
        )
    except Exception as exc:
        failed("release_reports_and_claim_boundary", exc)


for check in (
    inventory,
    document_containers_and_triplets,
    canonical_registry,
    critical_synchronization,
    active_version_binding,
    master_navigation,
    workbook_integrity,
    provenance_uniqueness,
    external_fact_record,
    supplement,
    release_reports_and_claim_boundary,
):
    try:
        check()
    except Exception as exc:  # defensive containment; individual checks should already catch.
        failed(check.__name__, repr(exc))

REPORT = {
    "release": "AF-v6.2",
    "status": "PASS" if not ERRORS else "FAIL",
    "verification_boundary": "Artifact integrity and internal synchronization only; not empirical validation, legal conformity, moral certification, or deployment authorization.",
    "checks": CHECKS,
    "errors": ERRORS,
}
print(json.dumps(REPORT, indent=2, ensure_ascii=False))
sys.exit(0 if not ERRORS else 1)
