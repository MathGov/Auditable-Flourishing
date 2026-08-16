# How to Verify Auditable Flourishing v6.2

1. Confirm the outer ZIP opens without CRC errors.
2. Extract it without renaming files.
3. Run `python verify_release_v6_2.py` from the extracted package root.
4. Compare `SHA256SUMS.txt` or `SHA256SUMS.json` with the extracted files.
5. Review `release/AF_CANONICAL_REGISTRY_v6_2.json` for canonical identifiers, Stage A precedence, Stage B dimensions, and artifact authority.
6. Review `release/FINAL_VALIDATION_REPORT_v6_2.json` and `release/TABLE_AND_VISUAL_QA_RECORD_v6_2.json` for the final candidate-package checks.
7. Run the supplement verifier inside `reproducibility/Auditable_Flourishing_v6_2_Release_Hardening_Supplement/`.

Genuine Word files are ZIP/OOXML containers containing `[Content_Types].xml` and `word/document.xml`. The workbook verifier checks workbook container integrity, calculation metadata, controlled list validations, current release binding, Stage A precedence, trusted-time fields, and required sheets without relying on a desktop spreadsheet application.

A separately exported, renamed, or edited file does not inherit these package attestations.
