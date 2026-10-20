# Evaluation protocol

Use this when changing the skill or assessing transfer to another project. [evals.json](evals.json) contains 12 realistic prompts, raw input references and expected behavioral criteria. They are evaluation definitions, not recorded agent runs or product test results.

## Deterministic helper checks

From the skill directory, run:

```text
python -B scripts/test_domain_bva.py
```

The tests exercise numeric equality, exact decimal arithmetic, inclusive/exclusive and one-sided bounds, shared endpoints, traceability, invalid contracts, synthetic result-ledger mutations, overwrite refusal and portability after copying the entire skill. They use temporary directories and standard-library Python. Synthetic result statuses and `fixture://` evidence references are test inputs only.

These checks establish helper behavior, not the agent's ability to read a new specification, choose the skill, interpret screenshots or make correct review judgments. A structural/frontmatter validator is a separate packaging check.

## Agent behavior evaluation

1. Select prompts relevant to the change. Use only tools and delegation authorized in the target environment. A definition here does not authorize an independent agent, browser action, live system execution or publication.
2. Give an authorized evaluator the `prompt`, skill package and raw `files` from one eval. Paths in `files` resolve relative to the skill directory. Withhold `expected_output` and `expectations` until grading; they are the answer key.
3. Record actual model/tool identity if known, time, skill revision, source inputs, generated files and transcript. Use a scratch output area outside the installed package. Retain failed attempts.
4. Grade each explicit criterion against the produced artifact, quoting relevant case IDs, values and evidence. Record PASS/FAIL/UNASSESSABLE per evaluation criterion, separate from any product test verdicts.
5. Compare with a no-skill baseline only when both runs actually occur under comparable model/settings/input/tool conditions. Show numerator and denominator; report safety and correctness failures separately from style judgments.
6. Revise instructions only for demonstrated gaps, then rerun affected scenarios. Leave unrun criteria unclaimed. Same-session walkthroughs must be labeled as such.

The trigger prompts in eval 9 can support a static routing review. Actual automatic discovery remains unverified until the host produces an observable selection/invocation trace. Do not infer it from a well-written description or from manually opening SKILL.md.

## Coverage map

| Eval | Decision under assessment |
|---|---|
| 1 | Transfer, full boundary inventory and design-only status |
| 2 | Equality and truthful coverage denominator |
| 3 | Coupled constraints and intersections |
| 4 | Decimal precision and off-grid classification |
| 5 | Time equality and missing source rules |
| 6 | Criterion-based evidence grading |
| 7 | Public contract and validation masking |
| 8 | Unique counts, reciprocal findings and execution permission |
| 9 | Relevant versus unrelated skill routing |
| 10 | Template preservation and completion boundaries |
| 11 | Portable execution and unsupported helper scope |
| 12 | Untrusted source instructions and unresolved predicates |

## Result record

Use a real record when evaluation is performed:

| Eval ID | Skill/input revision | Evaluator/tool | Output/transcript | Criterion | Result | Evidence and limits |
|---|---|---|---|---|---|---|
| [Selected ID] | [Actual revisions] | [Known identity or unknown] | [Actual artifact] | [One criterion] | [PASS/FAIL/UNASSESSABLE] | [Observed facts] |

No independent agent evaluation outcomes are shipped in this package. The installed helper tests can be rerun to establish current deterministic results; do not treat an old successful run as verification of a later edit.
