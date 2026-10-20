# Boundary analysis

Read for ordered values, lengths, counts, times or coupled comparisons. Start from partitions and name the project boundary-selection convention.

## Boundary record

| Field | Required detail |
|---|---|
| Rule/domain | Stable IDs and source/version |
| Variable | Value, length, timestamp, counter or expression |
| Predicate | Exact operator, including equality |
| Unit/representation | Integer, decimal scale, currency, time unit/timezone or length definition |
| Neighbor step | Sourced or explicitly selected representable increment |
| Points | Exact values and valid/invalid classification |
| Controls | Other inputs needed to reach the condition |
| Coverage criterion | Selected thresholds,2-value BVA,3-value BVA or stated local convention |

Unknown precision/equality is an open question, not a guessed oracle. Continue independently specified cases.

## Selecting points

For discrete step `d` and selected threshold `b`, start with `b-d`, `b`, `b+d`. Classify each by its predicate:

| Predicate | b-d | b | b+d |
|---|---|---|---|
| x >= b | Invalid | Valid | Valid |
| x > b | Invalid | Invalid | Valid |
| x <= b | Valid | Valid | Invalid |
| x < b | Valid | Invalid | Invalid |

These selected-threshold triplets do not automatically establish complete 3-value BVA over adjacent partition endpoints.

Under ISTQB CTFL 4.0.1,2-value BVA takes each identified boundary value and its nearest neighbor in the adjacent partition;3-value BVA takes each boundary value and both neighbors. Identify endpoints of relevant invalid as well as valid partitions, then deduplicate before computing coverage.

For integer partitions `x <= 9`, `10 <= x <= 11`, `x >= 12`:

| Inventory/criterion | Unique values |
|---|---|
| Valid-interval thresholds | 10,11 |
| Triplets around those thresholds | 9,10,11,12 |
| Boundary values of all three partitions | 9,10,11,12 |
| Complete 2-value inventory for those boundaries | 9,10,11,12 |
| Complete 3-value inventory for those boundaries | 8,9,10,11,12,13 |

Four selected cases can be intentional without covering the six-item 3-value inventory. If the project uses another convention, cite it, name the denominator and show values. Do not relabel an existing suite as complete without checking its points.

## Length, numbers and time

### String length

State whether length counts bytes, code points, code units or grapheme clusters when specified. An ASCII implementation regex does not settle an unspecified Unicode-digit requirement.

For a sourced 10-11 digit rule, 9/10/11/12 are selected neighbors of the valid interval; keep prefix/charset nominal and test wrong prefix separately. Empty/null are presence classes, not substitutes for length neighbors.

### Money and decimals

Use declared currency/precision. Do not invent 0.01, rounding or a discount cap. Integer fixtures can isolate a formula defect without deciding rounding.

For `total >= 100` with integer-unit fixture, use 99/100/101. A sourced 10 percent adjustment on 200 gives an exact adjustment of 20 and final value of 180; check both, not just success status.

For `amount > 0` with unspecified scale, zero is unambiguous. Label the fixture step for negative/positive probes; do not infer fractional values must be rejected.

### Time

Name the varied operand and frozen clock. With strict `now < expiry`, UTC and one-second resolution:

| Frozen now | Expiry input | Expected |
|---|---|---|
| 08:00:00Z | 07:59:59Z | Reject |
| 08:00:00Z | 08:00:00Z | Reject |
| 08:00:00Z | 08:00:01Z | Accept |

A date-only expiry does not define end-of-day/timezone semantics. Keep equality unresolved until the source defines its instant. Do not alter the original clock to manufacture an existing screenshot's timestamp.

### Counters

For `used < limit` with limit 2 and integer counters, 0/1/2/3 gives accept/accept/reject/reject. Keep identity fixed and record public-workflow versus direct-setup provenance.

## Surfaces and intersections

The constraints `x >= 0`, `y >= 0`, `x+y <= 100` define a two-dimensional domain. Per-field min/max testing can miss the sum comparison.

At interior ON point `(60,40)`:

- `(59,40)` and `(60,39)` are inside the sum constraint.
- `(61,40)` and `(60,41)` are outside it.
- All remain nonnegative, isolating the sum boundary.

Inspect intersections `(0,0)`, `(100,0)` and `(0,100)`. Moving `(100,0)` to `(100,-1)` crosses nonnegativity, not the sum boundary; name the distinction. Mark infeasible combinations instead of inventing runnable state.

ON/OFF/IN are geometric labels, not verdicts. Show coordinates and validity; equality belongs to the operator's permitted side. Explain local label conventions.

## Unsupported limits

A large input is not an upper-boundary test without an upper rule. Treat it as an exploratory probe with stated resource limit/observation criteria. Do not assign FAIL for an unspecified reset, maximum or rounding policy.
