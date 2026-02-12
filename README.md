# Codex Skills Vault

Curated Codex skills for structured, repeatable workflows.

## Overview

This repository hosts reusable Codex skills. Each skill lives in its own folder under `skills/` and contains the required `SKILL.md` plus any optional resources (scripts, references, assets) used to make workflows consistent and reviewable.

## Repository Layout

```
codex-skills-vault/
├── README.md
└── skills/
    └── atomic-execution-engine/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        ├── assets/
        ├── references/
        │   └── review-cycle.md
        └── scripts/
            └── slugify_unit.py
```

## Included Skills

| Skill | Description | Resources |
| --- | --- | --- |
| `atomic-execution-engine` | Converts high-level implementation plans into sequential, coherent PRs with one unit per PR. | `scripts/slugify_unit.py`, `references/review-cycle.md` |

## Quick Start

1. Install via OpenAI Skill Installer:
   - `scripts/install-skill-from-github.py --repo cangiremir/codex-skills-vault --path skills/atomic-execution-engine`
2. Or copy a skill folder into your Codex skills directory.
3. Ensure each skill has a `SKILL.md` with `name` and `description` frontmatter.
4. (Recommended) Provide `agents/openai.yaml` for UI metadata.

## Adding New Skills

- Use short, hyphenated names (e.g., `plan-executor`).
- Keep `SKILL.md` concise and procedural.
- Move long reference material into `references/`.
- Only add `scripts/` and `assets/` when they add concrete value.

## License

Licensed under the MIT License.
