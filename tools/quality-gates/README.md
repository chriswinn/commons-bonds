# tools/quality-gates/ — corpus-invariant registries + sign-off artifacts

Per pipeline doctrine §2 ([`tools/commons_bonds_pipeline_doctrine_v1.0.0.md`](../commons_bonds_pipeline_doctrine_v1.0.0.md)).

## Registries

| File | Purpose |
|---|---|
| `scaffolding-patterns.yaml` | Scaffolding-scan registry — placeholders + drafting-template scaffolding + process-scaffolding vocabulary that should never appear in publisher-facing prose. |
| `regressed-patterns.yaml` | Regressed-pattern scan registry — corpus-wide institutional memory of patterns previously fixed by rigor passes. Each entry traces back to its origin rigor-pass artifact. |

Both registries are consumed by [`tools/scripts/check-corpus-invariants.sh`](../scripts/check-corpus-invariants.sh).

## Sub-directories (output artifacts)

| Directory | Contains |
|---|---|
| `clean-baselines/` | Stage 1a invariant-gate clean-baseline verification artifacts (per Stage 1 doctrine §1.4) |
| `coherence-checks/` | Stage 1c cross-artifact coherence verification artifacts (per Stage 1 doctrine §3.3) |
| `sign-offs/` | Stage 1 + Stage 5 sign-off artifacts (per Stage 1 doctrine §4.3 + Stage 5 doctrine §2.3) |
| `render-baselines/` | Stage 1b baseline render-test artifacts + Stage 4 render-audit artifacts (per Stage 4 doctrine §3.4) |

## Schema (both registries)

```yaml
schema_version: "1.0.0"
last_updated: "YYYY-MM-DD"
registry_type: "scaffolding" | "regressed"

patterns:
  - id: <unique-id>
    pattern: '<pattern>'      # the substring / regex / word to match
    type: string | regex | word
    severity: HIGH | MEDIUM | LOW
    category: <category-tag>
    description: <human-readable description>
    origin:                    # regressed-patterns.yaml only
      pass: <origin rigor-pass>
      commit: <origin commit short-sha>
      ratified: <YYYY-MM-DD>
    allowlist:                 # per-file substantive-use exceptions
      - file: <path>
        line: <line-number>
        rationale: <why this match is legitimate>

scope:
  include: [<glob>, ...]
  exclude: [<glob>, ...]
```

## Severity tiers

- **HIGH** — block: commit / stage transition refused; author must resolve.
- **MEDIUM** — flag: surface for review; do not block.
- **LOW** — informational: log only.

## How to add a new pattern

1. Identify origin (which rigor-pass artifact + commit surfaced the pattern).
2. Add entry to the appropriate registry following the schema.
3. Verify with `tools/scripts/check-corpus-invariants.sh --verbose` that:
   - The pattern matches expected violations.
   - The pattern doesn't generate spurious matches against current corpus (or add allowlist entries for known-legitimate substantive uses).
4. Commit the registry update.

## Schema versioning

Schema version 1.0.0. Do NOT change schema without coordinating across:
- Both YAML registries (must match).
- `tools/scripts/check-corpus-invariants.sh` (parser depends on schema).
- This README + Stage 1a doctrine doc.

If schema changes are needed, bump to 1.x.0 + update all four. Treat as a versioned interface.
