---
name: domain-bva-testing
description: Apply stepwise Domain Testing and Boundary Value Analysis to a supplied feature specification, with traceable cases, actual execution, bugs and AI gap review.
---

# Domain Testing and Boundary Value Analysis

## Inputs and scope

Read the supplied feature ID/pool, versioned specification, API contract and available course lecture. List inputs, outputs, mutable state and available interfaces. Record missing rules explicitly. Follow the user's approved execution scope and human review requirements. Never invent screenshots, execution times, signatures or student discoveries. Do not use subagents or Computer Use without the user's authorization.

## Stepwise procedure

1. **Oracle:** paraphrase the exact rule and source section. Keep SRS expected independent of implementation. Record which rules are direct and which are mappings to another interface. Completion: every expected result has a rule or is an observation.
2. **Domains:** partition values, types, presence, authentication, authorization, ownership and state. Assign stable domain IDs. Hold all other dimensions nominal for one-invalid-condition tests; label deliberate interactions. Completion: each class has representative, expected and TC coverage.
3. **Boundaries:** identify ordered domains, inequality, equality status and precision. State ON and concrete neighboring values with valid/invalid labels. Enums, missing values and unspecified maxima are not invented numeric boundaries. Completion: boundary table maps to stable TC-IDs.
4. **Cases:** specify preconditions/reset, exact request or UI inputs, numbered actions, expected, postcondition and seam. Keep literal API field/enum names unchanged. Completion: a second person can reproduce without guessing account state or ellipses in payloads.
5. **Review:** compare specification, design and source hypotheses. Check masking failures, unsupported assumptions and conflicting domain/TC mappings. Preserve the original AI output and record corrections separately. Completion: no fabricated human verdict or model comparison.
6. **Execute:** use isolated fixtures and versioned source; record real timestamp, public requests/responses or genuine UI evidence, state readback and hashes. PASS/FAIL require criterion evidence; OBSERVATION is for unspecified oracle; INCOMPLETE is for missing execution/preconditions/evidence. Completion: compiler/API success never implies native UI success.
7. **Bugs:** group behavior across failed TCs. Include reproducible input/state, expected/actual, precise evidence, source-supported cause or explicit hypothesis, impact limitations and regression checklist. Completion: every failed TC maps to a bug, every counted bug has its file. Publish Issues only in the designated group stage.
8. **Audit:** reconcile unique ID counts across README/report/cases/raw evidence. Record actual tool, timestamp, prompt, output, correction and human review status. Completion: broken links, placeholders and remaining required actions are listed honestly.

## Worked feature — FR-17

- Specification: six required fields; code unique; type percent/fixed; discount_value>0; min_order_amount≥0; max_uses_per_user≥1; admin-only Create/View/Delete.
- [Analysis](../../../reports/C-FR17-domain.md): presence/enum/numeric/role classes, integer fixture neighbors and traceability.
- [Cases](../../../tests/C-FR17-coupon-management.md):30 API+6 UI IDs; [raw execution](../../../evidence/execution/C-api.md).
- Reproduce API: `node scripts/run-api.cjs C` from repository root; port3100 and copied database. Preserve the original SUT.
- [BUG-C04](../../../bugs/BUG-C04.md): C-API-12/13 are −1/0; [BUG-C06](../../../bugs/BUG-C06.md): C-API-18/19 are −1/0, with zero silently becoming1.
- UI browser rejection of maxUses0 is separate from backend acceptance. Missing after-delete evidence remains INCOMPLETE.
- [Video link](../../../Video_Links.md); do not describe an existing output as a fresh invocation.

## Outputs

One feature analysis with Domain/BVA steps, detailed cases, actual evidence, bug files and gap analysis. Keep planning/coordination notes outside the submission. Preserve exact selected AI template filenames under ai-audit/; no interactions/ directory. Documents remain Markdown; the student handles final format export.
