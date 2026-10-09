# Secrets inventory template (names only)

Copy into a **private** tracking location Sen controls (or a private note). **Never commit real values.** Cells hold **names and metadata only**.

Important credentials: store values in the **owner’s vault** (Sen’s Google Drive); this inventory only references that as the source of truth.

## Inventory

| Name | Scope (`shared` / `project`) | Linked projects (or `n/a`) | Environments (`Production` / `Preview` / `Development`) | Owner | Source of truth | Rotation cadence | Last rotated (YYYY-MM-DD) | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EXAMPLE_API_KEY` | shared | project-a, project-b | Production | Sen | owner’s vault | 90d | 2026-01-15 | Linked team shared var |
| `EXAMPLE_PREVIEW_API_KEY` | shared | project-a, project-b | Preview, Development | Sen | owner’s vault | 90d | 2026-01-15 | Non-prod only |
| `NEXT_PUBLIC_SITE_URL` | project | project-a | Production, Preview, Development | Sen | repo docs / Vercel | n/a (public) | — | Public URL; not a secret |

## Rules

1. One row per **name** (+ environment split if prod vs non-prod use different names).
2. Scope **`shared`** when the value is a Vercel team Shared Environment Variable linked to multiple projects.
3. Scope **`project`** only for project-specific values.
4. Preview/Development rows must not reuse production secret **names** that hold prod material — use distinct non-prod names.
5. If OIDC replaces a secret, mark the old name `retired` in Notes and set Last rotated when removed from Vercel.

## Pointers

- Policy: [vercel-env.md](vercel-env.md)
- Rotation steps: [secrets-rotation-checklist.md](secrets-rotation-checklist.md)
