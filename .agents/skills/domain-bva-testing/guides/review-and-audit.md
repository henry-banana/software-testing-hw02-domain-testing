# Review and audit

Use for AI-output review, result reconciliation and bug grouping. Review evidence before choosing which wording to preserve.

## Two reviews

- Method/spec: do rules, classes, boundaries, contracts and expectations agree with the test basis?
- Evidence: do actual records prove the claimed actor, state, interface, criterion and postcondition?

A good design can be NOT RUN. A flawed generated case is an artifact problem; a confirmed SUT FAIL is a product finding. Failed-test percentage is not AI accuracy.

## Review questions

| Area | Decision to verify |
|---|---|
| Oracle | Expectation sourced or explicitly unresolved? |
| Contract | Field names, enum case, method/path and identity exact? |
| Partitions | Representative/class agreement and gap/overlap assumptions explicit? |
| Boundaries | Equality, units, step and coverage denominator stated? |
| Interactions | Target isolated, or earlier validation can mask it? |
| State | Setup establishes usage/ownership/history without overstating how? |
| Numbers | Raw literals/arithmetic agree across case, bug and report? |
| UI | Evidence shows criterion, not alert alone or unrelated account? |
| Bugs | Every FAIL mapped; variants grouped without hiding distinct behavior? |
| Totals | IDs, attempts, images, bugs and technique labels counted separately? |
| Disclosure | Actual prompts/tools/times/corrections and human decisions distinguished? |

## Preserve and correct

Retain original prompt/output and a visible correction record:

`artifact -> original claim -> verdict -> rule/evidence -> corrected version -> review owner/status`

Use supplied AI-template vocabulary, commonly VALID/INVALID/INCOMPLETE. Preserve its fields/declarations; fill answer areas, rows and evidence-backed checkboxes. Leave human signatures, personal experience and unverified declarations to the student.

If displayed transcripts need punctuation normalization, retain recoverable source text/hash separately and label the transformation. A normalized copy is not byte-identical.

Known prompt time is not unknown artifact-generation time. Name interaction snapshot boundaries instead of claiming complete session logging from a partial export.

## Bug record

Each behavior group needs:

1. Bug ID and affected case IDs.
2. Source version, interface, actor and initial state.
3. Exact setup/input and numbered reproduction.
4. Required versus actual result and relevant postcondition.
5. Evidence, variants and visibility limits.
6. Observed impact, separate from untested risk.
7. Source-supported mechanism or explicitly tentative cause.
8. Regression cases and actual Issue/attachment state when in scope.

Many invalid values can expose one missing-validation bug. Identical messages alone do not prove a shared cause. Explain grouping by behavior and available causal evidence.

## Reconciliation

Use one ledger keyed by stable case ID. Technique labels are attributes; attempts belong to run history. Conflicting definitions of one ID are integrity errors, not silent merges.

Report separately:

- Designed IDs and per-interface totals.
- Evidenced PASS/FAIL/OBSERVATION cases.
- INCOMPLETE and NOT RUN cases.
- Confirmed bug groups.
- Coverage with explicit rule/domain/boundary/decision inventories.
- Artifact-quality verdicts and actual audited-artifact count.
- Image/attachment coverage and publication status.

Recalculate summaries and check reciprocal case/bug links and file paths. A correct ledger does not prove a fresh SUT run.

## Final claim

State result, verification and material limits. File presence/static validation cannot prove unrun device behavior, independent model evaluation, personal review, signature, video upload or final packaging.
