# EShop FR-17: worked feature and HW02 adapter

Use only for CSC13003 HW02 or to understand the workflow through a concrete example. The generic skill does not require these paths, ports or homework forms.

## Existing evidence, not a new run

This example reuses [FR-17 analysis](../../../../reports/C-FR17-domain.md), [detailed cases](../../../../tests/C-FR17-coupon-management.md) and [raw API execution](../../../../evidence/execution/C-api.md). Reading it is not a fresh skill invocation, SUT rerun, independent review or completed video demonstration.

Baseline: `85af3ba875c88283615e22cb108f13e2fccaf0e9`. The tested checkout also had a root `.gitignore` commit; source comparison and fixtures are recorded in the reports.

## Oracle and scope

FR-17 explicitly requires Create, View and Delete. Do not infer Update from the word CRUD.

Baseline contracts:

- Create: `POST /api/admin/coupons`.
- View: `GET /api/coupons`.
- Delete: `DELETE /api/admin/coupons/:id`.
- UI: Admin coupon-management screen.

The selected SRS requires `code`, `type`, `discount_value`, `min_order_amount`, `expired_at`, `max_uses_per_user`; unique code; type `fixed`/`percent`; `discount_value > 0`, `min_order_amount >= 0`, `max_uses_per_user >= 1`. Test admin-only operations separately from numeric rules. Read the [SRS](https://github.com/ttbhanh/eshop-sut/blob/85af3ba875c88283615e22cb108f13e2fccaf0e9/README.md) and local analysis for exact mappings.

`discountValue`, `expiryDate` and uppercase `FIXED` are different inputs, not report-format variants.

## Nominal create fixture

Authenticate as admin and choose a unique code:

```json
{
  "code": "SKILL_FR17_CONTROL",
  "type": "fixed",
  "discount_value": 1,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

A future replay must establish absence of this code or reset only its disposable fixture. Do not import original `database.js` to do that: it drops/seeds tables. The recorded API suite used a copied backend/database on port3100; a new run must record its own environment.

## Domain decisions

| Dimension | Classes | Representative strategy |
|---|---|---|
| Presence | Each required field absent/present | Remove one field from a complete control |
| Code | Unique, duplicate, empty, unresolved normalization | Establish existing control before duplicate probe |
| Type | fixed, percent, outside enum | Keep numeric/date/actor inputs nominal |
| Discount | Positive, zero, negative | Integer fixture neighbors, without integer-only SRS assumption |
| Minimum order | Nonnegative, negative | Keep discount positive and usage nominal |
| Usage limit | >=1, zero, negative | Distinguish rejection from silent default |
| Actor | Admin, user, missing/invalid authentication | Check each operation separately |
| Lifecycle | Existing/deleted target and control object | Record ID and before/after readback |

Retain stable domain IDs from the linked analysis; do not renumber them here.

## Selected probes and recorded results

| Rule | Fixture points | Traceability | Recorded result |
|---|---|---|---|
| discount_value > 0 | -1,0,1 | C-API-12/-13 and nominal valid cases | -1/0 created; [BUG-C04](../../../../bugs/BUG-C04.md) |
| min_order_amount >= 0 | -1,0,1 | C-API-15 and valid neighbors | Negative minimum persisted; [BUG-C05](../../../../bugs/BUG-C05.md) |
| max_uses_per_user >= 1 | -1,0,1,2 | C-API-18/-19 and valid neighbors | -1 persisted; 0 became 1; [BUG-C06](../../../../bugs/BUG-C06.md) |
| User cannot Create/View/Delete admin coupons | User vs admin control | C-API-23/-26/-29 | [C07](../../../../bugs/BUG-C07.md), [C08](../../../../bugs/BUG-C08.md), [C09](../../../../bugs/BUG-C09.md) |

These are existing selected probes, not complete 3-value coverage of every possible partition/type.

## One complete bug path

1. Rule: discount value must be positive.
2. Domain: zero/negative invalid; other required fields and actor remain valid.
3. Cases: C-API-12 uses -1; C-API-13 uses 0. Preserve that order.
4. Execution: historical raw record holds exact request/response.
5. Readback: invalid created value appears in the public list.
6. Verdict: FAIL for invalid persistence, not a guessed status mismatch.
7. Bug: BUG-C04 groups the validation behavior and links cases/UI evidence.
8. Publication: the bug file links the actual group Issue; [Issue evidence](../../../../evidence/github-issues/README.md) states image coverage.

## UI evidence and limits

Existing feature scope is 30 API and 6 UI case IDs. Read current verdicts rather than importing counts from an older AI snapshot.

A shared Admin list image supports C-UI-02/C-UI-06 with explicit student action/reload clarification. It shows retained valid coupon, absent deletion target and control coupon. Keep clarification separate from visible pixels; do not call this independently replayed. Client rejection does not prove backend validation.

## Local output and authorization rules

- Keep documents Markdown; the student exports PDF/ZIP.
- Preserve selected original AI-template filenames and structure under `ai-audit/`; fill fields without replacing questions/declarations.
- Keep working scripts/research/task coordination outside the submission. This package has no executable helper dependency.
- Respect the explicit restriction on subagents and Computer Use. Terminal/file access is not browser authorization.
- Group repository permission was Issues only: no evidence branch or file push.
- Preserve genuine images, raw values, timestamps and hashes; never fabricate personal review/signature.
- Use the user's plain-punctuation convention in authored Markdown.

[Video_Links.md](../../../../Video_Links.md) states the demonstration URL status. Instructions/examples do not prove recording or upload.

For another feature, supply its own versioned rules and fixture, then use fresh IDs/evidence. These FR-17 records remain historical examples.
