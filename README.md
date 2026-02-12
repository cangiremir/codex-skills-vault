# Codex Skills Repository

A general-purpose repository for curated Codex skills. Each skill lives in its own folder under `skills/` and contains the required `SKILL.md` plus any optional resources (scripts, references, assets) needed for repeatable workflows.

## Repository Structure

```
skills-repo/
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

## Skills

### atomic-execution-engine
Converts high-level implementation plans into sequential, coherent PRs with one unit per PR, enforcing a review cycle before progressing to the next unit.

**Key workflow guarantees**
- One coherent unit per PR; no unrelated batching.
- Required Codex review loop until no valid suggestions remain.
- Finalize PR only after CI/tests pass and the unit is coherent.

**Bundled resources**
- `skills/atomic-execution-engine/scripts/slugify_unit.py`: Generates `codex/<unit-slug>` branch names from unit titles.
- `skills/atomic-execution-engine/references/review-cycle.md`: Checklist for handling review suggestions.

## Adding New Skills

1. Create a new folder under `skills/<skill-name>`.
2. Add `SKILL.md` with required YAML frontmatter (`name`, `description`).
3. Add `agents/openai.yaml` with UI metadata.
4. Add optional `scripts/`, `references/`, or `assets/` as needed.

## Usage Notes

- Keep `SKILL.md` concise and procedural; move long reference material into `references/`.
- Only include optional folders when they add concrete value.
- Avoid unrelated batching within a single skill.

## License

Licensed under the MIT License.
