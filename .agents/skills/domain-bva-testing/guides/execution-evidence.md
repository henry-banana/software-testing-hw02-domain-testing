# Execution and evidence

Read before exercising an authorized SUT or grading supplied records. Environment/evidence must match the intended interface and initial state.

## Before execution

1. Identify the versioned SUT, checkout and pre-existing changes. A dirty checkout is not pristine.
2. Inspect startup/seed behavior before importing modules or starting servers. Use a disposable copy/database when startup resets data.
3. Match actor, role, ownership, clock and counters. Record setup method and a control object for destructive operations.
4. Choose an observable interface proving the rule. API cases can use HTTP; a UI criterion still needs that UI.
5. Check authorization/tool availability. Browser/device automation, subagents and external publication need the required user authorization. Continue independent authorized work while a dependent action is blocked.

Separate setup/cleanup from the measured action. Do not reset a fixture if that would erase another tester's evidence; isolate instead.

## Execution record

Record case ID, run/attempt ID, source version, environment, real observation time, simulated clock if any, setup facts, exact action/request, actual output, relevant readback and evidence paths.

Keep credentials out of captured logs. Placeholder authentication headers can document the contract, but identity/role setup must remain reproducible. Capture errors and successes; explain redactions without changing business values.

A readback collected after a screenshot supports the later observed state. It does not establish the state at the exact screenshot moment. Name this timing limit.

## Evidence strength

| Evidence | Supports | Does not independently support |
|---|---|---|
| Source inspection | Implementation mechanism/test hypothesis | Runtime outcome or business oracle |
| Build/runner startup | The checked environment action | Unrun cases or UI behavior |
| Raw HTTP response | That request's API result | Frontend validation or device interaction |
| Public readback | Observed persisted state | An unobserved sequence producing that state |
| UI input plus rejection | Displayed input blocked at that step | Backend behavior if client never sent it |
| Success alert alone | A message was displayed | Save-and-reload/fresh-login persistence |
| Final cart/list image | Visible final state | Exact Add/Create/Delete sequence |
| Human statement | Claimed action sequence | Independent replay/machine-recorded trace |
| Issue header image | Visible title/number/status/metadata | Lower Steps/Expected/Actual or attachments |
| Issue API readback | Publication content/identity/URL at that time | Screenshot of the GitHub page |

## Criterion-based verdicts

For valid-update acceptance and persistence:

- Valid input rejected: FAIL for acceptance; persistence was unreached.
- Success alert without readback: INCOMPLETE for the full criterion.
- Exact values after reload/fresh login: PASS for the specified persistence scope.

For usage limits, `used=limit` setup plus observed rejection can satisfy limit checking. If rows were seeded directly, do not claim completion of prior orders end to end.

For sequences, distinguish final-state from sequence evidence. If student attestation is accepted under the caller's evidence policy, record it and its limits instead of calling it independently replayed.

Observed behavior with an unspecified oracle can be OBSERVATION. An unexecuted exploratory candidate stays NOT RUN. Missing infrastructure/fixture produces an environment/incomplete result, not product FAIL.

## Image provenance

Inspect images before assigning IDs. Match visible account, values, URL, object IDs and response; filenames/capture order alone are insufficient.

Keep original bytes when renaming. Record old/new name, SHA-256, case/bug/Issue mapping, visible facts and limits. File modification time is not execution time. Image count is not case count.

Shared images can support several cases only when facts and any separate attestation support each criterion. Do not imply independent runs or create duplicate IDs from repeated evidence.

## External publication

When Issues are authorized, prepare complete bodies, check duplicates, create/update only the designated repository and read results back. An Issues-only permission does not authorize evidence branches, commits, repository-file uploads or pushes.

After CLI create/readback, track publication separately from attachments/page images. Use genuine screenshots; do not render synthetic terminal/page images as captured UI.

## Bounded retries

Retain failed attempts. Retry transient errors only while fixture/version remain comparable. Stop when a recurring external blocker has no new hypothesis or a retry exceeds scope/affects unrelated state. Explain partial evidence rather than changing the target criterion.

A later valid run can resolve an incomplete case while retaining the old attempt. It is not a new designed case unless its input/criterion changes and receives a new ID.
