# AF v6.2 Artifact Authority and Version Policy

## 1. Purpose

This policy prevents a derivative, implementation, rendering, example, or release-control file from silently acquiring authority it does not possess.

## 2. Authority order

1. **Core Protocol:** controls AF's normative architecture and canonical meanings.
2. **Delegated companion:** controls only the topic explicitly delegated by the Core.
3. **Machine-readable registry and schemas:** bind exact identifiers and fields but do not create new normative meaning.
4. **Workbook and reference logic:** implement or illustrate the controlling meaning; they cannot revise it.
5. **Methods Article and submission materials:** communicate the protocol for a venue; they cannot override it.
6. **Examples and synthetic data:** demonstrate behavior only.
7. **Release records, manifests, hashes, and verifiers:** establish artifact identity and internal consistency only.

## 3. Conflict rule

A conflict is not resolved by choosing the newest-looking file, the most convenient output, or the artifact that yields the most favorable status. The conflict is logged, the Core and delegated authority are identified, and the affected finding is held as indeterminate or refused until the conflict is corrected and reissued.

## 4. Release version versus component version

`AF-v6.2` is the package release. `AF-SB12-v5.6` and `AF-SB-RELATION-v6.0` are stable component identifiers retained because their semantics did not change. Updating a package version does not authorize silent component renaming. A component version changes only when its controlling semantics change.

Historical v6.1 references may remain only in provenance or migration history where they explicitly identify a pre-v6.2 audit/synchronization baseline. They do not carry current package authority.

## 5. Change classes

- **Major:** changes rights floors, eligibility criteria, precedence, status meaning, Stage B dimensions, relation semantics, or authority boundaries.
- **Minor:** adds compatible instruments, evidence controls, provenance, verification, implementation hardening, or publication-integrity improvements.
- **Patch:** corrects typographical, rendering, or non-semantic metadata defects.

Version 6.2 is a minor release. It does not change a Stage A or Stage B outcome for the same valid inputs under v6.0.

## 6. Public-claim boundary

A verified package is not a validated protocol. A synchronized rendering is not a legal opinion. A favorable AF finding is not certification, due diligence, procurement approval, safety assurance, moral approval, community consent, or permission to deploy.

## AF v6.2 synchronization note

This artifact implements the v6.2 three-axis record (`decision_status`, `evidence_state`, `review_state`), the non-erasure invariant, perturbation-replay anti-inflation and anti-suppression controls, and the separation of raw agreement, reliability, adjudication, and external validity. These controls clarify the existing protocol and do not confer legal, moral, procurement, or deployment authority.

