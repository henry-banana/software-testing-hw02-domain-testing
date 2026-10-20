# Worked example: parcel acceptance

This is an original, synthetic design example with no connection to an existing application. The [machine input](../data/examples/parcel.json) and generator make the numeric and enum part reproducible. No parcel form has been executed, and no result below is a product verdict.

## Test basis and oracle

Synthetic parcel acceptance criteria v1:

- R-QUANTITY, AC1: accept integer quantity 1-3 inclusive; reject other quantities without submitting a parcel.
- R-COUNTRY, AC2: accept destination VN or SG; reject other codes without submitting a parcel.

The logical acceptance predicate is `integer(quantity) AND 1 <= quantity <= 3 AND country IN {VN, SG}`. Field names here identify logical inputs; the eventual API/UI contract must supply actual payload types, endpoint, actor permissions and observable response. Error text and HTTP status are unspecified.

## Fixture and controls

F1 is a fresh isolated parcel draft with an authorized test operator, quantity 2 and country VN. Before each case, establish no submitted parcel for that fixture. Use a new draft or an explicit reset so prior accepted submissions cannot affect later cases. Read state through the chosen public interface, and retain a separate control draft when checking that rejection leaves state unchanged.

The shared execution procedure, to bind before running, is:

1. Establish and verify F1 in the chosen versioned environment.
2. Replace F1 values with the complete row input, mapping logical types to the actual interface contract.
3. Submit once and capture the response plus input/action evidence.
4. Read the draft/submission state through the public interface and compare it with the sourced row expectation.
5. Record actual result, evidence and verdict; isolate/reset before the next row.

These are designed steps. Environment details, real actor identity, exact interface commands and observation time remain unfilled until the target project provides them.

## Partitions and boundaries

| ID | Universe and predicate | Representative | Classification |
|---|---|---|---|
| Q-LOW | Integer q <= 0 | 0 | Invalid |
| Q-IN | Integer 1 <= q <= 3 | 2 | Valid |
| Q-HIGH | Integer q >= 4 | 4 | Invalid |
| C-VALID | Country in {VN, SG} | VN and SG | Valid |
| C-INVALID | Other string country codes | XX, selected explicit representative | Invalid |

The integer partitions are disjoint and exhaustive over integers. They do not cover other types. VN/SG representatives cover the two named accepted enum values; XX represents one invalid code, not every invalid string behavior.

Quantity endpoints across adjacent ordered partitions are `0,1,3,4`. The full 2-value inventory is those four values. The full 3-value inventory is their neighbor union `-1,0,1,2,3,4,5`. Country stays VN during quantity probes, and quantity stays 2 during country probes. No combination coverage is claimed.

## Designed cases

All cases use F1 and the shared steps. Expected state behavior comes from AC1/AC2, not from an implementation observation.

| Case | Quantity | Country | Coverage | Expected response and postcondition | Status |
|---|---|---|---|---|---|
| TC-001 | 2 | VN | Nominal; Q-IN; quantity neighbor; C-VALID | Accept and create the corresponding parcel submission | NOT RUN |
| TC-002 | -1 | VN | Q-LOW; 3-value neighbor | Reject; no parcel submitted | NOT RUN |
| TC-003 | 0 | VN | Q-LOW endpoint | Reject; no parcel submitted | NOT RUN |
| TC-004 | 1 | VN | Q-IN lower endpoint | Accept and create the corresponding parcel submission | NOT RUN |
| TC-005 | 3 | VN | Q-IN upper endpoint | Accept and create the corresponding parcel submission | NOT RUN |
| TC-006 | 4 | VN | Q-HIGH endpoint | Reject; no parcel submitted | NOT RUN |
| TC-007 | 5 | VN | Q-HIGH; 3-value neighbor | Reject; no parcel submitted | NOT RUN |
| TC-008 | 2 | SG | C-VALID second enum | Accept and create the corresponding parcel submission | NOT RUN |
| TC-009 | 2 | XX | C-INVALID | Reject; no parcel submitted | NOT RUN |

Actual values are null; execution evidence is empty for all rows. Design inventory coverage is 7/7 quantity points and 3/3 selected enum representatives, with 9 unique cases because the nominal control belongs to both inventories. Executed coverage is zero. This is not complete feature coverage.

## Manual completion and review

Add explicit wrong-type cases, such as quantity `1.5`, under the integer requirement. Obtain the interface contract before deciding whether a numeric string is accepted/coerced. Missing/null/empty and whitespace semantics need their own test-basis decisions. Add state and interaction coverage only when requirements supply those behaviors. Avoid inventing price limits, account history, persistence guarantees beyond the stated postcondition or exact error strings.

If a later authorized run accepts quantity 0 and submits a parcel, it contradicts R-QUANTITY and supports a FAIL with state evidence. A design prediction alone does not create a confirmed bug. If input is rejected but required state readback is missing, grade the full rejection-and-no-submission criterion according to [execution evidence](execution-evidence.md).
