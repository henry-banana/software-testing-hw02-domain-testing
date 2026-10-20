# Domain design

Read before selecting classes or designing interactions. Use sourced rules, not implementation behavior.

## Rule ledger

For each rule, record ID, source/version, predicate, expected result, interface and uncertainty. Separate:

- Required business rule: an ordinary user cannot create an administrator-only reservation.
- Transport contract: the request field is `seat_count`.
- Implementation fact: the handler uses `value || 1`.
- Inference: that expression may silently change zero to one.

Only normative requirements/contracts supply expectations. Use implementation facts to design a probe or explain a confirmed result. Retain API/SRS disagreements rather than guessing an endpoint. For an interface mapping, cite which obligations were inherited.

## Vector and nominal fixture

A reservation request may depend on:

`(authenticated_actor, body_identity, resource_state, requested_seats, clock, prior_reservations)`

The nominal fixture includes everything needed to reach the target rule, not just the edited field.

| Dimension | Questions changing case design |
|---|---|
| Actor | Anonymous, invalid/expired identity, user, admin? |
| Ownership | Own object, another user's object, nonexistent object? |
| State | Active/inactive, available/exhausted usage, empty/nonempty? |
| Time | Before/equal/after the sourced cutoff? |
| Values | Correct type, format, unit and supported range? |
| Interface | Does client validation block the intended backend case? |

Do not construct the full Cartesian product by default. Use each-choice representatives and selected interactions for masking/coupled-rule defects. Name the combination criterion instead of claiming exhaustive coverage.

## Partition sets

A partition set models one dimension under one rule. Each class needs a predicate and concrete representative.

For explicitly integer quantity in `[1,3]`:

| Class | Predicate | Representative | Validity |
|---|---|---|---|
| Q-D1 | integer q < 1 | 0 | Invalid |
| Q-D2 | integer 1 <= q <= 3 | 2 | Valid |
| Q-D3 | integer q > 3 | 4 | Invalid |

Missing, null, `""`, `"2"` and `1.5` belong in separate presence/type sets where their semantics differ. Examples containing integers do not establish an integer-only contract.

Check predicates and representatives:

1. Are classes within the set mutually exclusive?
2. Does the set cover its universe, or explicitly exclude part?
3. Does each representative satisfy its claimed predicate?
4. Are unresolved Unicode/coercion/normalization rules separated from invalid classes?
5. Does validity depend on a coordinate held nominal?

Across sets, overlap is expected: an input can have valid type and invalid range. Counts across those sets are not unique test counts.

## Isolating invalid conditions

Start from the valid control and change one dimension. Record unchanged coordinates or reference the complete fixture by ID.

A reservation with invalid category, negative seat count and missing departure does not isolate category validation. Keep required fields nominal and change only category; test missing departure and negative seat count separately. Add multi-invalid cases for explicit interaction/precedence questions without inventing error order.

When persistence/uniqueness is the criterion, rejection also needs relevant state readback. A 500 response alone neither proves corruption nor creates a separate bug if the sole requirement is rejection without insertion. Error-contract/disclosure findings need their own oracle.

## Coupled predicates

Suppose acceptance requires:

`exists AND active AND available >= requested AND now < deadline AND reserved < quota`

Create an all-valid row, then falsify one condition at a time. Add combinations for named questions, such as authenticated identity versus untrusted body user ID.

| Row | Exists | Active | Seats available | Before deadline | Quota available | Expected |
|---|---|---|---|---|---|---|
| DT1 | T | T | T | T | T | Accept |
| DT2 | F | N/A | N/A | N/A | N/A | Reject nonexistent resource |
| DT3 | T | F | T | T | T | Reject inactive resource |
| DT4 | T | T | F | T | T | Reject insufficient seats |
| DT5 | T | T | T | F | T | Reject late request |
| DT6 | T | T | T | T | F | Reject exhausted quota |

Dependent attributes of a nonexistent object are not literally true; mark them not applicable. Error wording/order is not implied by this table. The specification must supply any required precedence when multiple conditions fail.

## State transitions

Record initial state, action, expected next state and observation method.

Preview might quote a reservation while confirmation consumes quota. Two Preview clicks do not establish two confirmed reservations. Seeded counters can isolate limit checking but do not exercise confirmation-to-counter updates.

For create/view/delete:

- Create: read back the exact identifier and contractual fields.
- View: verify actor permission and returned content independently.
- Delete: establish target existence, delete it, read back absence and inspect a control object.

Do not add Update because a document casually calls the feature CRUD.

## Coverage and prioritization

Prioritize controls, invalid classes, equality points, state gates and permissions. Add stress/security probes only within authorized scope. Keep rule/class/boundary/decision inventories separate. Missing coverage is a design gap, not a confirmed SUT defect.
