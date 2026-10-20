# Sources and design decisions

Read this for provenance/source conflicts; it is not required for ordinary case design. Research was performed 2026-10-20. Links below pin the inspected repository revisions; no upstream scripts were installed/executed or copied into this package. The workflow wording and worked examples are original synthesis from project evidence and the cited principles.

## Format and test-method basis

- [Agent Skills specification](https://agentskills.io/specification): name/description, supported optional fields and progressive loading. Used as format authority when a community convention differs.
- [Agent Skills creator guidance](https://agentskills.io/skill-creation/best-practices): ground instructions in real task corrections and keep only detail that changes decisions.
- [ISTQB CTFL 4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf), sections4.2.1-4.2.4: partitioning, ordered boundaries, decision tables and state transitions. Source for technique terminology; the supplied specification and applicable project contracts govern the actual test oracle.

## Requested repositories

| Source at inspected revision | Adopted decision | Boundary of reuse |
|---|---|---|
| [affaan-m/ECC](https://github.com/affaan-m/ECC/blob/6f1881aeafa3c48f7b603cc4be4b2e4e70daad59/.agents/skills/eval-harness/SKILL.md) | Make evaluation criteria explicit and separate deterministic checks from human/model judgments. | Do not import fixed 80 percent coverage targets, generic scan commands or mandatory build steps into black-box test design. |
| [mrgoonie/claudekit-skills](https://github.com/mrgoonie/claudekit-skills/blob/80113d86bc4407f105af40a2c4ea58194f7c370a/.claude/skills/skill-creator/references/metadata-quality-criteria.md) | Use discoverable metadata and load specialized guidance only for the branch that needs it. | Its 200-character guidance is a repository convention; Agent Skills specification permits 1024. Its broad CRUD checklist cannot add operations absent from the target requirements. |
| [mattpocock/skills](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/writing-for-agents/SKILL.md) | Put conditional detail behind explicit pointers, co-locate related rules and end steps with observable completion conditions. | Do not import source workflow permissions or a mandatory background-agent pattern over the target environment restrictions. |
| [MengTo/Skills](https://github.com/MengTo/Skills/blob/398cd41c86ba42fbb30e944ae507f463648f08b7/agent-skills/codex/audit-verify-explain-grade-5/SKILL.md) | Connect an audited claim to a real artifact/check and explain the limits in plain language. | A toy demo expected-output file is not evidence that our SUT, browser or network behavior occurred. |
| [agentskills/agentskills](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/docs/specification.mdx) | Keep portable name/description frontmatter, a concise entrypoint and conditional supporting files. | Keep scripts, references and assets scoped to useful portable resources rather than copying a complete unrelated toolkit. |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/test-driven-development/SKILL.md) | Prefer observable business behavior and prove that the selected check can expose the intended discrepancy. | Do not import its implementation workflow, browser tool assumptions or optional subagent use into a design-only request. |
| [obra/superpowers](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/verification-before-completion/SKILL.md) | Tie completion statements to the actual check performed and its evidence rather than confidence. | Skill evals do not authorize independent agents or comparison runs; absent runs remain unclaimed. |

The seven source repositories were inspected, not installed as required dependencies. Patterns were selected independently; conflicting agent/tool permissions are not inherited. ClaudeKit had no SPDX license returned by the repository API at inspection, so no source text/code was redistributed from it.

## Discovery with find-skills

The skills.sh leaderboard was checked first. The following CLI searches were run successfully:

```text
npx skills find "boundary value"
npx skills find "domain testing"
npx skills find "test case design"
npx skills find "skill creator"
npx skills find "boundary value testing"
```

Two focused results were inspected beyond their search snippets:

| Result | Discovery signal at inspection | Content decision |
|---|---|---|
| [unit-test-boundary-conditions](https://github.com/giuseppe-trisciuoglio/developer-kit/blob/fe73fb33a09ee6562eeec7415a3f9a3bcf795177/plugins/developer-kit-java/skills/unit-test-boundary-conditions/SKILL.md) / [skills.sh](https://skills.sh/giuseppe-trisciuoglio/developer-kit/unit-test-boundary-conditions) | 4K installs; 360 repository stars | Java/JUnit/AssertJ-specific, not a portable black-box Domain/BVA workflow. Do not import type assertions or generic edge examples as SRS rules. |
| [boundary-value-testing](https://github.com/naodeng/awesome-qa-skills/blob/547fbcd9c417ab8afbde1cd9f18b40ecbae0333b/skills/en/testing-types/boundary-value-testing/SKILL.md) / [skills.sh](https://skills.sh/naodeng/awesome-qa-skills/boundary-value-testing) | 34 installs; 272 repository stars | Directly relevant but low adoption at inspection; reviewed as an idea source, not treated as authority. It produces candidates rather than full execution/case workflow. |

Popularity is a discovery signal, not evidence of correct testing methodology. In particular, neither a high-install Java example nor a low-install specialist overrides the supplied requirements or technique definition. No add/update command was run.

## Why the package is split

SKILL.md holds shared decisions and routing. references/ holds conditional domain, boundary, evidence, audit and helper guidance; assets/ provides a reusable output scaffold; scripts/ implements local deterministic generation and record checks; data/ holds schemas, synthetic fixtures and pinned provenance; evals/ defines agent-level acceptance scenarios; agents/openai.yaml supplies optional Codex metadata. Project-specific adapters and generated test results belong in the target project, outside the reusable package.

The conceptual workflow is usable with file tools alone. Optional helpers require Python 3.10 or newer and no third-party runtime libraries. Execution uses tools already available and authorized in the target project. Package presence does not prove discovery, independent agent evaluation, a new SUT run or human review. Exact inspected source URLs and hashes are available in [provenance.json](../data/provenance.json). No upstream implementation is redistributed as a dependency.
