# Auditable Flourishing v6.2 Challenge Administration Handbook

## Status and role

This handbook is the binding administration companion to the v6.2 Core Protocol. It governs host duties, reviewer competence, conflicts, immutable pre-discussion ratings, evidence notices, adjudication, appeals, affected-party standing, public reporting, AI assistance, and challenge integrity. It supports synthetic replay, reviewer training, controlled shadow-mode work, Phase 0, and independently governed pilots. It does not establish empirical validity or authorize live deployment.

Where this handbook conflicts with the Core Protocol, the Core controls general semantics. The Reviewer Training, Qualification, and Rating-Deposit Standard controls reviewer curriculum, qualification maintenance, deposit properties, and AI-assistance classification. The Scenario Governance and Calibration Standard controls scenario identity and matching.

[[PAGEBREAK]]

[[TOC_HEADING]]

[[TOC]]

[[PAGEBREAK]]

## 1. Administration principles

A challenge must be capable of testing the protocol rather than merely enacting the author, sponsor, candidate, or host's preferences. Strictness and procedural fairness are simultaneous requirements. A material C0-C5 defect cannot be averaged away, but no reviewer creates a silent veto. Every adverse finding must be evidence-specific, scoped, causally material, falsifiable where possible, contestable, and recorded. Every positive finding must be bounded, expiring, and incapable of silently becoming certification or authorization.

Administration distinguishes candidate failure, protocol failure, host failure, evidence insufficiency, reviewer non-assessment, and burden infeasibility. These events have different implications and may not be collapsed into one fail state.

## 2. Roles and separation

The minimum role set is:

- sponsor or commissioning body;
- independent host;
- candidate representative;
- reviewers;
- adjudicators;
- data and rating-deposit custodian;
- statistician or analysis custodian;
- affected-party representatives where applicable;
- publication authority;
- independent conflict and appeal authority.

One person may hold more than one low-conflict administrative role only when the profile permits it and the role combination is disclosed. For an affiliated entrant, the protocol author may act only as candidate sponsor or technical explainer. The author may not select reviewers, control the host, rate candidates, access sealed initial ratings before deposit closure, adjudicate, control analysis, or veto publication.

## 3. Mandatory independence and host-interest dossier

Before reviewers receive candidate material, the host publishes or securely registers:

- sponsor, host, candidate, reviewer, adjudicator, custodian, analyst, and publication roles;
- appointment, removal, payment, funding, and reporting lines;
- data custody and access;
- reviewer-pool construction and selection rule;
- conflict adjudication and recusal;
- protocol amendment authority;
- publication control and security-redaction limits;
- protected dissent, null-result, adverse-result, and protocol-failure publication rights;
- affected-party selection, standing, compensation, access, and withdrawal;
- the host's institutional, financial, legal, procurement, reputational, or policy interest in the outcome;
- any preferred or precommitted outcome and the safeguards against it;
- AI systems permitted in evidence retrieval, summarization, translation, rating, adjudication, or analysis.

The dossier is **inadequate** when sponsor, candidate, author, or interested host can control material data, reviewer selection, adjudication, analysis, or publication; when adverse outcomes can be suppressed; when dissent can be erased; when rating deposits are mutable or available to the panel before closure; when required affected-party representation is absent without a justified narrower scope; or when AI-generated ratings are presented as independent human ratings.

An inadequate dossier produces `protocol_refusal_to_evaluate`, a narrower non-dispositive methods exercise, or an explicit protocol-failure record. It never produces a positive independence claim.

## 4. Reviewer competence and panel fit

Reviewer competence is task-specific, not a global credential. The host maps the case to needed capabilities: governance and policy, rights and law, measurement and evaluation, technical audit, safety and risk, domain practice, disability and accessibility, community or customary governance, and lived experience. Missing competence can require assistance, panel expansion, narrower scope, indeterminacy, or refusal.

Qualification and maintenance requirements are owned by the Reviewer Training, Qualification, and Rating-Deposit Standard. At minimum, every reviewer must have:

- completed the current orientation and codebook;
- completed the current frozen practice bank;
- demonstrated ability to distinguish material defect, indeterminacy, and ordinary weakness;
- demonstrated correct rights-floor and refusal routing;
- disclosed conflicts and AI assistance;
- retained current qualification for the profile and domain;
- deposited an independent initial assessment before discussion.

## 5. Immutable pre-discussion rating deposits

A reliability or independence claim requires each initial rating to be deposited before panel discussion in an independently controlled system that provides:

- server-side timestamp;
- content SHA-256 or equivalent cryptographic digest;
- append-only audit history or explicit supersession chain;
- reviewer identity or controlled pseudonym binding;
- access control preventing other reviewers and interested parties from viewing open ratings;
- exportable record and audit evidence;
- declared reason for any withdrawal, correction, or supersession.

A shared spreadsheet does not establish these properties. It may aggregate records only after deposit closure. Examples of possible implementations include a preregistration repository, an electronic data-capture system with an audit trail, or signed version-controlled records under independent host custody. The protocol is technology-neutral; the properties are mandatory.

A late, edited, unverified, or model-generated record remains usable for exploratory process analysis only if clearly labeled. It is excluded from coefficients presented as independent human pre-discussion reliability.

## 6. Criterion order and halo control

The host preregisters a balanced or randomized criterion order for independent rating. Reviewers record a brief global-impression probe before criterion-level analysis and again after completing the record. The probe is never used to determine the outcome. It tests whether broad favorable or adverse impressions explain correlated criterion ratings.

The analysis reports order effects, global-impression shifts, criterion-specific agreement, and final-layer agreement separately. A high final agreement combined with weak criterion agreement or strong global-impression dependence is not evidence of reliable criterion application.

## 7. Mandatory adjudication sequence

1. **Protocol and scenario binding.** Confirm exact protocol version, candidate versions, scope, scenario-set version and hash, profile, evidence cut-off, and rating-deposit system.
2. **Conflict and panel-fit screen.** Recuse, manage, or refuse where competence or conflict is inadequate.
3. **Independent rating deposit.** Reviewers complete and seal initial records before discussion.
4. **Evidence-specific notice.** Each proposed material finding states criterion or dimension, scope, evidence pointer, causal materiality, uncertainty, root cause, and patch or clarification condition.
5. **Symmetric response.** Candidates receive a defined response period and equal access to the non-security-sensitive record used against them.
6. **Affected-party response.** Where material, affected parties can submit evidence, identify missing harms, challenge scope, and preserve dissent without retaliation.
7. **Panel adjudication.** At least three non-conflicted adjudicators review unresolved matters. At least one is selected through a route not controlled solely by the host.
8. **Perturbation admission and replay.** Every proposal identifies candidate, dimension, alternative category, anchor conflict, evidence, materiality, proposer, and timing. It enters replay only after concurrence by a second independent reviewer or reasoned admission by a non-proposing independent adjudicator. Rejections retain reasons and appeal. Every admitted alternative is replayed under AF-SB-RELATION-v6.0.
9. **Recorded determination.** Majority, minority, unresolved uncertainty, conflicts, recusals, root causes, patch conditions, and burden are recorded.
10. **Bounded appeal.** A procedural or evidentiary appeal is available. New evidence can reopen a finding under a declared rule; no indefinite relitigation is required.
11. **Publication and expiry.** Publish bounded outputs, limitations, dissent, and authority vector; set expiry or requalification triggers.

## 8. Evidence modes and equity

Functionally equivalent evidence is admissible when it supports the required function. Computational, legal, institutional, oral, observed, participatory, community-held, customary, translated, or restricted evidence may be used. For non-documentary or community-governed evidence, record provenance, consent, purpose, custody, interpretation, translation, triangulation, challengeability, compensation, withdrawal, data sovereignty, confidentiality, and uncertainty.

Professional polish is not evidence strength. Hosts must test whether low-resource or non-documentary candidates receive higher missingness, burden, adverse findings, or lower confidence after controlling for substantive safeguard quality. Assistance must be recorded because it can improve access while also changing the candidate artifact.

## 9. Criterion states and public status grammar

Each C0-C5 criterion receives one state:

- `adequate_for_scope`;
- `adequate_control_dependent`;
- `indeterminate`;
- `material_defect_patchable`;
- `material_defect_unpatchable_for_stated_claim`;
- `not_reviewed`.

The Stage A public status uses the canonical human-readable phrase and machine token. Bare Pass, Fail, Approved, Certified, Safe, Ethical, Legitimate, Valid, or Compliant labels are prohibited. Every output binds candidate identity and version, scope, population, jurisdiction or community, evidence cut-off, host, protocol version, profile, issue date, expiry or review date, conditions, dissent, and appeal route.

## 10. Stage B disagreement and relation routing

The base relation and all defended perturbation relations are published. Under valid prerequisites:

- invariant one-direction dominance -> `dominance`;
- invariant crossing -> `incomparable`;
- changing relation, tie, or potentially repairable unresolved evidence -> `non_decisive`;
- invalid comparison prerequisites -> `refusal_to_compare`.

The host must not classify every disagreement as non-decisive. Peripheral disagreement that leaves a crossing invariant still permits incomparability. A dominance relation that changes under any defended alternative is not robust enough to publish as dominance.

## 10.1 Perturbation admission and anti-veto integrity

A proposal is not self-executing. Admission tests evidence supportability, not whether the proposed category is ultimately correct. Majority preference may not suppress a well-supported dissent. Unsupported, duplicate, strategically delayed, or immaterial proposals are rejected with public reasons and appeal. Causally coupled alternatives are tagged and replayed jointly. Reports publish proposed, admitted, rejected, withdrawn, superseded, reversal-capable, and relation-changing counts. `C2-D05 Unsupported perturbation inflation` applies when proposals are multiplied to manufacture instability. Host or sponsor pressure to admit, reject, delay, or conceal an alternative voids independence.

## 11. Reliability and calibration

Reliability is reported by criterion, dimension, and decision layer, never as one blended value. Ordinal criterion or dimension categories use a preregistered coefficient appropriate to ordered data and prevalence, such as Gwet's AC2 or another justified statistic. Nominal final outcomes use an appropriate nominal coefficient. Continuous burden or time measures use an appropriate agreement or reproducibility statistic.

The Phase 0 study is exploratory. Its small sample estimates prevalence, disagreement structure, completion time, missingness, order effects, and plausible interval width. It must not be presented as confirmatory merely because a point estimate exceeds a threshold. A larger study uses simulation-based precision or decision-error design informed by Phase 0, with the coefficient, target, interval width, missing-data rule, subgroup analysis, and consequence of a miss fixed before data are unsealed.

Multiplying criterion coefficients to estimate the reliability of the C0-C5 conjunction is prohibited. The final Stage A outcome must be rated and analyzed directly.

## 12. AI assistance in review

Every reviewer and analyst discloses tool, provider, model or version, date, task, prompt or instruction class where lawful, data sent, retrieval source, output used, verification, and whether the tool influenced a category or outcome.

AI may support retrieval, formatting, translation, or clerical comparison under declared controls. Ratings materially generated, suggested, harmonized, or revised by the same model are correlated by construction and cannot be counted as independent human ratings. They form a separate AI-assisted condition. A model must not receive protected or community-governed evidence without authority, purpose limitation, security, and data-sovereignty compliance.

Undisclosed material AI influence is an administration defect. It can invalidate a reliability claim even when the final ratings appear consistent.

## 13. Burden, capacity, and access gate

Feasibility is conjunctive. Review cannot be marked feasible unless reviewer hours, adjudication hours, calendar time, qualified reviewer count, and required accessibility or interpretation support meet demand. Average hours per case cannot offset an impossible calendar, absent reviewer, or unmet access need.

Burden is reported separately for:

- completed feasible administrations;
- infeasible or stopped before rating;
- aborted during review;
- incomplete records.

The host reports reviewer, candidate, affected-party, access-provider, adjudication, analysis, and publication burden separately, including uncompensated time and opportunity cost. A favorable mean among completed cases cannot hide excluded or abandoned cases.

## 14. Affected-party standing and safeguards

Affected parties have rights to submit evidence, challenge scope and factual records, request accessible communication, identify missing harms, preserve minority views, seek correction or withdrawal of improperly obtained evidence, appeal material findings, and petition for protocol amendment or retirement. Participation must not be coerced or used as a condition of ordinary rights or services.

Live involvement requires appropriate legal, ethical, and community governance. Phase 0 synthetic work cannot claim affected-party legitimacy and must not use simulated participation as a substitute.

## 15. Public report and anti-shield language

The public report contains:

- exact identity, scope, scenario set, host, profile, evidence cut-off, and protocol version;
- independence and host-interest dossier;
- deposit-system description and integrity exceptions;
- criterion states, root causes, evidence, uncertainty, and patch conditions;
- Stage B profile, base relation, perturbation set, and public outcome where eligible;
- affected-party participation, burden, access, and dissent;
- appeals, expiry, and requalification;
- authority-specific verdict vector;
- explicit anti-shield statement.

Required anti-shield statement:

> An Auditable Flourishing finding is a protocol-relative, scope-bound assurance record. It is not a certificate, warranty, legal opinion, due-diligence safe harbor, procurement defense, proof of reasonable care, proof that flourishing occurred, or authorization for deployment. It does not bar legal claims, regulatory action, remedy, appeal, or later adverse evidence. Any legal or procurement characterization must reproduce the full status, scope, limitations, dissent, conditions, expiry, and separate competent authority.

## 16. Protocol failure and stopping

The host pauses or stops when there is material rights risk, coercion, retaliation, data exposure, unmanaged conflict, sponsor or host interference, publication veto, rating-deposit compromise, scenario leakage, pervasive anchor failure, excessive burden, or inability to distinguish candidate and protocol defects. Stopping is a valid scientific outcome.

## 17. Minimum templates

The release supplies machine-readable and human-readable templates for:

- candidate and scope registration;
- scenario-set registration;
- independence and host-interest dossier;
- reviewer qualification and AI disclosure;
- immutable rating deposit metadata;
- evidence-specific notice;
- root-cause and patch log;
- adjudication and appeal;
- burden and access;
- decision value;
- authority-specific verdict vector;
- public report;
- protocol petition and amendment.

## Cited works

Gwet, K. L. (2014). *Handbook of inter-rater reliability* (4th ed.). Advanced Analytics.

Harris, P. A., Taylor, R., Thielke, R., Payne, J., Gonzalez, N., & Conde, J. G. (2009). Research electronic data capture (REDCap): A metadata-driven methodology and workflow process for providing translational research informatics support. *Journal of Biomedical Informatics, 42*(2), 377-381. https://doi.org/10.1016/j.jbi.2008.08.010

Krippendorff, K. (2018). *Content analysis: An introduction to its methodology* (4th ed.). SAGE.

## AF v6.2 synchronization note

This artifact implements the v6.2 three-axis record (`decision_status`, `evidence_state`, `review_state`), the non-erasure invariant, perturbation-replay anti-inflation and anti-suppression controls, and the separation of raw agreement, reliability, adjudication, and external validity. These controls clarify the existing protocol and do not confer legal, moral, procurement, or deployment authority.

