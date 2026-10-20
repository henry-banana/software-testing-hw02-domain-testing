# Behavioral scenarios

These are evaluation inputs and acceptance criteria, not recorded agent runs or SUT results. Use a scratch workspace and relevant skill resources. Keep generated artifacts/logs outside the submission.

Structural validation checks packaging/links, not model selection or behavior. If independent agents/model evaluation are unavailable or unauthorized, label a same-session walkthrough accordingly; do not claim independent evaluation.

## Evaluation protocol

Give an authorized evaluator the task prompt, skill and raw inputs without these acceptance criteria. Grade the produced artifacts afterwards. Compare against a no-skill run only when both actually occurred under comparable conditions.

Record tool/model if known, actual time, input/skill revisions, generated output, criterion results and limits. These scenarios are not additions to 114 HW02 test results or new product bugs.

## E1 - Transfer to a different feature

**Task:** Design a parcel form. Quantity is integer 1-3 inclusive. Country is VN or SG; nominal fixture quantity 2 / country VN. No price/length rule. Do not execute.

**Accept:** Sourced classes/control, selected neighbors 0/1/2/3/4, separate type/presence cases, country held nominal and all new cases NOT RUN. No EShop paths, invented price maximum or execution claims.

## E2 - Equality and coverage vocabulary

**Task:** Integer length 10-11 is accepted. Analyze all three ordered partitions and request full 3-value BVA over each adjacent partition endpoint.

**Accept:** Boundary inventory 9/10/11/12; neighbor union 8/9/10/11/12/13; correct validity. Distinguish this from four selected neighbors around the valid interval. Do not call 9/10/11/12 complete for the six-item criterion.

## E3 - Coupled inputs

**Task:** Integer x>=0, y>=0 and x+y<=100. Exercise the sum boundary and intersections without executing.

**Accept:** ON (60,40), neighbors(59,40)/(61,40)/(60,39)/(60,41), correct validity, relevant intersections and named constraints crossed by corner neighbors. Independent per-field min/max does not exhaust the sum constraint.

## E4 - Exact arithmetic versus implementation

**Task:** Coupon requires total>=300000 and grants 10 percent off; integer-VND fixture. Observed total 400000 returns discount=-3600000/final=4000000. Review and design an equality probe.

**Accept:** Expected 40000/360000, observed discrepancy, selected 299999/300000/300001 with equality valid, unchanged actual literals and no invented rounding. New unrun equality cases remain NOT RUN.

## E5 - Time and missing rules

**Task A:** Strict now<expiry, frozen now 2026-10-19T08:00:00Z, one-second resolution. Design expiry neighbors.

**Accept A:**07:59:59Z/equal08:00:00Z/08:00:01Z gives reject/reject/accept; name varied operand and clock.

**Task B:** Another rule says only valid expiry date, with no timezone/cutoff or quantity maximum.

**Accept B:** Preserve unknown equality/timezone/maximum; no invented end-of-day, millisecond precision or upper-boundary FAIL. Continue unambiguous cases.

## E6 - Evidence grading

| Record | Requirement and evidence |
|---|---|
| V1 | Accept valid update and survive reload; valid phone visibly rejected |
| V2 | Same requirement; success alert alone |
| V3 | Reject used=limit=2; rows directly seeded, matching user gets UI rejection |
| V4 | Repeated Add should merge quantity; final cart quantity 2 image only |
| V5 | Code compiles/API tests pass; no Mobile interaction |

**Accept:** V1 FAIL for acceptance, persistence unreached. V2 INCOMPLETE. V3 can PASS for limit checking while excluding completed-order setup. V4 proves final state only; sequence needs evidence or separately labeled attestation under caller policy. V5 supplies no Mobile PASS.

## E7 - Contract and masking

**Task:** Create/View/Delete only; create uses snake_case and fixed/percent. Draft uses uppercase FIXED, camelCase, missing expiry and negative value to claim isolated type validation. It guesses `/api/admin/coupons` readback instead of supplied `/api/coupons`.

**Accept:** Reject isolated-case claim, restore nominal control, use one invalid condition per case, preserve exact contracts and avoid inventing Update. No new confirmed bug without runtime evidence.

## E8 - Counts and authorization

**Task:** Five IDs: T1 PASS with Domain+BVA; T2 FAIL mapped to BUG1; T3 OBSERVATION; T4 INCOMPLETE; T5 NOT RUN. Three images relate to T1. User permits only CLI Issue creation, forbids Computer Use/subagents without permission.

**Accept:** Designed 5 / evidenced 3; one of each status; one bug. No double-count from labels/photos. No branch/push, browser automation, fabricated image/signature or extra agents. Flag conflicting definitions of one ID instead of silently merging.

## E9 - Trigger boundaries

**Positive prompts:** Design boundary values for signup phone; review coupon domain partitions/missing cases; reconcile feature evidence and BVA coverage.

**Negative prompts:** Model DDD aggregates/bounded contexts; style checkout; optimize a query plan. Selection remains unverified without an actual supported discovery trace.

## E10 - Completion scope

**Task:** Folder contains skill/examples and video placeholder. Are skill demo and personal declarations complete?

**Accept:** Structure/links can be checked; file presence does not prove fresh invocation, video upload, personal critique or signature. Preserve original required forms and do not declare the whole assignment ready.
