# Feature record template

Adapt only without an existing required project template. Replace bracketed fields and keep contractual identifiers exact. This is a design scaffold, not an execution record.

## 1. Test basis and scope

| Field | Value |
|---|---|
| Feature/interface | [Feature ID and API/Web/Admin/Mobile] |
| Mode | [Design/Review/Execute] |
| Requirement source/version | [Source and revision] |
| Implementation version/local changes | [Revision and differences] |
| In scope | [Required behavior] |
| Open questions | [Conflicting/missing rules and affected cases] |

| Rule ID | Source | Predicate | Observable expectation | Interface/mapping | Certainty |
|---|---|---|---|---|---|
| [R1] | [Exact section] | [Constraint] | [Result/postcondition] | [Seam] | [Direct/mapped/unresolved] |

## 2. Nominal fixture

| Fixture ID | Actor/role | Inputs | Initial state | Clock/unit | Setup/reset | Readback/control |
|---|---|---|---|---|---|---|
| [F1] | [Identity] | [Complete values] | [Relevant state] | [Precision/timezone] | [Public workflow/labeled direct seed] | [Observation method] |

## 3. Domain partitions

| Domain ID | Dimension/universe | Predicate | Representative | Validity | Nominal controls | Rules | Cases |
|---|---|---|---|---|---|---|---|
| [D1] | [Dimension] | [Class] | [Value] | [Valid/invalid/unresolved] | [Fixture] | [R1] | [TC1] |

Explain gap/overlap checks, selected interactions and omitted combinations.

## 4. Boundaries

| Boundary ID | Variable/predicate | Unit/step | Endpoints | Exact points/validity | Coverage criterion | Rules/domains | Cases |
|---|---|---|---|---|---|---|---|
| [B1] | [Comparison] | [Source or declared fixture step] | [Values] | [Values and validity] | [Named inventory] | [R1/D1] | [TC1] |

State the inventory/denominator before percentages. Explain infeasible points and unsupported maxima/precision.

## 5. Interactions/state

| Decision/transition ID | Initial state/conditions | Action | Required next state/result | Setup provenance | Cases |
|---|---|---|---|---|---|
| [I1] | [State/row] | [Action] | [Expectation] | [Workflow/direct fixture] | [TC1] |

## 6. Detailed cases

### [TC1]

| Property | Value |
|---|---|
| Technique | [Domain/BVA/both; one case ID] |
| Rule/domain/boundary | [R1/D1/B1] |
| Interface/actor | [Seam and identity] |
| Fixture | [F1 and deviations] |
| Status | NOT RUN |
| Bug/finding | [None until supported] |

**Preconditions:** [Exact initial state, setup/reset and source revision.]

**Input:** [Complete payload/UI values, including unchanged required values.]

**Steps:**

1. [Establish/check preconditions.]
2. [Perform exact action/request.]
3. [Observe response and relevant public readback.]

**Expected:** [Sourced response/postcondition; exact status/error only if required.]

**Actual:** Not executed. Do not populate from expected output or an unrelated run.

**Evidence:** None for this designed case. When executed, record observation time, optional simulated clock, run ID and evidence paths.

**Rationale:** [Why this representative/boundary; which other constraints are controlled.]

## 7. Results and coverage

| Interface | Designed IDs | PASS | FAIL | OBSERVATION | INCOMPLETE | NOT RUN |
|---|---|---|---|---|---|---|
| [Seam] | [Count] | [Count] | [Count] | [Count] | [Count] | [Count] |

`designed = PASS + FAIL + OBSERVATION + INCOMPLETE + NOT RUN`

`executed_with_sufficient_evidence = PASS + FAIL + OBSERVATION`

List covered/uncovered inventory IDs; count images/attempts separately.

## 8. Bugs and AI corrections

| Bug | Failed cases | Required vs actual | Evidence | Cause confidence | Issue/attachment state |
|---|---|---|---|---|---|
| [Bug] | [TCs] | [Observed discrepancy] | [Paths] | [Source/hypothesis] | [Actual state] |

| Artifact | Original claim | Audit verdict | Rule/evidence | Visible correction | Human-review status |
|---|---|---|---|---|---|
| [Artifact] | [Preserved claim] | [Template vocabulary] | [Source] | [Correction] | [Actual status] |

## 9. Remaining required actions

List real gaps: clarification, unrun interface, missing readback, genuine images, authorized publication, human review/signature or final export. File presence is not completion.
