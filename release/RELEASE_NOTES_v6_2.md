# AF v6.2 Release Notes

Version 6.2 is a bounded publication-integrity, provenance, verification, and deposit-readiness release that supersedes v6.0.

**Version-reference rule.** AF-v6.2 is the current package release. Any v6.1 references retained only inside provenance identify an internal pre-v6.2 audit or synchronization baseline; they are historical and do not identify the current package. Stable component identifiers such as `AF-SB12-v5.6` and `AF-SB-RELATION-v6.0` remain unchanged because their controlling semantics did not change.

## What changed

- Final publication sanity pass: synchronized all active package references to AF-v6.2, preserved v6.1 only as an explicitly historical provenance baseline, repaired escaped Markdown line breaks and stale/duplicated TOC text, reconciled the 19-sheet workbook/validation records, and regenerated exact hashes and verification records without changing normative semantics.

- Removed the duplicate, misleadingly named v6.0 provenance file and retained the raw pre-correction review once under an accurate name.
- Added a machine-readable canonical registry covering artifact authority, stable component identifiers, Stage A states and statuses, binding precedence, AF-SB12-v5.6, evidence boundaries, and verification paths.
- Added an artifact-authority and version policy that separates package versions from stable component versions and requires unresolved conflicts to fail closed.
- Added a separate official-source verification record for the load-bearing contemporary factual anchors used in the Core.
- Updated all active publication, companion, workbook, submission, release, and supplement bindings to AF-v6.2 while preserving `AF-SB12-v5.6` and `AF-SB-RELATION-v6.0`.
- Strengthened the root verifier to reject active stale-release drift, canonical-registry divergence, duplicate provenance content, workbook-version drift, broken triplets, and supplement failure without requiring a spreadsheet application.
- Rebuilt and visually inspected the complete DOCX/PDF family and the key workbook surfaces.
- Reconstructed nine publication graphics so text, callouts, connectors, and panel padding render cleanly; rebalanced two sparse Core continuation pages without changing wording, page count, navigation, or normative semantics.

## What did not change

C0-C5, the non-compensatory rights floor, Stage A precedence, public status meanings, AF-SB12 dimensions, Stage B relation semantics, constitutional-legitimacy ladder, and authority boundaries are unchanged.

## Evidence boundary

Version 6.2 remains internally specification-complete and Phase 0 design-ready. External reliability, validity, fairness, decision value, affected-party legitimacy, plural constitutional legitimacy, live-use safety, and deployment authorization remain open.
