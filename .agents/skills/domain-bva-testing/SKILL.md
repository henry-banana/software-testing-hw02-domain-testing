---
name: domain-bva-testing
description: Design and review black-box test cases from requirements using Domain Testing, equivalence partitions, Boundary Value Analysis (BVA), state constraints and traceable evidence.
---

# Domain Testing and Boundary Value Analysis

Turn versioned requirements into predicates, partitions, boundary points and reproducible cases. Keep expected behavior independent of implementation, and designed work separate from executed evidence. This skill tests input domains; it does not model Domain-Driven Design architecture.

## Choose a mode

| Request | Mode | Required outcome |
|---|---|---|
| New feature or incomplete design | Design | Rules, nominal fixture, partitions, boundaries, cases marked NOT RUN |
| Existing cases or AI output | Review | Traceability gaps, unsupported claims and visible corrections |
| Run an authorized plan | Execute | Actual results, relevant readback, verdicts and interface-specific evidence |

Honor the requested mode. Design completion does not authorize execution. Continue already authorized work without requesting the same permission again.

## Load support only when needed

- Before selecting classes/interactions, read [Domain design](guides/domain-design.md).
- For ordered values or coupled comparisons, read [Boundary analysis](guides/boundary-analysis.md).
- Before execution or grading screenshots/logs, read [Execution and evidence](guides/execution-evidence.md).
- For draft review, bug grouping or totals, read [Review and audit](guides/review-and-audit.md).
- Without an existing required schema, adapt [Feature record](assets/feature-record.md); never replace a supplied template with it.
- For CSC13003 EShop only, load [FR-17 example and local adapter](examples/eshop-fr17.md).
- To evaluate this skill, use [Behavioral scenarios](evals/scenarios.md).
- For provenance/source conflicts, consult [Sources and design decisions](guides/sources.md).

## 1. Establish the oracle

Read the specification, acceptance criteria, public contract and relevant course guidance. Record versions. Give each behavior a stable rule ID, condition and observable response/postcondition. Distinguish direct requirements, interface mappings, implementation observations and unresolved assumptions.

Keep contractual field names, enums and status tokens exact. Source code can explain a mechanism; it cannot redefine expected behavior. Resolve source conflicts only for affected expectations and continue independent cases. Do not invent Update, rounding, maxima or reset rules from a familiar feature name.

**Done when:** every expectation has a source or an explicit open question/observation.

## 2. Build a valid control

Record the input vector and relevant state: actor/role, ownership, object existence, counters, clock, amount, quantity and interface. Choose one nominal fixture satisfying all known preconditions.

Inspect startup/seed behavior before running it. Use isolated mutable fixtures and preserve original data and pre-existing user edits. Label direct database setup: it establishes state but does not prove the bypassed public workflow.

**Done when:** candidates identify their actor, state and dimensions held nominal.

## 3. Partition the domains

Write predicates and concrete representatives for valid, invalid and unresolved classes. Distinguish absence, null, empty, whitespace, type, format, range, identity and state where semantics differ.

Check overlaps/gaps within each partition set; overlap across dimensions is normal. Prefer one invalid condition per case so earlier validation does not mask the target. Add deliberate interactions as decision rows, state transitions or coupled constraints. Each-choice coverage is not all-combinations coverage.

**Done when:** each retained class has a source, representative, validity and case mapping; omissions are explained.

## 4. Derive boundaries

Identify ordered partition endpoints, comparison equality, units and a justified neighboring step. Show exact points and their valid/invalid classification. Record time resolution/timezone/clock and money precision rather than guessing them.

Distinguish selected business-threshold triplets from complete 3-value BVA over all identified partition endpoints. State the inventory and denominator before reporting coverage. Deduplicate shared points without losing mappings.

For coupled inputs, choose feasible ON points and change a controlled coordinate to either side; name any other constraint crossed. Unsupported maxima/precision remain open questions.

**Done when:** every selected point is reproducible, classified and mapped to rules/cases.

## 5. Specify cases

Preserve stable IDs and required schemas. Each case needs technique and rule/domain/boundary IDs; interface/actor; exact fixture/reset; complete input; numbered actions; sourced expected response/postcondition; and actual/evidence/verdict when executed.

Multiple assertions may establish one business outcome, such as rejection plus unchanged state. Do not invent an exact error string or HTTP status when only rejection is specified. Do not hide payload fields behind an ellipsis.

**Done when:** another tester can reproduce without guessing input or account history.

## 6. Review and execute within scope

Check equality, masking, cross-field constraints and state before execution. Use implementation inspection for hypotheses, not oracle changes. For authorized runs, capture setup, action/request, response and relevant public-interface readback. Separate real observation time from simulated SUT clock and environment failure from product failure.

Loading this skill grants no permission for subagents, browser/device automation, publication or other external mutation. Follow existing user authorization, ask only for missing authorization/input blocking the affected action, and continue independent authorized work.

**Done when:** the evidence proves the criterion, or the missing precondition/step/evidence is explicit.

## 7. Classify and group

Use the caller's vocabulary; otherwise use:

| Status | Criterion |
|---|---|
| PASS | Required behavior and applicable postcondition are evidenced |
| FAIL | Evidence contradicts a sourced requirement |
| OBSERVATION | Behavior observed, but oracle unspecified/conflicting |
| INCOMPLETE | Run/record lacks necessary precondition, action or evidence |
| NOT RUN | Designed case not executed |

A valid update rejected at validation is FAIL for acceptance, even when persistence is unreached. A success alert alone is INCOMPLETE for save-and-reload. API success does not prove UI success. A final screenshot does not independently prove an action sequence; record human attestation separately.

Group failures by behavior and supported cause. Each FAIL needs a finding/mapped bug, not a new bug per boundary value. Separate observed impact from hypothetical risks and source-supported causes from hypotheses.

**Done when:** verdicts explain criterion/evidence and bugs have reproducible traceability.

## 8. Reconcile and deliver

Count unique case IDs, not technique labels, attempts or images:

`designed = PASS + FAIL + OBSERVATION + INCOMPLETE + NOT RUN`

`executed_with_sufficient_evidence = PASS + FAIL + OBSERVATION`

Keep bug counts, screenshot coverage and artifact-quality verdicts separate. Report coverage against named inventories, not unsupported completeness percentages. Flag conflicting definitions of one ID instead of silently merging them.

Deliver requested Markdown analysis/cases/results, bugs and AI corrections. Preserve supplied template structure/filenames. Record actual tools/prompts/outputs/times from available records; leave unknown timestamps, personal decisions and signatures unknown. List pending actions without declaring the whole submission ready.

**Done when:** IDs/counts/links reconcile and final claims state exactly what was verified and what remains unproven.
