# Portable helpers and data contract

Read this when using the bundled Python helpers. The conceptual workflow supports arbitrary domains; the deterministic generator deliberately supports a smaller, explicit contract. Use Python 3.10 or newer. Runtime and tests use the standard library, perform no network requests and do not invoke a SUT, browser or shell command.

## Run from any location

The following commands assume the skill directory is the working directory. From elsewhere, use absolute paths to both script and input. Paths supplied to the CLI are relative to the caller's working directory; there is no dependency on a repository name, ancestor directory or installed skill path.

```text
python scripts/domain_bva.py validate data/examples/parcel.json
python scripts/domain_bva.py generate data/examples/parcel.json --output /path/to/new-design
python scripts/domain_bva.py audit data/examples/results.json
python -B scripts/test_domain_bva.py
```

Replace `/path/to/new-design` with a new local directory, such as `C:\Temp\parcel-design` on Windows or `/tmp/parcel-design` on Linux. Generation refuses an existing destination, including an empty directory. A validation error returns exit code 2 before creating output; a filesystem error may leave partial output in the newly created directory. Inspect that directory before retrying with a new destination. Exit code 0 means the requested helper operation completed, not that a product passed its tests.

`validate` checks design inputs. `generate` validates first, then writes `cases.json` and `design.md`. `audit` reads a separate result ledger and prints its consistency summary. The helpers never modify the input file. Copy the whole skill directory to reuse it; the optional Codex UI metadata is in [openai.yaml](../agents/openai.yaml). Installation/discovery follows the target agent's skill mechanism.

## Design specification v1

Use [spec.schema.json](../data/spec.schema.json) for editor/schema validation and `validate` for additional semantics. Start with one of the [sample inputs](../data/examples/parcel.json). Reject unknown keys rather than silently ignoring unsupported constraints.

| Field | Meaning |
|---|---|
| `schema_version` | Integer 1 |
| `feature` | Stable `id` and human-readable `title` |
| `rules` | Unique `id`, versioned `source`, exact `requirement` text |
| `fixture` | `actor`, `interface`, `initial_state`, `setup`, `action`, `readback`, all nonempty text |
| `bva` | `2-value` or `3-value`, defined below |
| `dimensions` | 1-100 independent numeric or enum dimensions, each with a unique `name`, valid `nominal` and known `rule_ids` |

Identifiers start with an ASCII letter, followed by up to 63 ASCII letters, digits, underscores or hyphens. Rule text is carried through verbatim; the helper does not interpret natural language or prove that dimension constraints correctly encode it. Every rule must map to a modeled dimension; keep unsupported rules in the manual analysis instead of hiding them in this machine input.

### Integer and decimal dimensions

Supply `kind`, `unit`, `origin`, `step`, `nominal`, `rule_ids` and at least one of `minimum`/`maximum`. Each bound is an object with `value` and Boolean `inclusive`. The model's universe is the unbounded lattice `origin + k * step`, with integer `k`. A missing lower/upper bound stays unbounded in this model; this does not invent a missing product limit.

- Store numeric values as plain decimal strings, including integers. JSON floats, exponent notation, NaN and infinity are rejected. Up to 48 characters and 18 fractional digits are accepted; declared numeric magnitudes are limited to `10^24`. Arithmetic uses exact rational values, with exact decimal output.
- `integer` requires step `1` and origin `0`. `decimal` requires a positive, explicitly justified step and explicit origin. The helper cannot decide the correct precision for the source requirement.
- Thresholds and nominal values must align with the lattice. Exclusive bounds shift the first/last valid grid point by one step. A nonaligned threshold requires manual analysis or a justified preprocessing decision; it is never rounded silently.
- The nominal value must satisfy all declared bounds. This also rejects reversed bounds and intervals containing no valid lattice points.

For each transition between adjacent invalid/valid ordered partitions, the helper records both endpoints. For integer acceptance `[10,11]`, these are `9,10,11,12`. `2-value` includes those endpoints; `3-value` includes every endpoint and both neighbors, yielding `8,9,10,11,12,13`. Shared points are deduplicated while retaining coverage mappings. A one-sided bound creates only that transition; no fictitious other endpoint is added.

### Enum dimensions

Supply string `valid_values`, a valid string `nominal`, `rule_ids`, and optional explicit string `invalid_values`. Values must be unique and valid/invalid lists disjoint. All supplied representatives are selected. No invalid code is invented, and an empty `invalid_values` list does not demonstrate invalid-class coverage. Enum values have no numeric BVA inventory.

### Generator output and limits

The output contains a valid nominal control and one-dimension-at-a-time candidates. Nominal controls reused by several inventories receive all applicable coverage mappings. Each case contains complete logical dimension values, technique labels, domain classification and violated rule IDs, with `status=NOT RUN`, `actual=null` and empty `evidence`. Do not import these logical strings as production HTTP payloads without applying the actual field types.

`domain_valid` means satisfaction of the modeled constraints. It is not an exact status code, error message, transaction result, full acceptance oracle or executed verdict. The common fixture and rule ledger are included; complete per-case steps and sourced response/postcondition expectations using [feature-record.md](../assets/feature-record.md) or the caller's template.

Handle these manually using the conceptual references:

- Missing/null/empty/whitespace and transport coercion; numeric off-grid and wrong-type probes.
- Unicode length/normalization, regex languages and semantic format classes.
- Cross-field arithmetic, arbitrary predicates, permissions, state transitions and decision-table interactions.
- Date/time equality, clock control, timezone and daylight-saving changes.
- Postconditions, persistence, mutable setup/reset and execution evidence.

No expression evaluator or arbitrary code execution is provided. More complex models should retain explicit predicates and reproducible points in Markdown rather than pretending the helper covers them.

## Result ledger v1

Use [results.schema.json](../data/results.schema.json). The [synthetic example](../data/examples/results.json) exercises the auditor only; its `fixture://` references are deliberately not real evidence. Never insert it into a project's execution results.

The top level contains `schema_version`, known `rule_ids`, the independent `designed_case_ids` inventory, detailed `cases`, and `findings`. Every case needs `id`, `status`, `rule_ids`, sourced `expected`, `actual`, `evidence`, `reason`, and `finding_ids`. Evidence entries are nonempty reference strings, not attachments. A finding contains unique `id` and nonempty `case_ids`.

The auditor checks:

1. Exact agreement between designed inventory and unique case records; known rules and supported statuses.
2. `NOT RUN` has null actual and no execution evidence/findings.
3. `PASS`, `FAIL` and `OBSERVATION` have actual text and evidence references; `INCOMPLETE` can have partial actual/evidence and needs an explanatory reason.
4. Every `FAIL` has at least one finding; other statuses do not map to confirmed defect findings in this ledger. Track exploratory observations separately.
5. Reciprocal case/finding links, without orphan findings or duplicate IDs.
6. Unique-case totals, per-status counts and distinct finding counts. Multiple failed cases can map to one finding.

The helper preserves caller-supplied verdicts; it does not choose them. A successful audit establishes record consistency only. Evidence existence/content, oracle correctness and completeness of the declared design inventory still need review. The summary labels the evidenced-case total as `executed_with_sufficient_evidence_claimed` for this reason.

## Adapting the package

Keep project paths, credentials, real data, account history and rubric rules in the target project's adapter or test basis. Bind this skill through explicit source links and interface mappings. Preserve a supplied output schema rather than overwriting it with these convenience schemas. Write generated artifacts to the requested work area, outside the installed skill directory. The bundled data should remain stable synthetic fixtures for reuse and regression checks.
