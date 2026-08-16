# Independent Senior Audit — Auditable Flourishing v5.9

**Scope:** the 25 supplied AF v5.9 artifacts plus the aggregation workbook
**Purpose:** determine what would genuinely improve AF as a rigorous, independently usable master work at v6.0
**Method:** byte-level artifact forensics, formula-level instrument testing, independent mathematical reproduction, cross-document consistency scanning, hostile review
**Date of audit:** 13 August 2026
**Auditor stance:** adversarial on claims, conservative on recommendations

---

## 0. WHAT I INSPECTED AND WHAT I COULD NOT

This section exists because AF itself insists that evidence boundaries be stated before findings. The same discipline applies to its auditor.

### 0.1 Inspected directly

| Artifact | Format actually on disk | Words | Inspected |
|---|---|---|---|
| Auditable_Flourishing_v5_9_Core_Protocol.md | UTF-8 Markdown | 30,928 | Full text, all 45 tables, all 11 figure references, heading tree, reference list |
| Auditable_Flourishing_v5_9_Core_Protocol.docx | **UTF-8 Markdown (false extension)** | — | Byte-level + diff against .md |
| AF_v5_9_External_Pilot_Aggregation_Workbook.xlsx | Genuine OOXML | 16 sheets | All 1,757 formulas, all 77 validation rules, raw sheet XML, cached values |
| Stage_A_Operational_Anchors_v5_9.md | UTF-8 Markdown | 1,707 | Full text |
| Measurement_and_Construct_Handbook_v5_9.md | UTF-8 Markdown | 6,574 | Structure, TOC, cross-refs |
| Legal_Rights_and_Authorization_Note_v5_9.md | UTF-8 Markdown | 3,537 | Structure |
| Challenge_Administration_Handbook_v5_9.md | UTF-8 Markdown | 2,323 | Structure |
| MASTER_REFERENCE_CATALOG_v5_9.md | UTF-8 Markdown | 2,341 | Structure |
| External_Validation_Burden_and_Decision_Value_Protocol_v5_9.md | UTF-8 Markdown | 1,860 | Structure |
| Constitutional_Legitimacy_and_Stewardship_Charter_v5_9.md | UTF-8 Markdown | 1,137 | Full text |
| Phase_0_Feasibility_and_Registered_Report_Protocol_v5_9.md | UTF-8 Markdown | 1,055 | Full text |
| Reviewer_Training..._Standard_v5_9.md | UTF-8 Markdown | 1,045 | Structure |
| Scenario_Governance..._Standard_v5_9.md | UTF-8 Markdown | 766 | Full text |
| Methods_Article_Submission_Draft.md | UTF-8 Markdown | 4,701 | Structure, claim comparison against core |
| All 10 companion `.docx` | **UTF-8 Markdown (false extension)** | — | Byte-level + diff against `.md` twins |

**Total AF corpus inspected: ~59,900 words of source plus one 16-sheet instrument.**

### 0.2 Could NOT inspect — and the consequences

| Not supplied | Consequence for this audit |
|---|---|
| `../media/*.png` — all 11 figures | **No graphics quality audit is possible.** I can audit figure *specification*, placement, caption discipline, and epistemic framing only. I cannot assess label size, grayscale survival, arrow ambiguity, or resolution. |
| Rendered DOCX and PDF | **No page-by-page visual QA is possible.** Section L below therefore contains no page numbers. Fabricating them would be the single worst thing this audit could do. |
| `RELEASE_VERIFICATION_RECORD_v5_8.json`, `RELEASE_MANIFEST_v5_8.json`, `SHA256SUMS.txt/.json` | The integrity attestations in Appendix A and D are **uninspectable**. Their validity is asserted, not demonstrated, to any reader who receives what I received. |
| `stage_b_yield_simulation_v5_8.py` and its outputs | Seed-matched replication impossible. I reproduced the results independently instead (see §E.4). |
| Machine-readable schemas, examples, hostile cases, reference implementation | Cannot verify the machine-readable layer AF claims. |

`RippleLogic_Aligners_Sheet_v5_6.xlsx` was supplied but is a MathGov artifact, not part of the AF release line. It is outside the audit scope you set and I did not audit it.

### 0.3 Version and ownership map

- **Master/reference edition:** `Auditable_Flourishing_v5_9_Core_Protocol`, treated as authoritative throughout.
- **Journal-facing derivative:** `Methods_Article_Submission_Draft` (4,701 words). No claim inflation detected against the core.
- **Normative companions with delegated ownership:** Stage A Operational Anchors (criterion anchors), Legal Rights and Authorization Note (legal boundary), Measurement and Construct Handbook (constructs), Constitutional Legitimacy and Stewardship Charter (CL ladder), Scenario Governance, Reviewer Training and Rating Deposit, Challenge Administration, External Validation Burden and Decision Value, Phase 0 Protocol.
- **Instrument:** External Pilot Aggregation Workbook.
- **Catalog:** Master Reference Catalog.

Version self-declaration is consistent: every companion declares `AF v5.9`. That is a genuine improvement and I found no artifact-name drift among supplied files.

---

# A. EXECUTIVE VERDICT

Auditable Flourishing v5.9 is a serious, unusually disciplined piece of protocol architecture that is currently **undermined by its own delivery layer**. The thinking is stronger than the shipping.

**What is genuinely strong.** The conceptual core holds up under adversarial pressure. The non-compensatory Stage A gate is real, not decorative: `Stage_A!AE4` requires all sixteen administrative and criterion fields to be non-blank before any status is derived, `AI4` demands six positively recognised states, and unrecognised values route to refusal rather than to a pass. That chain is correctly built and I could not break it by blanking, partial population, or unrecognised criterion values. The separation of AF eligibility from legal conformity, moral adequacy, community legitimacy, and deployment authorization is stated in the abstract, diagrammed, tabulated in the authority vector, enforced in §6.5, restated in the conclusion, and independently policed by a formula (`Verdict_Vector!M4`) that rejects bare "approved", "certified", "safe", "ethical", "legitimate", and "compliant" labels. Few frameworks carry a boundary claim that far into their instrumentation.

The mathematics is correct. I independently re-derived every closed-form probability claim in §11.4 and Appendix E and all six exact values reproduce to the digit: P₅(12) = 0.4354%, P₂(12) = 6.2864%, P_mixed = 1.3285%, and the 4/6/8-dimension baselines. The general form P_k(n) = 2[((k+1)/2k)ⁿ − (1/k)ⁿ] is right, and it correctly reduces to both special cases. I re-implemented the Gaussian copula simulation from scratch; both correlated rows reproduce inside my own Monte Carlo interval. The reported standard errors and 95% intervals are arithmetically exact. This is better statistical hygiene than most published methods papers.

Table and figure numbering is clean across a 45-table, 11-figure document: no gaps, no duplicates, no referenced-but-uncaptioned items, no captioned-but-unreferenced items. The three-layer reading structure the brief asks for already substantially exists, "AF in 60 Seconds", "What an AF Finding Does Not Mean", a 501-word abstract, a status-at-a-glance table, and a reader guide, together 1,322 words, all before the argument and all before any release machinery.

**What is materially defective.** Three defect families, and they are not cosmetic.

*First, the artifact chain.* Every one of the eleven supplied `.docx` files is plain UTF-8 Markdown carrying a false extension. Magic bytes are `2a 2a` (`**`), not `50 4b 03 04`. None is a Word document. Appendix C of the master specifically rebuts this exact finding from the 12 August audit as a "selection artifact" and asserts that "the actual v5.8 distribution, whose DOCX files are genuine OOXML and correctly named". Whatever is true of the internal package, the artifact set that reached this auditor is defective in exactly the way the previous one was. Under AF's own root-cause discipline, a second identical observation from a second independent reviewer is evidence about distribution control, not about reviewer selection. A protocol whose thesis is auditability cannot ship a rebuttal of a container defect inside a defective container.

*Second, the instrument's enforcement layer does not exist.* The workbook contains 77 data-validation rules. **Zero are list-type.** Fifty-seven have no `type` attribute and no `formula1` at all, which in OOXML means `type="none"`, they never restrict input and never show a dropdown. The twenty that are typed are all numeric range guards. So every controlled-vocabulary field in the instrument, including the six C0–C5 criterion states and every independence control, is unconstrained free text. The validation nodes still carry `errorStyle="stop"` and the message "Select one exact controlled state. Free text, legacy labels, punctuation variants, and trailing-space variants are invalid and fail closed." That message can never fire. This is a false attestation embedded in the instrument.

*Third, and most serious, the independence architecture fails open.* `Independence!O4` is a **negative blacklist**, not a positive whitelist. It tests `E4="Sponsor controlled - invalid"`, `F4="Sponsor veto - invalid"`, `G4="Sponsor/candidate controlled - invalid"`. Any other string in those three cells, a typo, a case variant, an em dash, a plausible-sounding novel phrase, falls through to `"Adequate"`. Data control, publication control, and reviewer selection are the three most capture-sensitive fields in the entire protocol, they have no dropdown, and they are guarded by an enumeration of bad answers rather than a whitelist of good ones. Both the master's Conclusion ("workbook independence and burden logic use positive whitelists and numeric guards") and Read_Me B23 ("use positive whitelists and fail closed on unknown controls") assert the opposite of what is implemented.

Four further instrument defects compound this. `Dashboard!B8` counts a v5.8 string, `"Stage-A admissible - scoped with verified controls"`, which no formula in the workbook produces. Every control-dependent admissible record is silently dropped from the headline admissibility KPI. `Burden_Log!L` (Access_Support_Required) is validated as a decimal but consumed by `P4` as the text `"Yes"`, so a compliant reviewer disables the accessibility gate entirely. `Reliability_Results!H` and `!I` (CI bounds) are constrained to 0–1, which makes it structurally impossible to record a negative reliability coefficient, the single most important adverse finding Phase 0 could produce, inside a protocol that declares null and adverse results first-class. And there is no `calcPr` element and no `fullCalcOnLoad`, so 1,391 of 1,757 formulas (79%) ship with no cached value and render blank to any non-recalculating viewer.

**Where this leaves AF.** The specification is close to what it claims to be. The delivery is not. v5.9's own stated achievement, "workbook independence and burden logic use positive whitelists", "unrecognised values fail closed", "the master edition is navigable through a clickable contents system", is partly unearned as shipped. The gap between claim and artifact is small in engineering terms and large in credibility terms, because AF's entire proposition is that claims should resolve to inspectable evidence.

None of this touches the conceptual architecture, which I tried hard to break and could not. C0–C5 remain genuinely non-compensatory. Stage B remains genuinely subordinate. Refusal, indeterminacy, and incomparability remain genuinely reachable. The repairs below are mostly engineering, not redesign.

**Disposition: material revision**, driven almost entirely by artifact and instrument defects rather than by the argument. See §O.

---

# B. MASTER-EDITION COMMUNICATION VERDICT

**Is the full master version currently easy enough to navigate and understand for a serious reader who will not read it linearly?**

**Partly. The design is right and the execution is blocked by one delivery failure and one imbalance.**

The design is right. Front matter already does what the brief asks: idea before machinery, doorway before depth, boundary before content. Version history, release hashes, and correction records are already in appendices. A reader path selector already exists. This is better than most 30,000-word technical documents and I would change very little of it.

Two things stop it working.

**The navigation layer does not exist in any artifact a reader can receive.** The master source contains `[[TOC]]`, `[[LIST_OF_TABLES]]`, and `[[LIST_OF_FIGURES]]` build placeholders. Those are correct as source. But the file named `.docx` is Markdown, so there is no clickable TOC, no bookmarks, no navigation pane, and no working cross-references anywhere in the supplied set. The Conclusion's claim that "the master edition is navigable through a clickable contents system" is unverifiable and, for this reader, false. Non-linear navigation is currently impossible.

**The weight distribution fights the reader.** Section 1 is 4,570 words, the largest section in the document, and it sits between the reader and the mechanism. Section 8, the worked scenario, is 4,338 words. Together they are 29% of the body. Meanwhile Stage A, the controlling gate, is 1,620 words and the Formal Protocol is 602. A reader who wants to know how AF actually decides things must travel 4,570 words of framing to reach 1,620 words of mechanism. That is inverted.

Fix both and the answer becomes an unqualified yes. Neither fix requires cutting content.

---

# C. TOP 10 HIGHEST-VALUE IMPROVEMENTS

Ranked by expected improvement, not by ease.

| Rank | Improvement | Where | Why | Severity | Effort |
|---:|---|---|---|---|---|
| 1 | Convert `Independence!O4` from negative blacklist to positive whitelist with explicit unknown-value routing | Workbook, Independence sheet | Sponsor, publication, and reviewer-selection control currently fail open on any unlisted string. This is the protocol's central capture defence and it does not hold. | **P0** | Low |
| 2 | Add list-type data validation to all 57 inert rules; make the promised whitelists real | Workbook, all sheets | 77 validation rules carry stop-level error messages that can never fire. False attestation inside the instrument. | **P0** | Medium |
| 3 | Ship genuine OOXML and stop asserting container integrity that a reader cannot verify | Release pipeline; Appendix C and D | Eleven of eleven `.docx` are Markdown. Second independent occurrence. Appendix C rebuts the finding it is currently demonstrating. | **P0** | Low |
| 4 | Repair `Dashboard!B8` dead v5.8 string and complete the token migration everywhere | Workbook Dashboard; Anchors §2–7 | Control-dependent admissible records are silently counted as zero. Same root cause as two other drift sites. | **P0** | Low |
| 5 | Fix `Burden_Log!L` type contradiction and `Reliability_Results!C/H/I` range errors | Workbook | Accessibility gate cannot fire; negative reliability coefficients cannot be recorded; a categorical column is validated as a decimal. | **P0** | Low |
| 6 | Add `calcPr fullCalcOnLoad="1"` and ship with cached values | Workbook XML | 79% of formulas display blank in non-recalculating viewers. In a fail-closed instrument, blank is the most dangerous rendering. | **P0** | Trivial |
| 7 | Split Section 1 and move Section 8's bulk to an appendix; promote Section 10 | Core §1, §8, §10 | 29% of the body sits between the reader and the mechanism. Nothing needs deleting, only relocating. | P1 | Medium |
| 8 | Define the `N/P` floor tier or eliminate it | Core §6.1, Table 8 | Three dimensions including Non-domination carry a tier value the controlling taxonomy does not define. No routing rule exists for it. | P1 | Trivial |
| 9 | Build and ship the genuine DOCX with real TOC, List of Tables, List of Figures, and bookmarks | Release pipeline | Non-linear reading is currently impossible. This is the single largest usability gain available. | P1 | Medium |
| 10 | Resolve ~30 uncited bibliography entries and bump all v5_8 integrity references to v5.9 | Core References; Appendix D, E | A third of the bibliography is uncited, and v5.9 names v5.8 manifests as its controlling integrity authority. | P2 | Low |

---

# D. CRITICAL DEFECTS (RELEASE BLOCKERS)

Seven. All are verifiable from the supplied bytes. All are repairable without touching the conceptual architecture.

### D-1 — Independence architecture fails open (P0)

**What:** `Independence!O4` uses a negative blacklist on the three capture-critical control fields.

**Evidence:**
```
O4 = IF(COUNTA(A4:W4)=0,"",
     IF(COUNTA(A4:J4)<10,"Indeterminate",
     IF(OR(E4="Sponsor controlled - invalid",
           F4="Sponsor veto - invalid",
           G4="Sponsor/candidate controlled - invalid",
           H4<>"Yes", I4<>"Yes", J4<>"Yes",
           V4<>"Present and frozen",
           W4="Material shared-model generation undisclosed"),"Inadequate",
     IF(OR(...),"Adequate with declared controls","Adequate"))))
```
H, I, J, and V are correctly whitelisted (`<>"Yes"` → Inadequate). E, F, and G are blacklisted.

**Attack that succeeds:** A host enters `Sponsor-controlled (invalid)` in E4, semantically identical, textually different. The blacklist misses. H/I/J/V are satisfiable independently. `O4` returns `"Adequate"`. If N4 also reads "Adequate", `P4` returns `MATCH`, and `Dashboard!B11` counts zero independence exceptions. The capture is invisible at every layer.

**Why the current form is inadequate:** Enumerating bad answers is unbounded; enumerating good answers is bounded. AF states this principle itself and then does not apply it here. With inert data validation (D-2) there is nothing constraining the input either.

**How to repair:** Invert to a positive whitelist. Any value in E, F, or G outside the named admissible set routes to `"Indeterminate"` (not "Inadequate", an unrecognised string is an evidence problem, not an established defect). Add a companion `Vocabulary_Check` column returning `UNRECOGNISED_CONTROL_VALUE`, surfaced on the Dashboard alongside the existing integrity exceptions.

**Acceptance test:** Enter three novel strings into E4, F4, G4. `O4` must return `Indeterminate`, the vocabulary check must return `UNRECOGNISED_CONTROL_VALUE`, and the Dashboard exception count must increment. Repeat for correct whitelist values and confirm `Adequate` still reachable.

---

### D-2 — All controlled-vocabulary validation is inert (P0)

**What:** 57 of 77 `dataValidation` nodes have no `type` attribute and no `formula1`. Under ECMA-376 this is `type="none"`: no restriction, no dropdown, no enforcement. The remaining 20 are numeric guards. **Zero list-type validations exist in the workbook.**

**Evidence, raw sheet XML, Stage_A:**
```xml
<x:dataValidation errorStyle="stop" showErrorMessage="1"
  errorTitle="Invalid Stage A criterion state"
  error="Select one exact controlled state. Free text, legacy labels,
         punctuation variants, and trailing-space variants are invalid
         and fail closed."
  sqref="K4:P60" />
```
No `type`. No `<formula1>`. The error can never fire.

**Distribution of inert rules:**

| Sheet | Inert | Typed | Fields left unconstrained |
|---|---:|---:|---|
| Stage_A | 11 | 0 | K:P (the six C0–C5 criterion states), H, I, J, R |
| Profile_Routing | 10 | 0 | D–L, N (all AF-Lite/Standard/High-Consequence routing) |
| Independence | 9 | 0 | E, F, G, H, I, J, N, V, W |
| Reliability | 6 | 0 | all layer/eligibility fields |
| Decision_Value | 4 | 0 | all |
| Rating_Deposits | 4 | 0 | immutability and deposit-status fields |
| Candidate_Register, Scenario_Register | 4 | 0 | all |
| Verdict_Vector | 1 | 0 | D (status) |
| Study_Readiness | 1 | 0 | all |
| Perturbation_Register | 7 | 2 | admission/rejection fields |
| Burden_Log | 0 | 11 | (numeric only) |
| Reliability_Results | 0 | 7 | (numeric only) |
| **Total** | **57** | **20** | |

**Mitigating factor, stated fairly:** Stage_A has genuine downstream defence. `AI4` counts recognised states and returns `UNRECOGNISED_VALUE`, which routes through `AE4` to `Q4` as `"Protocol refusal to evaluate"`. So Stage_A does fail closed on bad criterion values even without dropdowns. That is good defence in depth and it should be preserved. But it misclassifies a substantive finding as an administrative one (see D-6), and it does not extend to Independence, Profile_Routing, Rating_Deposits, or Verdict_Vector.

**How to repair:** Add `type="list"` with an explicit `<formula1>` for every controlled field, sourced from a new hidden `Vocabulary` sheet holding the canonical strings from core Table 5B, Table 5, and Table 8M. Do not inline the lists as literal strings, a single source enables one-line migration at v6.1.

**Acceptance test:** Open in Excel and LibreOffice. Every controlled cell shows a dropdown. Typing a non-list value is rejected with the stated error. `openpyxl` reports `formula1` non-null for all 77 rules.

---

### D-3 — Container integrity: eleven false `.docx` (P0)

**What:** Every supplied `.docx` is plain UTF-8 Markdown with a false extension.

**Evidence:**

| File | First 4 bytes | Required |
|---|---|---|
| Auditable_Flourishing_v5_9_Core_Protocol.docx | `2a 2a 41 55` (`**AU`) | `50 4b 03 04` |
| Challenge_Administration_Handbook_v5_9.docx | `2a 2a 43 48` (`**CH`) | `50 4b 03 04` |
| Constitutional_Legitimacy..._v5_9.docx | `2a 2a 43 4f` | `50 4b 03 04` |
| External_Validation_Burden..._v5_9.docx | `2a 2a 45 58` | `50 4b 03 04` |
| Legal_Rights_and_Authorization_Note_v5_9.docx | `2a 2a 4c 45` | `50 4b 03 04` |
| MASTER_REFERENCE_CATALOG_v5_9.docx | `2a 2a 4d 41` | `50 4b 03 04` |
| Measurement_and_Construct_Handbook_v5_9.docx | `2a 2a 4d 45` | `50 4b 03 04` |
| Phase_0_Feasibility..._v5_9.docx | `2a 2a 50 48` | `50 4b 03 04` |
| Reviewer_Training..._v5_9.docx | `2a 2a 52 45` | `50 4b 03 04` |
| Scenario_Governance..._v5_9.docx | `2a 2a 53 43` | `50 4b 03 04` |
| Stage_A_Operational_Anchors_v5_9.docx | `2a 2a 53 54` | `50 4b 03 04` |

All eleven `.docx`/`.md` pairs are also **byte-divergent under the same version label**. The `.docx` variants are Markdown plus a bolded title line and a flattened plain-text table of contents carrying page numbers that are visibly stale (many entries read `·· 1`). They are pre-render text drafts, not built output.

**Why this is the most serious of the seven:** Appendix C states that the prior audit's "false-filename observation does not apply to the actual v5.8 distribution, whose DOCX files are genuine OOXML and correctly named", dispositioned as *"Rejected for actual distribution, selection artifact; actual package verified."*

I make no claim about the internal package I cannot see. I make a narrow, verifiable claim: **the set that reached this reviewer exhibits precisely the defect Appendix C rejects, and this is the second independent occurrence.** AF's own root-cause rule says a distinct finding requires a distinct causal defect. Two reviewers receiving false containers from the same programme is one causal defect in distribution control, and the correct owner is C0/C2, not the reviewers.

**How to repair:** Three parts, in order.
1. Build genuine OOXML for all twelve documents and verify magic bytes plus `unzip -t` plus a python-docx open test on each before hashing.
2. Rewrite Appendix C's first paragraph. Replace the rejection with an accurate statement: the internal package was verified, *and* two independent reviewers received non-conforming derivatives, which is itself a C0 finding about distribution control. Record the corrective control.
3. Publish a one-page `HOW_TO_VERIFY.md` at package root giving the three-signal check, so any reader can self-verify in thirty seconds rather than trusting an attestation.

**Acceptance test:** `head -c 4 f | od -An -tx1` returns `50 4b 03 04` for all twelve. `unzip -t` passes. python-docx opens each. SHA-256 manifest computed hash-last after format freeze. A reviewer given only the ZIP can verify without contacting the author.

---

### D-4 — Dashboard silently undercounts admissibility (P0)

**What:** `Dashboard!B8` counts a string no formula produces.

**Evidence:**
```
B8 = COUNTIF(Stage_A!Q4:Q60,"Stage-A admissible - scoped")
   + COUNTIF(Stage_A!Q4:Q60,"Stage-A admissible - scoped with verified controls")
```
`Stage_A!Q4` produces exactly two admissible strings:
- `"Stage-A admissible - scoped"`
- `"Stage-A admissible - scoped, control-dependent"`

The second `COUNTIF` term is a **v5.8 label**. It matches nothing, returns 0 silently, produces no error token, and triggers no integrity exception. Every control-dependent admissible record vanishes from the headline KPI.

**Root cause:** The v5.9 changelog states the release "renames controlled admissibility as control-dependent". The rename was applied to core Table 5, Table 5B, Appendix G, the Anchors companion §1.4, and `Stage_A!Q4`/`AF4`. It was not applied to `Dashboard!B8`. The same incomplete migration produced D-8 below.

**How to repair:** Replace the literal with `"Stage-A admissible - scoped, control-dependent"`. Then source both strings from the `Vocabulary` sheet introduced in D-2 so no literal status string appears in any formula.

**Acceptance test:** Populate one plain-admissible and one control-dependent row. `B8` returns 2. Add a `Vocabulary_Coverage` check that fails if any Dashboard `COUNTIF` criterion is absent from the canonical vocabulary list.

---

### D-5 — Accessibility gate cannot fire (P0)

**What:** `Burden_Log!L` is validated as a number and consumed as text.

**Evidence:**
- Header: `L = Access_Support_Required`
- Validation: `L4:L60  type="decimal"  operator="greaterThanOrEqual"  formula1=0`
- Consuming formula, `P4`: `...AND(L4="Yes",OR(M4<>"Yes",N4<>"Yes"))...` and `IF(L4="Yes","Feasible with verified support",...)`

A reviewer who obeys the validation enters a number. `L4="Yes"` is then FALSE, the access-support conjunct is skipped, and `P4` can return `"Feasible"` while access support is required, unfunded, and undelivered. A reviewer who enters `"Yes"` is blocked by `errorStyle="stop"`.

**Why this matters beyond a typo:** This is the equity conjunct of the conjunctive burden gate. §7.6 and the Read_Me both treat accessibility and translation support as protection, not convenience. The one numeric guard that *is* active on this sheet disables the one non-numeric protection on it.

**How to repair:** Change `L4:L60` to `type="list"` with `formula1="Yes,No"`. Apply the same to `M` and `N` (currently unvalidated). Add a guard so `P4` returns `"Not feasible"` when L, M, or N is not one of `Yes`/`No`.

**Acceptance test:** L="Yes", M="No", N="No" → `P4` = "Not feasible". L=1 → rejected at input. L blank with other fields populated → "Not feasible", never "Feasible".

---

### D-6 — Reliability instrument cannot record adverse results (P0)

**What:** Two errors on `Reliability_Results`, one a range error and one a column-type error.

**Evidence:**

| Column | Header | Validation | Problem |
|---|---|---|---|
| C | `Decision_Layer` | `decimal between 0 and 1` | **Categorical field validated as a decimal.** Decision_Layer must hold "Stage A criterion", "Stage A final", "Stage B dimension", "Stage B final". A compliant reviewer enters a number and destroys layer separation; a correct reviewer is blocked. |
| H | `CI_Lower` | `decimal between 0 and 1` | **Negative values impossible.** |
| I | `CI_Upper` | `decimal between 0 and 1` | Same. |
| G | `Estimate` | *(none)* | Point estimate may be negative while its own interval may not. Internally incoherent. |
| J | `Confidence_Level` | `decimal between 0 and 1` | Acceptable, but no unit declared. 95 is rejected, 0.95 required, and the header says neither. |

Core §7.3 explicitly admits "Gwet's AC1, Krippendorff's alpha, or another justified coefficient". Every one of those can legitimately be **negative** under below-chance agreement. A Phase 0 study returning AC1 = 0.04 with a 95% interval of [−0.09, 0.17], a textbook adverse reliability finding, and arguably the most decision-relevant result the pilot could produce, **cannot be entered into the instrument.**

This directly contradicts `Dashboard!D20` ("Null/adverse results are first-class"), Read_Me B13, and §11.3. The protocol commits to publishing adverse findings and then ships an instrument that structurally excludes the principal adverse finding.

**How to repair:** `C` → `type="list"` from the four canonical decision layers. `H`, `I`, `G` → `decimal between -1 and 1`. Add a cross-field check that `H ≤ G ≤ I` and flag violations. Rename `J` to `Confidence_Level_Proportion` or validate `between 0 and 1` with an explicit header note.

**Acceptance test:** Enter AC1 = 0.04, CI [−0.09, 0.17], layer "Stage A criterion". All four accepted. Enter CI_Lower > CI_Upper → flagged. Enter layer "0.5" → rejected.

---

### D-7 — 79% of formulas ship uncached (P0)

**What:** The workbook has **no `calcPr` element at all** and no `calcChain.xml`.

**Evidence:** 1,757 formula cells; 1,391 (79.2%) have no cached value.

| Sheet | Formulas | Uncached | % |
|---|---:|---:|---:|
| Stage_A | 627 | 336 | 54% |
| Burden_Log | 228 | 220 | 96% |
| Perturbation_Register | 192 | 187 | 97% |
| Reliability | 171 | 159 | 93% |
| Independence | 114 | 113 | 99% |
| Profile_Routing | 114 | 110 | 96% |
| Decision_Value | 114 | 108 | 95% |
| Study_Readiness | 114 | 104 | 91% |
| Verdict_Vector | 57 | 52 | 91% |
| Dashboard | 26 | 2 | 8% |

**Why this is P0 rather than cosmetic:** In a fail-closed instrument, blank is the most dangerous possible rendering, because blank is exactly what the design uses to mean "no record here". A reviewer opening this in Google Sheets preview, a mobile viewer, Quick Look, or any read-only web renderer sees blank `Derived_Overall_Status`, blank `Status_Match`, blank `Derived_Feasibility`, and blank `Derived_Status` on Independence. Those are the four columns the entire integrity architecture depends on. `Dashboard!B17` and `B18`, the Stage B reliability KPIs, are themselves uncached.

**How to repair:** Add `<calcPr calcId="191029" fullCalcOnLoad="1"/>` to `xl/workbook.xml`. Then recalculate headless in LibreOffice before hashing so cached values ship populated. Both, not either.

**Acceptance test:** `zipfile` read of `xl/workbook.xml` shows `fullCalcOnLoad="1"`. `openpyxl` with `data_only=True` returns a non-null value for every formula cell in a populated row. Open in a non-recalculating viewer and confirm no derived-status column is blank where inputs exist.

---

# E. SUBSTANTIVE SCIENTIFIC ANALYSIS

## E.1 Verdict by axis

The brief asks for separate verdicts and forbids compression. Here they are.

| Axis | Verdict | Basis |
|---|---|---|
| Conceptual coherence | **Strong** | I attempted category-mistake attacks across §3.4, §5, §6.5, §12 and found no place where eligibility silently becomes approval, compliance, certification, proof of flourishing, or authorization. |
| Construct validity | **Adequate but externally unvalidated** | Constructs are operationally anchored and floor-linked. Anchor overlap, factor structure, and architecture-family bias are acknowledged as open with a named falsification trigger (C3-D07). Nothing is empirically established. |
| Internal specification completeness | **Specification-complete with three gaps** | The `N/P` tier (§E.5), the missing derived path to "Out of scope" (§F-8), and the anchors label drift (§E.6). |
| Falsifiability | **Strong** | The dimension-set falsification condition in §6.1 is unusually explicit and genuinely disconfirmable. H-Y1 to H-Y4 are preregistrable. AF states conditions under which it should be retired. |
| Evidence discipline | **Strong in text, materially defective in instrument** | The document is scrupulous. The workbook contradicts it at three points (D-1, D-5, D-6). |
| Measurement architecture | **Adequate** | Ordinal discipline is enforced, arithmetic prohibited, evidence maturity separated from category. See §E.7 for the residual documentation-bias risk. |
| Statistical architecture | **Strong** | Fully reproduced. See §E.4. |
| Rights protection | **Strong** | Non-derogable protections correctly handled; principled non-equivalence is bilateral; emergency stacking is explicitly blocked with renewal counting and escalation. See §E.8. |
| Constitutional legitimacy | **Honestly incomplete, correctly labelled** | CL1 self-assessment, CL2 design materials only. The status is stated in the abstract, in Table S1, and in the charter. No laundering detected. |
| Challenge and appeal architecture | **Adequate** | Standing, dissent preservation, appeal routes, and rejection reasons are specified. Untested. |
| Institutional independence | **Materially defective as implemented** | Specification is good; instrument fails open (D-1). |
| Anti-capture protection | **Adequate in design, defective in instrument** | Same split. |
| Anti-gaming protection | **Adequate** | Perturbation admission gate, C2-D05 for strategic multiplication, applicability-abuse rule. |
| Operational implementability | **Pilot-ready after repairs** | Blocked by D-1 to D-7 only. |
| Burden and proportionality | **Adequate** | Conjunctive gate is genuinely conjunctive; burden is treated as possible harm; cohorts separated. One defect (D-5). |
| Empirical validation readiness | **Design-ready, not materials-ready** | Correctly self-labelled. D-6 must be fixed first or the pilot cannot record its own key result. |
| Usability | **Incomplete** | No navigable artifact exists; workbook lacks frozen panes and filters on 35-column sheets. |
| Communication quality | **Strong** | Prose is disciplined, claim boundaries explicit, no AI-writing markers, no em dashes in body prose. |
| Visual quality | **Not assessable** | Zero figures supplied. |
| Publication readiness | **Not yet** | Container defects and ~30 uncited references. |
| Master-reference-document readiness | **Material revision** | See §O. |

## E.2 Is AF evaluating the correct object?

Yes, and it says so with unusual precision. The abstract opens by stating AF "evaluates the decision architecture and evidentiary claims of frameworks that claim to support flourishing; it does not directly measure, certify, own, or guarantee" flourishing. §3.4.1's authority-specific verdict vector separates the findings structurally rather than rhetorically, and `Verdict_Vector!M4` enforces it in the instrument.

I probed for the five prohibited slides and found no textual leakage:

| Prohibited inference | Where blocked | Holds? |
|---|---|---|
| eligibility → ethical approval | §3.4, §5.3.1 line 545, §6.5, §12 | Yes |
| eligibility → legal compliance | §5.3.1, §5.4, Legal Note delegation | Yes |
| eligibility → certification | Front matter §2, Read_Me B6, Appendix A | Yes |
| eligibility → proof of flourishing | Abstract, §3.1, §12 | Yes |
| eligibility → deployment permission | §3.4, §6.5, Table S1 "Domain authorization: Not granted" | Yes |

**One residual risk, low severity.** The public string `"Stage-A admissible - scoped"` contains no negative marker. In downstream quotation it will be shortened to "AF admissible" and then to "AF passed". The protocol anticipates this, `Stage_A!AG4` requires the public string to embed both the canonical token and the version. But `AG4` hard-codes the literal `"AF v5.9"` inside the formula, which will silently invalidate every public-string check at v6.0 unless someone remembers to edit it. Move the version literal to the `Vocabulary` sheet.

## E.3 Non-compensation, subordination, root cause, and refusal

All four hold under test.

**C0–C5 non-compensatory.** `AH4=6` is required for plain admissibility, `AH4+AD4=6` with `AD4>0` for control-dependent. Any `AA4>0` or `AB4>0` short-circuits before adequacy is reached. There is no averaging, no weighting, and no offset path. Verified in formula, not merely in prose.

**Stage B subordinate to Stage A.** §6.1 line 652: a newly established material C0–C5 defect "suspends Stage B and returns the candidate to Stage A before any Stage B outcome is assigned". Floor-linked category reachability (Tier F → mandatory Stage A re-entry) enforces this at the descriptor level. Strong comparative performance cannot erase a constitutional-class defect. Confirmed.

**Root-cause non-duplication.** §5.1 requires one primary criterion owner per root cause and forbids the same defect becoming several penalties. This is correct and, notably, it cuts *against* the protocol's own interest in appearing thorough. That is a good sign.

**Refusal and indeterminacy genuinely reachable.** All six honest outcomes the brief asks about are reachable and reachable *by formula*, not just by prose: insufficient evidence (`INDETERMINATE`), incomparable (`invariant_crossing`), non-decisive (three named subreasons), protocol refusal (four named triggers), revise/restrict (patchable), retire (C4 triggers and the dimension-set falsification condition). This is the strongest part of the architecture.

## E.4 Independent reproduction of all statistical claims

I re-derived every formula from first principles and re-implemented the simulation without reference to the cited script.

**Closed forms, all correct.**

For k equiprobable categories, P(a ≥ b) = (k+1)/2k and P(a = b) = 1/k. Either-direction strict dominance over n independent dimensions is therefore 2[((k+1)/2k)ⁿ − (1/k)ⁿ]. The Appendix E general form is right and reduces correctly to both stated cases.

| Claim | Stated | Reproduced | Result |
|---|---|---|---|
| P₅(4) | 25.60% | 25.6000% | ✅ |
| P₅(6) | 9.32% | 9.3184% | ✅ |
| P₅(8) | 3.36% | 3.3587% | ✅ |
| P₅(12) | 0.4354% | 0.4354% | ✅ |
| P₂(12) | 6.2864% | 6.2864% | ✅ |
| P_mixed | 1.3285% | 1.3285% | ✅ |

`P_base(t,d) = 2[((1+t)/2)^d − t^d]` is also correct and consistency-checks: at t = 1/5 it returns exactly P₅(12) = 0.4354%.

**Simulations, reproduce within Monte Carlo error.**

Independent implementation: equicorrelated Gaussian latent, Cholesky, standard-normal quintile cuts, 500,000 draws, independent profiles.

| ρ | Stated | My reproduction | My 95% interval | Inside? |
|---|---|---|---|---|
| 0.30 | 11.2418% | 11.2326% | [11.1451, 11.3201] | ✅ |
| 0.60 | 34.4388% | 34.5570% | [34.4252, 34.6888] | ✅ (marginally) |
| 0.00 control | 0.4354% exact | 0.4422% simulated | — | ✅ |

The reported standard errors and intervals are arithmetically exact: √(p(1−p)/500000) gives 0.0447 pp and 0.0672 pp, and ±1.96 SE reproduces the stated bounds to four decimals.

**Assessment.** This is honest, well-executed, well-bounded statistical work. Table 23's "none is an empirical forecast" caveat is correct and load-bearing. §11.4's refusal to promote any predicted distribution to fact is exactly right.

**Two notes.**
1. The ρ = 0.60 point estimate sits near my interval edge (about 1.75 SE from my estimate). That is consistent with different RNG streams and is not evidence of error. But it cannot be *confirmed* as seed-matched replication because `stage_b_yield_simulation_v5_8.py` was not supplied. The SHA-256 pin is therefore an attestation, not a reproducible artifact, for any reader who receives what I received.
2. The script and its outputs carry `v5_8` in the filename inside a v5.9 release. If the simulation is unchanged, say so explicitly in Appendix E. If it changed, the name is wrong.

**Is Stage B decision-informative even when dominance is rare?** Yes, and §6.5 argues this correctly and without special pleading. The primary-output rule makes dominance supplementary rather than the endpoint, and H-Y4 preregisters the possibility that decision value is positive while yield is low. This is intellectually honest and I would not change it.

## E.5 The `N/P` floor-tier defect (P1)

**Observation.** §6.1 line 597 defines exactly three floor-linkage tiers: **F** fully floor-linked, **P** partly floor-linked, **N** not ordinarily floor-linked. Each has a distinct routing consequence: Tier F prohibited descriptors "necessarily return to Stage A"; Tier P "requires case-specific routing"; Tier N "remains comparative unless independent evidence establishes a C0-C5 defect".

**Evidence.** Table 8 assigns the value `N/P` to three dimensions: Non-domination, Ecological adequacy, and Institutional compatibility.

**Inference.** `N/P` is not in the taxonomy and has no routing rule. A reviewer who assigns Non-domination category 0 ("opaque/coercive") has no defined instruction: return to Stage A, route case-specifically, or continue comparing. In a non-compensatory architecture where floor tiers are the mechanism by which Stage B defers to Stage A, an undefined tier on a dimension named *Non-domination* is not a typographical matter.

**Repair.** Either define a fourth tier explicitly with its own routing rule, or resolve each of the three to F, P, or N. I recommend resolving to **P** (partly floor-linked, case-specific routing) for all three, since that is what `N/P` appears to intend and it is the conservative choice. Then add an acceptance check that every Table 8 tier value is a member of the declared set.

## E.6 Canonical token migration is incomplete (P2, three sites, one root cause)

Under AF's own root-cause discipline this is **one defect with three manifestations**, and it should be dispositioned as one.

**Root cause:** the v5.8 → v5.9 rename of "controlled" to "control-dependent" was applied to the core, Appendix G, the Anchors companion §1.1/§1.4, and `Stage_A!Q4`/`AF4`, but not everywhere.

| Site | Drift | Severity |
|---|---|---|
| `Dashboard!B8` | counts dead v5.8 string | **P0** (D-4) |
| Anchors companion §2–§7 anchor tables | row labels read "Adequate with controls", "Patchable defect", "Unpatchable for stated claim" | P2 |
| `Stage_A!AG4` | version literal `"AF v5.9"` hard-coded in formula | P2 |

**On the Anchors drift specifically, I tested a stronger hypothesis and rejected it.** My first reading was that three of the six canonical criterion states had no anchors at all, which would have been P0. That is wrong. §1.1 declares all six canonical machine tokens correctly and §1.4 reproduces all nine canonical public statuses verbatim and correctly. The drift exists only in the per-criterion anchor table row headings in §2–§7. Since those are descriptive row labels rather than token declarations, the severity is **P2, not P0**.

It still matters, because §2–§7 are the pages a reviewer actually works from, and with inert dropdowns (D-2) nothing corrects a reviewer who types what the anchor table shows them. Repair: align the row labels to the canonical strings. Cost is trivial; benefit is that the operative pages and the instrument speak the same language.

## E.7 Measurement architecture and the documentation-bias question

The brief asks whether polished institutions could systematically outperform less documented but substantively protective systems. AF has thought about this harder than most.

**What is genuinely well handled.** Table 7 explicitly frames C0–C5 as "functional safeguards, not mandates to imitate a computational or MathGov-shaped artifact set", and gives non-computational evidence examples for every criterion (charters, precedent records, minutes, dissent logs, community-defined indicators, non-consensus process). §5.3.1's principled non-equivalence route lets a customary, Indigenous, religious, or community architecture demonstrate functionally equal or stronger protection without copying legal instruments, and makes the rebuttal **bilateral**, the reference baseline itself is challengeable. §7.6.1 addresses non-documentary evidence, data sovereignty, and polish neutrality directly. §9.1's deliberative mini-public dry run is a real attempt to falsify architecture bias, and §9.2 preregisters an architecture-diversity calibration suite.

**Where residual risk remains.** Three places, all acknowledged by AF but none yet closed.

1. The common anchor ladder (§6.1.1) uses categories 3 and 4 that both require *independent challenge* and *cross-context demonstration*. Those are resource-intensive evidence forms. A well-funded institution can commission independent review; a community process often cannot, even where its substantive protection is stronger. The ladder therefore has a structural wealth gradient at its top two rungs. AF's assisted-dossier and resource-equity provisions (§7.6) mitigate but do not remove this.
2. The materiality test (§5.1) requires reviewers to record "decision relevance, floor implication, comparison effect, evidence, and a falsifiable patch condition". This is good discipline and it is also a documentation demand. Its burden falls asymmetrically.
3. "Adequate", "material", "verified", and "indeterminate" are anchored in the Anchors companion, which is 1,707 words covering six criteria. That is roughly 280 words per criterion for minimum record, adequacy, controls, patchable, unpatchable, indeterminate, boundary cases, and disconfirming evidence. That is thin for a two-reviewer independent-reproduction claim.

**Recommendation.** Do not add more anchor text. Instead, preregister the wealth-gradient question as a named Phase 0 diagnostic: measure whether category-3/4 attainment correlates with candidate resourcing independently of substantive protection. Make it a falsification trigger alongside C3-D07. This costs nothing now and makes the concern testable rather than rhetorical.

## E.8 Rights and legal architecture

**What holds.**

Non-derogable protections are correctly identified and correctly sourced: ICCPR Art. 4(2), HRC General Comment 29, and CESCR minimum essential levels. Crucially, §5.3.1 states the baseline is "not treated as a complete universal moral theory, a substitute for applicable local law, an automatic hierarchy over Indigenous, customary, religious, or community governance, or proof that every provision is culturally or institutionally sufficient". That is the right posture and it is stated without hedging.

Rights floors cannot be compensated by aggregate benefit. §5.3.1 line 547 is explicit that proportionality and derogation are "contested legal practices rather than arithmetic balancing rules", cites the genuine disagreement (Alexy, Tsakyrakis, Webber, Siracusa), and routes such claims to competent legal authority rather than deciding them. AF tests whether the candidate *identified* the elements; it does not adjudicate them. That distinction is held consistently.

Emergency powers cannot be stacked. §5.4 is one of the strongest passages in the document: renewal count, cumulative duration, predeclared escalation limit, non-automatic renewal with fresh necessity at each extension, first-renewal escalation trigger, and an explicit statement that repeated provisional actions "cannot be stacked into de facto ordinary operation". Table 16's rights-bypass probe tests for exactly this. I could not construct a stacking attack that the text permits.

The worked floor-conflict example (§5.3.2, outbreak data) demonstrates the non-aggregation rule concretely rather than asserting it.

**Anti-liability-shield architecture.** I tested each of the five misuse claims the brief names.

| Could an institution cite AF as… | Blocked where | Adequate? |
|---|---|---|
| proof of due diligence | Front matter §2 explicitly lists "proof of due diligence"; Read_Me B6; Read_Me B11 forbids exporting "Due-Diligence" labels | Yes |
| immunity | Read_Me B6 "not a … liability safe harbor" | Yes |
| certification | Front matter §2; Appendix A; token rename motivated by "reduces certification implication" | Yes |
| proof harm was unforeseeable | **Not explicitly addressed** | **No — see below** |
| substitute for continued monitoring | Expiry and requalification fields are mandatory; C4 monitoring triggers | Partly |

**Gap identified (P2).** The "harm was unforeseeable" defence is the one liability route AF does not name. An institution could argue: *AF reviewed our tail-risk adequacy under §6.3 and found it adequate, therefore the harm that materialised was outside reasonable foresight.* Nothing in the current text forecloses this, and §6.3's tail-risk method table is precisely the surface such an argument would use.

**Repair.** Add one sentence to the "What an AF Finding Does Not Mean" front-matter page and one row to the Read_Me: *an AF finding on tail-risk method adequacy concerns the declared method's fit to declared epistemic conditions at the evidence cut-off; it is not a finding that any particular harm was foreseeable or unforeseeable, and it does not bear on foreseeability in any legal forum.* Cost: two sentences. Benefit: closes the last open liability-laundering route.

## E.9 Constitutional legitimacy and power

Assessed as a skeptical constitutional theorist would.

**Who defines C0–C5, and is that status stated consistently?** Yes, and this is handled better than I expected. §1.9.1 states plainly that "the constitutional class is not a neutral convenience placed on top of a value-free comparison. It is the protocol's central normative claim." The abstract calls C0–C5 "a proposed constitutional class for framework comparison, not a universal constitution established by authorial assertion." §1.9.2 publishes the genealogy and derivation order. §1.9.3 publishes rival formulations and dissent routes. Table S1 records the legitimacy status as **CL1 self-assessment, CL2 design materials only**. I found no place where CL1 is described as more than CL1.

**Can partial legitimacy be laundered into universal legitimacy?** The CL0–CL6 ladder is the right instrument and the honest self-placement at CL1 is the right answer. The risk is not in the document; it is in downstream quotation, where "CL1" will disappear and "constitutionally legitimate" will remain. Recommendation: bind the CL level into the public status string the way version and scope already are, and check it in `AG4` alongside the token and version. This is a one-line instrument change with a large anti-laundering payoff.

**Could AF become institutional orthodoxy?** §1.9.1's second limit ("exclusion is scoped: non-admissibility for an authority role does not establish that a framework is worthless") and §11.7's stewardship, amendment, succession, and capture-resistance provisions address this. The document explicitly contemplates its own retirement. I could not find hidden centralization of epistemic authority in the text.

**Where the legitimacy architecture is genuinely weak, and correctly labelled as such.** No independent convention has occurred. No affected-party body has ratified anything. §11.6 names the programme risks honestly: candidate recruitment may fail, legitimacy processes may stall without independent funding and convening authority, some domains may lack enough qualified reviewers. Naming these is the right move. They remain unresolved and no amount of specification will resolve them.

**One structural observation.** Resource-rich actors can dominate the legitimacy process, and the charter does not currently bound this. The Constitutional Legitimacy and Stewardship Charter is 1,137 words, the shortest normative companion after Scenario Governance. For the document carrying the protocol's central legitimacy claim, that is thin. It is the companion I would expand at v6.0, specifically on convening funding, standing thresholds, and minority-view preservation.

## E.10 Independence and auditability under hostile conditions

I ran the ten corruption scenarios the brief specifies against the artifacts as built.

| Scenario | AF detects/resists? | Basis |
|---|---|---|
| Sponsor wants a favourable result | **Fails open** | D-1: blacklist not whitelist on E/F/G |
| Host wants a predetermined outcome | Partly | Host-precommitment and host-interest fields exist (`Independence!R`, `S`) but are unvalidated |
| Reviewers have conflicts | Detects | `K` financial interests, `L` intellectual affiliations, routed to "Adequate with declared controls" |
| Selective disclosure by candidate owners | Detects | §5.2 symmetric evidence access; `AC` count catches unreviewed criteria |
| Strategic documentation generation | Partly | §7.6.1 polish neutrality; no positive detection mechanism |
| Negative findings inconvenient to publish | Detects in spec, **fails in instrument** | `I` null/adverse publication right is whitelisted (`<>"Yes"` → Inadequate); but D-6 makes the key adverse result unrecordable |
| Reviewers use the same AI system | Detects | `W` shared-model rating status with disclosed/undisclosed split; `Reliability!Z`, `AA` per-reviewer AI assistance |
| Post-discussion ratings edited | Detects | `Reliability!L`, `M` discussion-changed flags; `AC` layer-agreement eligibility; Rating_Deposits immutability import |
| Powerful institution controls evidence custody | **Fails open** | Same as D-1: `E` Data_Control is blacklisted |
| Affected parties fear retaliation | Not addressed | No anonymity or protected-reporting channel specified |

**Actual independence versus declared independence.** AF is unusually good at knowing the difference. §7.2 is titled "Adjudicator and host independence: **mechanism, not assurance**". Read_Me B20 states flatly that "the workbook cannot create immutability", and B5 confines the instrument to "prospective aggregation after records are captured in independently controlled, timestamped, hash-bound systems". That is the correct scope declaration and it is the answer to the brief's question about whether the workbook is trying to perform functions requiring an immutable external system. **It is not, and it says so.** Credit where due.

**Two additions worth making at v6.0.**
1. An affected-party protected-reporting channel with anonymity provisions. Currently `J` records affected-party representation but nothing addresses retaliation risk, which §11.6 implicitly acknowledges when it worries about legitimacy processes stalling.
2. Validation on `R` (Host_Interest_in_Outcome) and `S` (Host_Precommitment). These are currently free text feeding nothing.

## E.11 Hostile review

Second pass, attempting to reject AF. Classified honestly, including the attacks that fail.

| Attack | Classification | Reasoning |
|---|---|---|
| Circularity: AF evaluates frameworks using criteria derived from a framework | **Serious but repairable** | §1.9.2 publishes genealogy and derivation order, and §11.5 applies C0–C5 to AF itself with honest "no current code established" entries. But the self-audit is author-conducted and says so. The repair is external administration, which AF already names as the next step. |
| MathGov-native bias | **Already adequately answered** | Table 7 architecture-appropriate evidence, §9.1 mini-public dry run, §9.2 diversity calibration suite, Appendix A competing-interests declaration naming MathGov as a disclosed seed entrant only. |
| Moral imperialism | **Weak** | §5.3.1's bilateral rebuttal and explicit refusal to treat the baseline as universal moral theory answers this. The reference baseline is challengeable by candidate, affected party, *or* reviewer. |
| Measurement invalidity | **Serious but repairable** | Honest. C3-D07 exists precisely for this and has a named falsification condition. Unresolved until Phase 0. |
| Excessive complexity | **Serious but repairable** | 30,928 words plus eleven companions plus a 16-sheet instrument. AF-Lite is the answer but is under-specified relative to AF-Standard. See §K-4. |
| Administrative infeasibility | **Serious but repairable** | The conjunctive burden gate is real and genuinely fails closed. Whether a small institution can run AF-Lite is untested and §11.6 admits it. |
| Documentation bias | **Serious but repairable** | See §E.7. Mitigated in design, unquantified in evidence. |
| Elite capture | **Serious — and currently worse than the text admits** | D-1 makes this concrete rather than theoretical. |
| Legal overreach | **Mistaken** | AF repeatedly declines to decide proportionality, derogation, or conformity, and delegates to the Legal Note. The one gap is foreseeability (§E.8). |
| False reassurance | **Serious but repairable** | The five prohibited inferences are well blocked in the master. The risk is downstream quotation, addressed by binding CL level into the public string. |
| Audit theatre | **Already partly answered** | §11.3 explicitly names audit theatre as a threat and preregisters detection. Dashboard B7/B11 count integrity exceptions. Strengthened by fixing D-1. |
| Statistical underpower | **Already adequately answered** | §11.4 states Phase 0 "is not powered for general yield claims". Correct and unusually candid. |
| Reviewer subjectivity | **Serious but repairable** | Anchors exist but are thin (§E.7). Inter-rater reliability is the whole point of Phase 0. |
| Independence theatre | **Serious — currently the strongest attack** | §7.2 correctly frames independence as mechanism not assurance, then the mechanism fails open. This is the attack I would lead with as a hostile reviewer. |
| High non-decisive rates | **Weak** | §6.5 and the primary-output rule pre-empt this. Incomparability is defended as faithful representation, not failure. |
| Cannot recruit candidate frameworks | **Serious, acknowledged, unrepaired** | §11.6 names it as a programme risk. No specification fixes it. |
| Cannot convene legitimacy processes | **Serious, acknowledged, unrepaired** | Same. Needs funding and convening authority, not text. |
| Liability laundering | **Serious but repairable** | Four of five routes blocked. Foreseeability open. Two sentences closes it. |
| AI-assisted reviewer correlation | **Already adequately answered** | Disclosed/undisclosed split, per-reviewer flags, exclusion from independence-based reliability claims. Better handled than in most assurance literature. |
| Affected-party burden | **Serious but repairable** | Burden is treated as harm and cohorted, but D-5 disables the accessibility conjunct. |

**Attacks I decline to strengthen.** "Excessive complexity" as a general charge is weak against a protocol that publishes a 60-second doorway and a reader-path selector. "High non-decisive rates" is answered. "Legal overreach" is mistaken. I will not inflate these to appear thorough.

**The attack a competent hostile reviewer would actually lead with:** *AF's independence architecture fails open on the three fields that matter most, and AF's own conclusion asserts the opposite.* That is D-1, and it is fixable in an hour.

## E.12 Originality and literature positioning

Assessed conservatively, separating what is established from what is new.

**Established, correctly adapted, not claimed as novel:** ordinal partial orders and outranking (Roy); non-compensatory MCDA; assurance and safety cases; program-evaluation meta-standards (Scriven, Stufflebeam); Goodhart-resistance and portfolio measurement; capability approaches; rights-based evaluation; robust decision-making under deep uncertainty (Lempert); model and system cards; algorithmic impact assessment. §2.3 and §2.4 position against these families explicitly and §2.5's blend selection rule is honest about what is borrowed.

**Genuinely distinctive architecture, three things, and I would foreground these:**

1. **The two-stage separation of eligibility from comparison, with hard subordination.** Assurance cases do not do this. MCDA does not do this. The rule that a newly established Stage A defect *suspends* Stage B rather than being traded against it, enforced through floor-linkage tiers at descriptor level, is not something I can point to elsewhere in this form.

2. **Symmetric perturbation replay with an evidence-gated admission step.** This is the most novel single mechanism in AF. It solves a real problem: how to let dissent affect a comparative finding without giving any single reviewer a silent veto. And it solves it symmetrically: unsupported proposals cannot demote dominance, and supported dissent cannot be suppressed by majority preference. Admission tests *supportability, not correctness*. I have not seen that distinction drawn this cleanly in the assurance or MCDA literature.

3. **The authority-specific verdict vector as an enforced object rather than a disclaimer.** Most frameworks disclaim authority in prose. AF makes the separation a data structure with per-component issuing authority, basis, scope, expiry, and appeal route, and then polices it with a formula.

**What is synthesis rather than novelty:** the C0–C5 set itself. §1.9.2 is right to publish the derivation order rather than claim independent discovery.

**Recommendation.** The abstract currently leads with the two-stage architecture and non-compensation. Perturbation replay is the more distinctive contribution and it is currently buried in §6.1. Foreground it. The strongest contribution of a paper is not always its advertised contribution.

---

# F. WORKBOOK AND INSTRUMENT AUDIT

Sixteen sheets, 1,757 formulas, 77 validation rules, all inspected.

## F.1 What is genuinely well built

State this first, because most of the workbook is good.

- **`Stage_A!AE4` is a correct completeness gate.** Requires all sixteen fields A:P non-blank before deriving anything. No blank row creates a substantive decision. No partially populated record fails open. Verified.
- **`Stage_A!AI4` is a correct recognition gate.** `AA+AB+AC+AD+AH = 6` or `UNRECOGNISED_VALUE`. Unrecognised input cannot become a pass.
- **`Stage_A!Q4` routing order is correct and non-compensatory.** Refusal → indeterminate → unpatchable → patchable → indeterminate-by-count → adequate. Unpatchable correctly controls over patchable, which correctly controls over adequacy.
- **`Status_Match` columns are genuinely useful.** Four distinct states (MATCH, MISMATCH, UNRECORDED, ORPHAN_RECORDED) implemented consistently on Stage_A, Independence, Burden_Log, and Study_Readiness. This is real reconciliation, not decoration.
- **`Verdict_Vector!M4` is an inference firewall in code.** Rejects approved/certified/safe/ethical/legitimate/compliant. Good.
- **`Burden_Log!P4` numeric guards genuinely fail closed.** Eight `ISNUMBER` tests, any failure → "Not feasible". Correct.
- **`Dashboard` separates burden cohorts.** B13 and B14 compute means separately for completed-feasible and infeasible-or-aborted, with D14 noting the latter "may reveal protocol burden harm". Excellent discipline.
- **`Dashboard` B15–B18 keep reliability layers separate** and label them "raw only", with D15 stating "Never blend with final or Stage B layers". This is exactly the discipline the brief demands and it is already implemented.
- **`Read_Me` correctly declines immutability.** B5, B6, B20. The instrument knows what it is not.

## F.2 Defect ledger

| ID | Sheet / Cell | Defect | Severity | Repair |
|---|---|---|---|---|
| W-1 | Independence!O4 | Negative blacklist on E/F/G; any unlisted string → "Adequate" | **P0** | Invert to positive whitelist; unknown → Indeterminate + vocabulary flag |
| W-2 | All sheets, 57 rules | `dataValidation` with no `type`, no `formula1` → inert; zero list validations exist | **P0** | Add `type="list"` sourced from a hidden `Vocabulary` sheet |
| W-3 | Dashboard!B8 | Counts dead v5.8 string "…with verified controls" | **P0** | Replace with "…, control-dependent"; source from Vocabulary |
| W-4 | Burden_Log!L4:L60 | Validated `decimal ≥ 0`; consumed by P4 as text "Yes" → accessibility gate never fires | **P0** | `type="list"` Yes/No; extend to M, N; guard P4 |
| W-5 | Reliability_Results!H, I | CI bounds constrained 0–1; negative coefficients unrecordable | **P0** | Change to −1 to 1; add H ≤ G ≤ I check |
| W-6 | Reliability_Results!C | `Decision_Layer` (categorical) validated as `decimal 0–1` | **P0** | `type="list"` with four canonical layers |
| W-7 | `xl/workbook.xml` | No `calcPr`, no `fullCalcOnLoad`, no `calcChain`; 1,391/1,757 formulas uncached | **P0** | Add `calcPr fullCalcOnLoad="1"`; recalc headless before hashing |
| W-8 | Stage_A!Q4 / AF4 | No derived path to `Out of scope`, though §5.5 and Anchors §1.4 declare it canonical. Recording it in R yields MISMATCH, inflating Dashboard!B7 integrity exceptions with a legitimate finding | P1 | Add an `Out_of_scope` administrative input routing through AE4 |
| W-9 | Stage_A!AG4 | Version literal `"AF v5.9"` hard-coded inside formula; silently invalidates at v6.0 | P1 | Move to Vocabulary sheet cell reference |
| W-10 | Reliability_Results!G | `Estimate` has no validation while its own CI does | P1 | Validate −1 to 1 |
| W-11 | Burden_Log!V4:V60 | `Reported_Burden_0_10` validated `whole ≥ 0` with **no upper bound**; feeds Dashboard means B13/B14 | P2 | `whole between 0 and 10` |
| W-12 | All 16 sheets | **No freeze panes anywhere.** Stage_A is 35 columns × 60 rows; Reliability is 29 columns | P2 | Freeze at B4 (or B5 where header row is 4) on every record sheet |
| W-13 | All 16 sheets | **No autofilter anywhere** | P2 | Add autofilter to header row on all record sheets |
| W-14 | Independence!R, S, T | Host_Interest_in_Outcome, Host_Precommitment, AI_Assistance_Policy are free text feeding no formula | P2 | Validate and route into O4 |
| W-15 | Read_Me!A14, A15 | Duplicated label "Workbook sequence" | P3 | Delete one |
| W-16 | Sheet conventions | Header row is 3 on 13 sheets, 4 on Rating_Deposits, Reliability_Results, Perturbation_Register | P3 | Standardise, or document in Read_Me |
| W-17 | Dashboard | Hard-coded ranges (`A4:A60`, `A5:A100`) silently undercount beyond row 60/100 | P2 | Use whole-column or dynamic ranges; add a row-overflow warning cell |
| W-18 | Workbook | No charts or drawings; Dashboard is text-only | P3 | Optional. A small-multiples exception panel would aid pilot administration |

**Final error scan.** Zero `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, `#N/A` in cached values across all 16 sheets. But this result is weak evidence: 79% of formulas have no cached value at all (W-7), so most cells could not surface an error. **Re-run the error scan after fixing W-7.** A clean scan on an uncached workbook is not a clean scan.

## F.3 Fail-open pathway summary

The brief asks specifically for false-green pathways. Three exist:

1. **Independence** (W-1), the serious one. Unlisted control values → "Adequate".
2. **Burden accessibility** (W-4), numeric L → access conjunct skipped → possible "Feasible".
3. **Dashboard KPI** (W-3), not false-green but false-blank; admissible records vanish rather than inflate. Directionally safer, still wrong.

Stage_A itself has **no fail-open pathway** that I could construct. That is the sheet that matters most and it holds.

---

# G. TABLE PRODUCTION AUDIT

## G.1 Scope limitation, stated plainly

The brief asks for border weights, cell padding, clipped text, row heights, repeated headers across page breaks, stranded captions, and orphaned rows. **None of this is assessable.** No genuine DOCX exists in the supplied set and no PDF was supplied. Table production defects live in the rendered artifact, not in the Markdown source.

I will not invent a defect ledger for rendering I cannot see. What follows is a **source-level table audit**, which is real and which I did perform, plus the acceptance criteria to apply once genuine output exists.

## G.2 Source-level findings

**Structural integrity: strong.** 45 tables (S1, 1, 1A, 1B, 2, 3, 3A, 4, 5, 5A, 5B, 6, 7, 8, 8A–8M, 9–25, 22A). No duplicate numbers. No gaps in the numeric range 1–25. Every table is referenced in body text. Every in-text table reference resolves to a caption. That is a clean result across 45 tables and it reflects real prior editorial work.

**Caption discipline: strong and distinctive.** Captions are declarative sentences carrying the epistemic claim, not labels. "Table 7. C0–C5 are functional safeguards, not mandates to imitate a computational or MathGov-shaped artifact set." "Table 24. Recursive application identifies protocol limits, revision triggers, and refusal conditions rather than self-certifying success." This is unusually good practice and should be preserved exactly.

**Source-level defects found:**

| ID | Table / location | Defect | Severity | Repair |
|---|---|---|---|---|
| T-1 | Table 8 (§6.1.2) | Floor tier `N/P` used for three dimensions; taxonomy defines only F, P, N | **P1** | Resolve to P; add membership check |
| T-2 | §6.1, lines 613 and 615 | Sentence duplicated verbatim with different dash characters | P2 | Delete line 615 |
| T-3 | Document-wide | `C0-C5` written with hyphen 19 times and en dash 13 times; `8A-8L` 2 vs 1; `CL0-CL6` hyphen only | P2 | Normalise to one form; hyphen is safer for search, replay, and token matching |
| T-4 | Table 5A / 5B ordering | Table 5B appears in source before Table 5A | P3 | Reorder or renumber |
| T-5 | Table ordering | Tables 8A–8L appear in Appendix F, after Tables 9–25 in the body | P3 | Acceptable given the compact-matrix design; note it in the List of Tables |

**On T-3 specifically.** This is not typographic pedantry in this document. AF makes canonical token discipline a first-class concern, ships a token map in Appendix G, and enforces exact-string matching in the instrument. A protocol that fails closed on "punctuation variants" in its own workbook should not carry two punctuation variants of its central identifier in its own master text.

## G.3 Table archetypes for v6.0

Currently the tables serve at least four distinct functions with no visual distinction between them. Three archetypes would carry the semantic load without flattening it:

1. **Constitutional / definitional**, Tables 5, 5B, 7, 8M, Appendix G. Heaviest rule, header emphasis, no zebra striping. These are controlling.
2. **Analytical / comparative**, Tables 8, 9, 22, 23. Lighter rule, zebra striping, right-aligned numerics.
3. **Operational / record**, Tables 16, 24, S1, worked-scenario tables. Lightest rule, compact padding.

Do not unify beyond three. The distinction between "this table controls" and "this table informs" is exactly the distinction AF cares about and it should be visible at a glance.

## G.4 Acceptance criteria for the rendered build

Apply these once genuine DOCX and PDF exist:

- Complete outer border on every table, bottom border specifically verified at 100% and 150% zoom
- Header row repeats on every page break (`w:tblHeader` on the header row)
- No row splits across pages (`w:cantSplit`)
- Caption bound to table (`keepNext` on the caption paragraph)
- Minimum 0.08" cell padding on all four sides; no text touching any border
- Consistent line weight within archetype
- Numerics right-aligned; text left-aligned; no centre-aligned body text
- No table wider than the text block
- Every table legible in grayscale

---

# H. GRAPHICS AUDIT

## H.1 Scope limitation

Eleven figures are referenced. **Zero were supplied.** I can audit specification, placement, caption discipline, and epistemic framing. I cannot audit label size, arrow ambiguity, hierarchy accuracy, grayscale survival, resolution, or visual consistency. Any claim I made about those would be fabrication.

## H.2 What the specification shows

| # | File | Caption epistemic framing | Placement | Assessment |
|---|---|---|---|---|
| 1 | figure0_af_in_60_seconds.png | "moves from a bounded claim to a challengeable finding without converting evaluation into authorization" | Front matter | Placement correct |
| 2 | figure0b_verdict_boundary.png | "AF eligibility is not universal approval" | Front matter | Placement correct; this is the highest-value figure in the set |
| 3 | figure2.png | §1 | — | Cannot assess |
| 4 | figure_cl_ladder.png | CL0–CL6 | §1.9.3 | Placement correct |
| 5 | figure1.png | §1.4 protocol at a glance | — | Cannot assess |
| 6 | figure_stage_a_gates.png | "non-compensatory: a material defect cannot be offset by strength elsewhere, and incomplete or unrecognised evidence fails closed" | §5 opening | Placement correct |
| 7 | figure3.png | "Profile dominance is a partial order. Incomparability is a legitimate finding, not a failure to force a winner." | §6 opening | Placement correct |
| 8 | figure_perturbation_replay.png | "unsupported proposals cannot silently veto dominance, while supported dissent cannot be suppressed" | §6.1 | Placement correct; illustrates the most novel mechanism |
| 9 | figure_profiles.png | §6 | — | Cannot assess |
| 10 | figure_independence_architecture.png | §7 | — | Placement correct |
| 11 | figure_validation_ladder.png | §11 | — | Placement correct |

**Caption quality is strong.** Every caption I can read states an epistemic boundary rather than describing the picture. Figures 1, 2, 6, 7, and 8 all carry the boundary claim into the caption. That is the right practice and it should be preserved.

## H.3 Proposed additions

The brief lists ten candidate graphics (A–J). Assessed against what already exists rather than added reflexively.

| Graphic | Existing/New | Purpose | Placement | Value | Recommendation |
|---|---|---|---|---|---|
| A. AF in 60 Seconds | **Exists** (Fig 1) | Doorway | Front matter | Essential | Keep. Do not duplicate |
| B. Stage A non-compensatory gates | **Exists** (Fig 6) | Show gates not scores | §5 opening | Essential | Keep |
| C. Verdict boundary | **Exists** (Fig 2) | Block the five prohibited slides | Front matter | Essential | Keep |
| D. Stage B partial order | **Exists** (Fig 7) | Dominance/incomparable/non-decisive/refusal | §6 opening | Essential | Keep. Verify all four outcomes appear, not just two |
| E. Evidence-to-finding trace | **New** | Evidence → criterion → finding → dissent → adjudication → appeal → bounded public status | §7 opening | **High-value** | **Add.** This is the single missing figure. §7 is 2,200 words of process with no visual spine, and this chain is what an external reviewer most needs to hold in mind |
| F. Independence architecture | **Exists** (Fig 10) | Sponsor/host/reviewer/custody/publication firewall | §7.2 | Essential | Keep. Update after D-1 repair so it shows whitelist gating |
| G. Validation ladder | **Exists** (Fig 11) | Spec closure → Phase 0 → pilot → replication | §11 | Essential | Keep |
| H. Constitutional legitimacy ladder | **Exists** (Fig 4) | CL0–CL6 | §1.9.3 | Essential | Keep. Mark current position at CL1 explicitly on the figure |
| I. Proportional review profiles | **New** | AF-Lite → Standard → High-Consequence, upward-only escalation | §7.1 | **High-value** | **Add.** §7.1's upward-only rule and no-downward-waiver rule are exactly the kind of asymmetry a diagram conveys instantly and prose conveys poorly |
| J. What an AF finding does NOT mean | **Exists** (Fig 2) | — | — | — | Already served by C. Do not add a second |

**Two additions, not ten.** E and I. Everything else already exists or would duplicate. Adding graphics that duplicate existing tables would violate the brief's own instruction and would add production burden for no comprehension gain.

**One deletion to consider.** Figures 3, 5, and 9 (`figure2.png`, `figure1.png`, `figure_profiles.png`) have generic filenames and I cannot assess them. If any duplicates a table without adding information, cut it. Rename all figure files to semantic names as figures 1, 2, 6, 8, 10, and 11 already are, generic `figure1.png` / `figure2.png` / `figure3.png` alongside semantic names is itself a small provenance defect.

---

# I. INFORMATION-ARCHITECTURE REDESIGN

## I.1 What to preserve

The front matter is already right and I recommend almost no change to it. Idea before machinery, boundary before content, doorway before depth, release records in appendices. Preserve exactly:

1. Title block with author, ORCID, affiliation, current status line
2. AF in 60 Seconds + Figure 1 + reader path selector
3. What an AF Finding Does Not Mean + Figure 2
4. Abstract (501 words, six labelled moves)
5. Current Status at a Glance (Table S1)
6. TOC + List of Tables + List of Figures
7. Reader Guide: Key Terms and Canonical Tokens

That sequence is better than most published protocols and changing it would be change for its own sake.

## I.2 The one structural problem

Section weight is inverted against reader need.

| Section | Words | % of body | Reader need |
|---|---:|---:|---|
| 1. Introduction | 4,570 | 15.6% | Framing |
| 8. Worked Scenario | 4,338 | 14.8% | Illustration |
| 11. Validation | 3,183 | 10.8% | Status |
| 6. Stage B | 2,322 | 7.9% | **Mechanism** |
| 7. Administration | 2,200 | 7.5% | **Mechanism** |
| 2. Related Work | 2,056 | 7.0% | Positioning |
| 3. Definitions | 1,837 | 6.3% | **Mechanism** |
| 5. Stage A | 1,620 | 5.5% | **Mechanism** |
| 10. Formal Protocol | 602 | 2.1% | **Mechanism** |

Framing and illustration together are 30.4%. The two controlling mechanism sections, Stage A and the Formal Protocol, are 7.6% combined.

## I.3 Three moves, no deletions

**Move 1, split Section 1.** Currently 4,570 words spanning problem statement, protocol overview, evidence status, thesis, research questions, non-claims, constitutional-class argument, genealogy, legitimacy, affiliation safeguards, status boundary, and protocol family precedence. That is three sections wearing one number.

| Current | Proposed | Reason |
|---|---|---|
| §1.1–1.8 | **§1. Introduction** (~2,000 words) | Problem, contribution, thesis, research questions, non-claims. Stops where framing stops |
| §1.9–1.10 | **§2. The Constitutional Class and Its Legitimacy** (~1,400 words) | This is the protocol's central normative claim per §1.9.1. It deserves its own number, not a subsection |
| §1.11–1.12 | Fold into new §3 Definitions, and Appendix | Status boundary belongs with definitions; protocol family precedence belongs with the artifact inventory |

**Move 2, relocate the bulk of Section 8.** Keep §8.1 (scenario specification), §8.4 (worked Stage A outcome), §8.8 (incomparability demonstration), and §8.9 (dominance proof) in the body, roughly 1,500 words. Move §8.2 mini-dataset, §8.3 Decision Note excerpt, §8.5 defect-code taxonomy, §8.6 adversarial probe catalog, §8.7 Stage B preview, and §8.10 populated perturbation case to a new **Appendix H: Complete Worked Scenario**, roughly 2,800 words.

Nothing is lost. The reader who wants the full run follows one cross-reference. The reader who wants the mechanism is not made to walk through 4,338 words of illustration first.

**Move 3, promote Section 10.** The Formal Protocol is 602 words and sits after the worked scenario and the candidate-diversity discussion. It should sit immediately after Stage B, because it is the formal statement of what Stages A and B just described informally. Renumber as **§8. Formal Protocol**, directly after Stage B and Administration.

## I.4 Proposed complete front-to-back structure

```
FRONT MATTER
  Title page
  AF in 60 Seconds                       [Fig 1] [reader paths]
  What an AF Finding Does Not Mean       [Fig 2]
  Abstract
  Current Status at a Glance             [Table S1]
  Table of Contents (clickable, depth 2)
  List of Tables
  List of Figures
  Reader Guide: Key Terms and Canonical Tokens

BODY
  1. Introduction                                    ~2,000
  2. The Constitutional Class and Its Legitimacy     ~1,400   [Fig 4 CL ladder]
  3. Related Work and Positioning                    ~2,050
  4. Definitions, Scope, and Role Boundaries         ~1,950
  5. Minimal Normative Kernel and Coverage             ~510
  6. Stage A: Minimum Eligibility Criteria           ~1,620   [Fig 6 gates]
  7. Stage B: Comparative Profile Evaluation         ~2,320   [Fig 7, Fig 8]
  8. Formal Protocol                                   ~600
  9. Administration, Independence, and Accountability ~2,200  [Fig 10, NEW Fig E, NEW Fig I]
 10. Worked Scenario: Core Demonstration             ~1,500
 11. Candidate Diversity, Affiliation, Challenge Scope ~860
 12. Validation Program and Recursive Self-Audit     ~3,180   [Fig 11]
 13. Limitations and Threats to Validity              ~600    [NEW, see below]
 14. Conclusion                                        ~270

BACK MATTER
  References
  Appendix A. Declarations and Release Record
  Appendix B. Version History and Changelog
  Appendix C. Independent Audit Findings and Correction Closure
  Appendix D. Artifact Inventory, Manifests, and Schema Map
  Appendix E. Statistical Derivations and Simulation Provenance
  Appendix F. Stage B Ordered Anchors (Controlling)
  Appendix G. Canonical Token Map and Version Migration
  Appendix H. Complete Worked Scenario                [NEW — from §8]
  Appendix I. How to Verify This Package              [NEW — see D-3]
```

**On the new §13 Limitations.** Currently limitations are distributed across §1.8 non-claims, §1.11 status boundary, §11.4 yield risk, §11.5 self-audit, §11.6 programme risks, and the conclusion. Each placement is individually defensible. Collectively it means no reader can find "what is wrong with AF" in one place. A skeptical reviewer, a funder, and an affected-party representative all want exactly that page. Consolidating it costs 600 words of cross-referencing and buys substantial credibility. It is also the section AF's own C0 would expect.

## I.5 Relocation table

| Content | Current location | Proposed location | Reason |
|---|---|---|---|
| Constitutional class argument | §1.9 | New §2 | Central normative claim; too important to be a subsection |
| Status boundary | §1.11 | §4 Definitions | Belongs with scope definitions |
| Protocol family precedence | §1.12 | Appendix D | Artifact inventory material |
| Mini-dataset, Decision Note, defect taxonomy, probe catalog, Stage B preview, perturbation case | §8.2–8.3, 8.5–8.7, 8.10 | Appendix H | Reference material, not argument |
| Formal Protocol | §10 | §8, after Stage B | Formalises what precedes it |
| Distributed limitations | §1.8, 1.11, 11.4, 11.5, 11.6, §12 | Consolidated §13 (cross-referenced, not moved) | Findability |
| Simulation provenance | Appendix E | Keep, add script to package | Already correctly placed |

---

# J. PROPOSED MASTER TABLE OF CONTENTS

Depth 2. Deeper than this is navigation clutter; shallower loses the Stage A/B substructure a returning reader needs.

```
AF in 60 Seconds
What an AF Finding Does Not Mean
Abstract
Current Status at a Glance
Reader Guide: Key Terms and Canonical Tokens

1. Introduction
   1.1 Steering without instrumentation
   1.2 The missing standard
   1.3 Candidate neutrality and accountable sponsorship
   1.4 Protocol at a glance
   1.5 Core thesis and research questions
   1.6 Non-claims and scope boundaries

2. The Constitutional Class and Its Legitimacy
   2.1 The constitutional-class boundary as central normative claim
   2.2 Genealogy and derivation order of C0-C5
   2.3 Constitutional legitimacy, plural derivation, and stewardship
   2.4 Functional criteria and the author-affiliation safeguard

3. Related Work and Positioning
   3.1 Flourishing is not a settled construct
   3.2 Flourishing as a constrained vector
   3.3 Major traditions, blind spots, and the added function
   3.4 Positioning against meta-evaluation traditions
   3.5 Blend selection rule

4. Definitions, Scope, and Role Boundaries
   4.1 Flourishing as floors, fields, horizons, and integrity
   4.2 Framework
   4.3 Traceability, reproducibility, and replay
   4.4 Eligibility, selectability, and authorization
   4.5 The authority-specific verdict vector
   4.6 Refusal under underdetermination
   4.7 Current status boundary

5. Minimal Normative Kernel and Flourishing Coverage
   5.1 Functional coverage before vocabulary
   5.2 Portfolio-based, distribution-aware measurement

6. Stage A: Minimum Eligibility Criteria
   6.1 Criterion states and decision architecture
   6.2 Evidence-sensitive findings
   6.3 Rights-floor routing and principled non-equivalence
   6.4 Emergency-provisional action is not admissibility
   6.5 Disagreement default and the no-silent-veto rule

7. Stage B: Comparative Profile Evaluation
   7.1 Ordered rubric profile and category descriptors
   7.2 Perturbation admission and symmetric replay
   7.3 Indicator-level comparison
   7.4 Tail-risk method adequacy under deep uncertainty
   7.5 Context-specific interpretation
   7.6 Practical uses and limits of the profile

8. Formal Protocol

9. Administration, Independence, and Public Accountability
   9.1 Proportional profiles and upward-only escalation
   9.2 Adjudicator and host independence
   9.3 Disagreement defaults and reliability preregistration
   9.4 Burden accounting and the capacity gate
   9.5 Affected-party standing
   9.6 Differential evidence pathways and resource equity

10. Worked Scenario: Core Demonstration
   10.1 Scenario specification
   10.2 Worked Stage A outcome
   10.3 Worked incomparability demonstration
   10.4 Worked dominance and perturbation survival

11. Candidate Diversity, Affiliation, and Challenge Scope
   11.1 Non-author candidate neutrality stress test
   11.2 Architecture-diversity calibration suite
   11.3 Adoption pathway and selection-bias record

12. Validation Program and Recursive Self-Audit
   12.1 Current maturity
   12.2 Validation matrix and study tiers
   12.3 External validation, audit theatre, and decision value
   12.4 Structural yield and perturbation fragility
   12.5 C0-C5 self-audit
   12.6 Stewardship, amendment, succession, capture resistance

13. Limitations and Threats to Validity

14. Conclusion

References

Appendix A. Declarations and Release Record
Appendix B. Version History and Changelog
Appendix C. Independent Audit Findings and Correction Closure
Appendix D. Artifact Inventory, Manifests, and Schema Map
Appendix E. Statistical Derivations and Simulation Provenance
Appendix F. Stage B Ordered Anchors (Controlling)
Appendix G. Canonical Token Map and Version Migration
Appendix H. Complete Worked Scenario
Appendix I. How to Verify This Package

List of Tables
List of Figures
```

**Build requirements.** Real `TOC \o "1-2" \h \z \u` field. Heading 1 and Heading 2 styles applied consistently. Bookmarks generated for every heading. `List of Tables` from Caption style with `\c "Table"`. `List of Figures` with `\c "Figure"`. PDF export with `Create bookmarks using: Headings` and `Document structure tags for accessibility` both enabled. Headers carrying short title left and section right; footers carrying page X of Y and version identifier.

---

# K. SIMPLIFICATION OPPORTUNITIES

Each stated as: current complexity → proposed simplification → information preserved.

**K-1. Section 1 carries twelve independent jobs.**
→ Split into §1 Introduction and §2 The Constitutional Class (§I.3, Move 1).
→ *Preserved: all twelve. Only the boundary between framing and normative argument is made visible.*

**K-2. Limitations are distributed across six locations.**
→ Consolidate into §13 with cross-references back to the detailed treatments.
→ *Preserved: every existing limitation, in its original detailed location. §13 is an index, not a replacement.*

**K-3. Two floor-tier notations coexist (F/P/N and N/P).**
→ Resolve to three declared tiers.
→ *Preserved: all routing distinctions. The N/P cases become P, which is what they appear to mean.*

**K-4. AF-Lite is named but under-specified relative to AF-Standard.**
→ Add one table to §9.1: for each of C0–C5, what AF-Lite minimally requires versus AF-Standard, with the explicit statement that *protection requirements are identical and only administrative burden scales*.
→ *Preserved: everything. This makes visible a rule §7.1 already states, and it directly answers the brief's question about whether a small institution can realistically use AF.*

**K-5. §6.1 runs eight consecutive bold-lead rule blocks before the reader reaches an example.**
→ Add a two-sentence roadmap at §6.1 opening naming the five rules in order.
→ *Preserved: all eight rules. Adds ~40 words, removes the "wall of rules" effect.*

**K-6. Acronym density peaks in §6 and §11.** AF-SB12-v5.6, AF-SB-RELATION-v5.9, C3-D07, CL0–CL6, L0–L6, F/P/N, C0–C5, C2-D05, H-Y1 to H-Y4.
→ The Reader Guide already exists. Add a one-line acronym strip in the running footer of §6 and §11 only, or a boxed mini-glossary at each section opening.
→ *Preserved: all identifiers. Reduces the cost of entering mid-document, which is exactly how this document will be read.*

**K-7. Table 8 (compact matrix) and Appendix F (full descriptors) restate the same 60 descriptors at two granularities.**
→ **Keep both.** This is correct progressive disclosure and the brief's own principle supports it. Add one line under Table 8: "Appendix F descriptors control; this matrix is a reader aid." §6.1 already says this in prose; putting it under the table is where the reader needs it.
→ *Preserved: everything. This is a case where apparent duplication is doing real work and should not be simplified away.*

**K-8. §11.4's four models are presented as prose plus equations plus Table 23.**
→ Lead with Table 23, then the equations as derivation, then the interpretation. Currently the reader assembles the comparison from three passes.
→ *Preserved: all four models, all equations, all caveats.*

---

# L. PAGE-BY-PAGE VISUAL QA LEDGER

**Not performed. Cannot be performed from the supplied artifacts.**

The brief instructs: "Render the complete master DOCX and PDF. Inspect every page visually. Do not infer visual quality from the source XML. Actually inspect rendered pages. Provide exact page numbers for every defect."

I cannot comply, and I will not simulate compliance. The reasons are byte-verifiable:

1. No genuine DOCX exists in the supplied set (D-3). All eleven `.docx` files are Markdown.
2. No PDF was supplied.
3. All eleven figure PNGs are absent, so even a rendered build from the Markdown source would show eleven broken image placeholders and would not represent the real document.

Producing a ledger with invented page numbers would be the single most damaging thing this audit could do, because it would be exactly the kind of false attestation AF exists to detect. A fabricated visual QA ledger is audit theatre.

**What to do instead.** Once the genuine build exists, run this checklist and record actual page numbers:

| Check | Pass criterion |
|---|---|
| Clipped or overlapping text | None at 100% and 150% zoom |
| Table bottom borders | Uninterrupted on every table |
| Header row repetition | Every table spanning a page break repeats its header |
| Row splitting | No row split across pages |
| Caption stranding | No caption separated from its table or figure |
| Heading position | No Heading 1 or 2 within 3 lines of page bottom |
| Widows and orphans | None |
| Figure resolution | ≥300 dpi effective at placed size |
| Figure consistency | Uniform width within each size class |
| Grayscale | Every figure legible without colour |
| Margins | Uniform; no drift |
| Footnote density | No page more than 25% footnote |
| TOC | Every entry clickable; every target correct |
| Bookmarks | Present for all Heading 1 and 2 in PDF |
| Accessibility | Tagged PDF; alt text on all 11 figures |

**Acceptance test for the build itself, before visual QA begins:** magic bytes `50 4b 03 04`; `unzip -t` clean; python-docx opens; `document.xml` contains a `TOC` field; `settings.xml` contains `updateFields`; all 11 image parts present in `word/media/`; PDF opens with a populated bookmark tree.

---

# M. INDEPENDENT VALIDATION ROADMAP

AF's own laddering (§11.2A, Table 22) is correct and I am not replacing it. These are the sequencing corrections.

## M.0 Gate before Phase 0 — instrument repair

**Non-negotiable and currently missing from the roadmap.** D-6 means the instrument cannot record a negative reliability coefficient. Phase 0's primary output is inter-reviewer agreement. Running Phase 0 on the current instrument risks a study that structurally cannot record its own most important adverse result.

Sequence: fix D-1 through D-7 → re-run the workbook error scan on a *cached* workbook → hostile-case replay against the repaired instrument → only then open Phase 0.

## M.1 Phase 0 — exploratory calibration

**On feasibility.** Phase 0 as specified requires an independent host, a trained reviewer pool, and a frozen calibrated twenty-case library. §11.6 already flags that reviewer recruitment may fail. Twenty cases at AF-Standard, two reviewers per case, plus adjudication, is a substantial commitment for an unfunded exploratory study.

**Reduction that preserves inferential usefulness.** Cut to **twelve cases**, chosen to span four architecture families (computational, deliberative, legal/charter, community/customary) at three difficulty levels. Twelve cases with two independent reviewers gives 24 ratings per criterion, which is thin for a stable AC1 point estimate but adequate for the questions Phase 0 actually asks: can reviewers interpret C0–C5 consistently, where do anchors overlap, what does administration cost, and does the instrument fail closed under real use. Those are calibration questions, not power questions, and §11.4 already states Phase 0 "is not powered for general yield claims".

Do **not** cut architecture-family coverage to save cases. Family coverage is the one thing twelve cases can genuinely inform, because architecture-family bias is a systematic effect rather than a variance question.

**Reliability reporting, hold the existing line exactly.** Separate by Stage A criterion, Stage A final decision, Stage B dimension, and Stage B final relation. Never blend. `Dashboard!B15–B18` already implement this correctly and it is one of the best features of the instrument. At Phase 0 sample sizes, report **raw agreement with exact intervals only**. Do not report AC1 or alpha from twelve cases; the intervals will be uninformative and the point estimates will be over-read.

**Preregister the wealth-gradient diagnostic** from §E.7 as a named Phase 0 output.

## M.2 Confirmatory pilot

Powered for Stage A criterion-level agreement. Preregistered Stage A and Stage B outcome bands. Preregistered threshold for "practically uninformative yield". H-Y1 through H-Y4 tested. Burden cohorts reported separately, with abandonment and infeasibility as first-class outcomes rather than missing data.

## M.3 Independent replication

A second host, no shared reviewers, no author involvement in administration, replaying a frozen case set. **This is the credibility pivot**, and it is worth more than any number of additional internal artifacts. One independently replayed frozen run establishes more than ten synthetic ones.

## M.4 External validation and bounded deployment evidence

Only after M.3. Decision value, capture resistance, and downstream effects. Nothing here should be attempted earlier and AF correctly does not attempt it.

## M.5 What would falsify AF

Stated so it is testable, drawn from AF's own commitments:

- Stage A criterion agreement persistently at or below chance after training and calibration → C3 review of anchors
- Architecture-family effects on Stage A outcome that survive adjustment for substantive protection → C1/C3 review, potential retirement of the comparison claim
- Near-zero eligible comparison sets across repeated administrations → C3-D07 and Stage B retention review
- Burden making AF-Lite unusable for institutions below a defined resource threshold → C1 equity defect
- A candidate found Stage-A admissible that subsequently produces the class of harm C0–C5 was designed to detect → C4 review and public correction

---

# N. PUBLICATION STRATEGY

## N.1 Do not compress the master into journal length

The master is 30,928 words and it should stay that way. Its purpose is correctness, completeness, navigability, and auditability, not journal compression. Forcing it to 8,000 words would destroy the auditability that is its reason for existing.

## N.2 Recommended structure

| Artifact | Length | Venue | Purpose |
|---|---|---|---|
| **Master Reference Edition v6.0** | ~31,000 words + companions + instrument | Zenodo, versioned, DOI, full package with manifests | Controlling specification. Cite by version and ZIP SHA-256 |
| **Methods article** | 4,701 words (exists) | *AI and Ethics*, *Minds and Machines*, or *Philosophy & Technology* | Two-stage architecture, non-compensation, perturbation replay |
| **Statistical note** | ~3,000 words | Methods venue or arXiv | Structural yield under range restriction and correlation. This is publishable on its own and the mathematics is already verified |
| **Legitimacy paper** | ~6,000 words | *AI & Society* or a governance venue | CL0–CL6, constitutional class, plural derivation. Currently AF's thinnest companion and its most contested claim |
| **Phase 0 registered report** | Protocol only | A venue accepting registered reports | Preregistration is the strongest available answer to the circularity attack |

## N.3 Sequencing

1. Fix D-1 to D-7 and build genuine artifacts.
2. Zenodo deposit of the complete v6.0 package with a DOI. **Do this before any journal submission.** It converts every "the package contains…" claim from an attestation into a citable, verifiable object, and it closes the single largest credibility gap this audit found.
3. Then circulate the methods article.
4. The statistical note can go out in parallel; it is independent of the artifact repairs and the mathematics already reproduces.

**On the DOI specifically.** Appendix A currently says "A persistent repository or preprint identifier is not yet assigned; the package contains deposit-ready metadata but does not claim a DOI." That is honest. It is also the thing most easily fixed, and fixing it removes the awkwardness of a protocol about verifiability asking readers to verify against a ZIP hash they cannot obtain independently.

---

# O. FINAL DISPOSITION

## **Material revision.**

Not minor revision, because seven P0 defects exist and three of them (D-1, D-5, D-6) mean the instrument does not do what the master document says it does, on independence, accessibility, and adverse-result recording respectively.

Not major redesign, because the conceptual architecture is sound and survived every attack I could construct. C0–C5 are genuinely non-compensatory in code as well as prose. Stage B is genuinely subordinate. Refusal, indeterminacy, and incomparability are genuinely reachable. The mathematics is correct and independently reproduces. The rights architecture is careful, the emergency-stacking block is strong, and the verdict-boundary discipline is held consistently across 30,928 words. Table and figure numbering is clean. The three-layer reading structure already exists. **The thinking does not need redesigning.**

The gap is between specification and delivery, and it is narrower than it looks. Of the seven P0 defects, five are single-formula or single-attribute repairs (D-1, D-4, D-5, D-6, D-7). One is a build-pipeline correction (D-3). One is a systematic but mechanical addition (D-2).

**The governing observation.** AF's central claim is that claims should resolve to inspectable evidence. Three of its own claims currently do not: "workbook independence and burden logic use positive whitelists" (they do not), "the master edition is navigable through a clickable contents system" (no navigable artifact exists), and Appendix C's rejection of the container finding (which recurred). None of these is dishonesty; all are the ordinary drift between a build pipeline and a document. But they are precisely the drift AF exists to catch, and a reviewer who catches AF failing its own C0 will discount everything else AF says.

Fix those three and AF's credibility position changes qualitatively, because the framework will then demonstrate the property it advocates rather than assert it.

**Recommended v6.0 sequence:**

1. Repair D-1 through D-7. Estimated effort: one focused engineering day.
2. Re-run the workbook error scan on a cached workbook. The current clean scan is not evidence.
3. Rewrite Appendix C to accept the container finding as a distribution-control defect with a named corrective control.
4. Apply the §I.3 structural moves. Nothing is deleted.
5. Add §13 Limitations and Appendix I How to Verify This Package.
6. Add the two new figures (evidence-to-finding trace; proportional review profiles).
7. Resolve the `N/P` tier, the duplicated sentence, and the dash inconsistency.
8. Resolve the ~30 uncited references and bump all v5_8 integrity references.
9. Build genuine OOXML with real TOC and bookmarks. Verify magic bytes. Hash last.
10. Run the §L visual QA on real rendered pages and record actual page numbers.
11. Zenodo deposit with DOI.
12. Then open Phase 0.

Steps 1 to 3 are the ones that matter most. Everything after step 3 is improvement. Steps 1 to 3 are repair of claims that are currently unearned.

---

## Appendix: Verification commands used in this audit

Reproducible by any reader with the same files.

```bash
# Container check — must return 50 4b 03 04 for genuine OOXML
head -c 4 FILE | od -An -tx1
file -b FILE
unzip -t FILE

# Pair divergence under a single version label
sha256sum BASE.docx BASE.md

# Workbook: calcPr and cached-value coverage
python -c "import zipfile,re; print(re.search(r'<calcPr[^>]*/?>',
  zipfile.ZipFile('WB.xlsx').read('xl/workbook.xml').decode()))"

# Workbook: inert data validation detection
python -c "import zipfile,re; x=zipfile.ZipFile('WB.xlsx').read('xl/worksheets/sheet4.xml').decode();
  print([n for n in re.findall(r'<x:dataValidation\b[^>]*/>',x) if 'type=' not in n])"

# Two-pass formula vs cached inspection
openpyxl.load_workbook(P, data_only=False)   # formula text
openpyxl.load_workbook(P, data_only=True)    # cached values
```

**Statistical reproduction:** exact closed forms re-derived from P(a≥b) = (k+1)/2k and P(a=b) = 1/k; Gaussian copula re-implemented with Cholesky decomposition, standard-normal quintile cuts, 500,000 draws, independent profiles. All six exact values matched to the stated digits; both correlated values reproduced within Monte Carlo error.

---

*End of audit. Findings are labelled observation, evidence, inference, or speculation throughout. Where a hypothesis was tested and rejected, the rejection is recorded rather than removed.*
