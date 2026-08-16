#!/usr/bin/env python3
"""Reference decision logic for AF v6.2 release hardening.

This code is illustrative and fail-closed. It does not issue legal, moral,
community, safety or deployment authorization.
"""
from __future__ import annotations

CRITERION_STATES={
 "Adequate for scope","Adequate - control-dependent","Indeterminate",
 "Material defect - patchable","Material defect - unpatchable for stated claim","Not reviewed"
}

def derive_stage_a(states, administration_valid=True, burden="Feasible", floor_unresolved=False):
    # Binding precedence: invalid prerequisites -> established defects -> uncertainty -> adequacy.
    # A known material defect is never erased by uncertainty on another criterion.
    if len(states)!=6 or any(s not in CRITERION_STATES for s in states): return "Protocol refusal to evaluate"
    if not administration_valid or burden=="Not feasible": return "Protocol refusal to evaluate"
    if "Material defect - unpatchable for stated claim" in states: return "Stage-A non-admissible - unpatchable for stated claim"
    if "Material defect - patchable" in states: return "Stage-A non-admissible - patchable"
    if burden=="Indeterminate" or floor_unresolved or "Indeterminate" in states or "Not reviewed" in states:
        return "Indeterminate - insufficient evidence"
    if all(s=="Adequate for scope" for s in states): return "Stage-A admissible - scoped"
    if all(s in {"Adequate for scope","Adequate - control-dependent"} for s in states) and "Adequate - control-dependent" in states:
        return "Stage-A admissible - scoped, control-dependent"
    return "Protocol refusal to evaluate"

def perturbation_admitted(record):
    if record.get("admission_status")!="admitted": return False
    if not record.get("evidence_ref") or not record.get("admission_reason"): return False
    if not (record.get("second_reviewer_id") or record.get("adjudicator_id")): return False
    if record.get("perturbed_relation") not in {"a_dominates_b","b_dominates_a","crossing","tie","unresolved"}: return False
    return record.get("record_version")=="AF-SB-RELATION-v6.0"
