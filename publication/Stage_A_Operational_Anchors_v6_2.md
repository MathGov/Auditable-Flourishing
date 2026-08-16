# Auditable Flourishing v6.2 Stage A Operational Anchors

## Status and role

This is the binding operational-anchor companion for Stage A. It states minimum records, criterion states, adequacy anchors, material-defect anchors, boundary cases, disconfirming evidence, floor-linked category re-entry, canonical tokens, and fail-closed implementation rules. It does not replace competent judgment, applicable law, affected-party input, or independent administration.

## 1. Common decision architecture

### 1.1 Criterion states

Each criterion receives exactly one controlled state; free text belongs in rationale, never the state field:

- `adequate_for_scope`;
- `adequate_control_dependent`;
- `indeterminate`;
- `material_defect_patchable`;
- `material_defect_unpatchable_for_stated_claim`;
- `not_reviewed`.

Blank fields are not criterion states. A completely blank record remains blank. A partially populated record is incomplete and cannot produce admissibility. Only six exact recognised adequate states can produce an admissible status. Any free text, legacy label, punctuation variant, trailing-space variant, or other unrecognised value routes to `protocol_refusal_to_evaluate`; absence of a recognised defect is never treated as positive adequacy. Invalid administration, infeasible burden, unmanaged conflict, absent required access, or missing mandatory criteria produces `protocol_refusal_to_evaluate`. Insufficient substantive evidence produces `indeterminate_insufficient_evidence`.

### 1.2 Materiality test

A gap is material when credible correction could change Stage A eligibility, protected-floor routing, Stage B applicability or relation, refusal, authority, public claims, burden or access feasibility, or downstream rights exposure. The record states evidence, causal mechanism, decision effect, floor implication, uncertainty, and a falsifiable patch or clarification condition.

### 1.3 Root-cause non-duplication

One causal defect receives one root-cause ID and one primary criterion owner. Secondary effects are cross-referenced but cannot create duplicate penalties. A second primary finding requires a distinct causal mechanism or independently decision-relevant defect.

### 1.4 Canonical public statuses

| Human-readable status | Canonical token | Meaning boundary |
| --- | --- | --- |
| Stage-A admissible - scoped | `stage_a_admissible_scoped` | Six recognised criterion states are adequate for the exact declared scope. |
| Stage-A admissible - scoped, control-dependent | `stage_a_admissible_scoped_control_dependent` | Eligibility depends on named, verified, monitored, time-bounded controls. |
| Stage-A non-admissible - patchable | `stage_a_non_admissible_patchable` | At least one material defect may be repaired, narrowed, or resubmitted. |
| Stage-A non-admissible - unpatchable for stated claim | `stage_a_non_admissible_unpatchable_for_stated_claim` | The stated claim or authority cannot survive the established defect. |
| Indeterminate - insufficient evidence | `indeterminate_insufficient_evidence` | The record supports neither adequacy nor a material defect safely. |
| Protocol refusal to evaluate | `protocol_refusal_to_evaluate` | Administration, competence, capacity, access, independence, vocabulary, version control, or another prerequisite prevents a valid review. |
| Out of scope | `out_of_scope` | The request lies outside the protocol, competence, or declared challenge. |
| Withdrawn | `withdrawn` | The entrant or host ended the review; no conformity inference follows. |
| Not reviewed | `not_reviewed` | No valid review occurred; no inference is permitted. |

Every public status binds candidate ID and version, role, population, domain, jurisdiction or community, evidence cut-off, host, profile, protocol version, issue date, expiry or requalification, conditions, dissent, and appeal. Bare Pass, Fail, Approved, Certified, Safe, Ethical, Legitimate, Valid, or Compliant labels are prohibited.

## 2. C0 Inspectability

| Anchor | Operational requirement |
| --- | --- |
| Minimum record | normative core; authority and override path; decision rule; dependencies; discretion; control channels; scope and version; confidentiality boundary |
| Adequate for scope | a competent external reviewer can reconstruct what materially determines a decision and who can alter or override it |
| Adequate - control-dependent | restricted material is independently inspected under verified access, conflict, logging, publication, and expiry controls |
| Patchable defect | a missing weight, rule, authority, dependency, override, or proprietary element could change outcomes but can be disclosed, independently reviewed, or scoped out |
| Unpatchable for stated claim | the claimed authority depends on a permanently unreviewable material core or uncontrolled hidden authority |
| Indeterminate | evidence cannot establish whether undisclosed elements are material |
| Boundary cases | trade secrets, classified detail, tacit community practice, distributed authority, adaptive systems |
| Disconfirming evidence | materially different evidence permits reliable reconstruction without the expected artifact |

## 3. C1 Rights protection

| Anchor | Operational requirement |
| --- | --- |
| Minimum record | protected floors; affected groups; applicable law and principled equivalents; non-compensatory routing; remedy; limitation or emergency process; non-refoulement where relevant; monitoring and redress |
| Adequate for scope | material rights risks are explicit, outside ordinary welfare aggregation, enforceable, contestable, and paired with usable remedy |
| Adequate - control-dependent | a bounded limitation is subject to competent separate authority, necessity, least-restrictive alternatives, time limit, review, redress, anti-stacking, and requalification |
| Patchable defect | thin floor, missing remedy, ambiguous affected group, or review gap can be repaired without abandoning the stated role |
| Unpatchable for stated claim | the claim requires ordinary compensation of severe rights injury, permanent unreviewable exception, transfer to serious prohibited harm, or elimination of standing |
| Indeterminate | rights, affected groups, jurisdiction, or practical remedy cannot be established |
| Boundary cases | conflicting rights, emergency stabilization, customary governance, minors, disability, non-human moral patients, transboundary effects |
| Disconfirming evidence | a rival architecture provides functionally equal or stronger protection through a different form |

## 4. C2 Auditability

| Anchor | Operational requirement |
| --- | --- |
| Minimum record | inputs, evidence, assumptions, transformations where applicable, discretion, reasons, authority, versions, outcome, challenge, correction, rating-deposit and release lineage |
| Adequate for scope | a competent reviewer can reconstruct why the result occurred and identify material evidence and authority |
| Adequate - control-dependent | sensitive evidence is replayable by an independent authorized party with logged access and a public bounded account |
| Patchable defect | logs lack reasons, evidence, version, authority, scenario, or deposit provenance but the lineage can be supplied |
| Unpatchable for stated claim | the material basis is intentionally ephemeral or inaccessible and no equivalent challenge path exists |
| Indeterminate | record completeness or correspondence to actual operation is uncertain |
| Boundary cases | oral deliberation, privacy-preserving logs, evolving models, distributed institutions, emergency decisions |
| Disconfirming evidence | observed or community-held records provide reliable replay without conventional logs |

## 5. C3 Measurement integrity

| Anchor | Operational requirement |
| --- | --- |
| Minimum record | construct, unit, target, portfolio, validity domain, uncertainty, missingness, distribution, subgroup, gaming, update, retirement, decision layer and evidence mode |
| Adequate for scope | evidence supports the claimed construct and decision use without ordinal arithmetic, mixed-layer reliability, hidden distribution, or false precision |
| Adequate - control-dependent | known weaknesses are bounded by verified monitoring, triangulation, subgroup safeguards, calibration, and requalification |
| Patchable defect | single-KPI, subgroup-blind, uncalibrated, mixed-layer, or missing-data weakness can be repaired or the claim narrowed |
| Unpatchable for stated claim | the authority claim requires an invalid proxy, arbitrary ordinal arithmetic, systematic invisibility of material harm, or manufactured agreement |
| Indeterminate | construct validity, units, applicability, independence, or uncertainty cannot be established |
| Boundary cases | qualitative evidence, sparse data, privacy, rare tail harm, adaptive preferences, cross-cultural measurement |
| Disconfirming evidence | alternative non-metric evidence reliably establishes the needed function with lower distortion |

## 6. C4 Corrigibility

| Anchor | Operational requirement |
| --- | --- |
| Minimum record | monitoring; failure and appeal triggers; owner; amendment; rollback, deprecation, retirement; recurrence; post-repair review |
| Adequate for scope | observable failure can force timely review and binding correction rather than discretionary consideration |
| Adequate - control-dependent | correction depends on verified monitoring, authority, resources, publication rights, and expiry conditions |
| Patchable defect | review exists but triggers, authority, timing, or repair verification are incomplete |
| Unpatchable for stated claim | material rules are immune to correction or affected-party challenge |
| Indeterminate | formal update powers exist but practical authority, resources, or responsiveness are unknown |
| Boundary cases | constitutional entrenchment, model updates, distributed governance, irreversible actions, legacy dependencies |
| Disconfirming evidence | a non-centralized process demonstrates reliable binding correction through another mechanism |

## 7. C5 Refusal and execution boundary

| Anchor | Operational requirement |
| --- | --- |
| Minimum record | refuse, defer, escalate, request information, narrow claim, safer alternative; competence, authority, capacity, reversibility, spillover, and execution triggers |
| Adequate for scope | the framework can abstain or escalate when a controlling prerequisite is insufficient and cannot convert comparison into permission |
| Adequate - control-dependent | refusal or execution depends on verified authority, monitoring, leases, or requalification triggers |
| Patchable defect | always-answer behavior, ambiguous escalation, or missing authority boundary can be repaired without abandoning the role |
| Unpatchable for stated claim | the role requires action despite unresolved rights, catastrophic risk, authority, competence, capacity, or non-refoulement risk |
| Indeterminate | practical ability to refuse, halt, or prevent unauthorized execution is unestablished |
| Boundary cases | emergency stabilization, human override, delegated systems, advisory outputs, automated execution, institutional lock-in |
| Disconfirming evidence | another architecture reliably contains action without the expected technical or documentary form |

## 8. Floor-linked Stage B category reachability

Every dimension receives Tier F (fully floor-linked), P (partly floor-linked), or N (not ordinarily floor-linked) for the declared scope. Tier F prohibited descriptors return to Stage A; Tier P requires case-specific routing; Tier N remains comparative absent independent C0-C5 evidence. The record names dimension, category, criterion, evidence, scope, materiality and consequence. Unreachable descriptors suspend Stage B; they are never hidden or recoded.

## 9. Overall routing and acceptance tests

The binding order is:

1. no record -> no derived status;
2. partial or invalid administration, unmanaged conflict, or unrecognized controlled value -> protocol refusal;
3. infeasible burden or required access not delivered -> protocol refusal;
4. any established unpatchable material defect -> non-admissible for the stated claim;
5. otherwise, any established patchable material defect -> non-admissible and patchable;
6. otherwise, unresolved protected floor, insufficient evidence, unresolved competence, Indeterminate, or Not reviewed criterion -> indeterminate;
7. otherwise, any criterion whose adequacy depends on named controls -> Stage-A admissible - scoped, control-dependent;
8. only six Adequate for scope findings -> Stage-A admissible - scoped.

Known material defects are never erased by uncertainty elsewhere. All criterion-level uncertainty remains visible in the six-criterion vector, evidence record, and rationale.

No arithmetic aggregation, majority vote, documentation polish, favorable dashboard, or separate authority finding may alter that order. A recorded status and derived status must match; unrecorded, orphaned, or mismatched statuses block public reporting.

## AF v6.2 synchronization note

This artifact implements the v6.2 three-axis record (`decision_status`, `evidence_state`, `review_state`), the non-erasure invariant, perturbation-replay anti-inflation and anti-suppression controls, and the separation of raw agreement, reliability, adjudication, and external validity. These controls clarify the existing protocol and do not confer legal, moral, procurement, or deployment authority.

