# Vercel environment variables (org canonical)

Applies to **all** LakeHouse templates (`Template-LakeHouse-Monorepo`, `Template-LakeHouse-Sandbox`, `Template-LakeHouse-Widget`, `Template-LakeHouse-OpenSource`) and their descendants. ZERO COST. Agents must not mutate Vercel env vars without Sen’s explicit approval - see [AGENTS.md](../../AGENTS.md) **Never do**.

## Shared vs project

| Scope | When |
| --- | --- |
| **Team Shared Environment Variables** | Value applies to **more than one** Vercel project → define once at the team, **link** into each project. |
| **Project env** | Value is **project-specific** only (unique URL, project id, per-app flag). |

Do not duplicate the same secret across projects as separate project-level copies when a shared variable can be linked.

## Naming convention

- **`UPPER_SNAKE_CASE`** only.
- Prefix by **domain or service**: `LAKEHOUSE_*`, `WIDGET_*`, `DOCS_*`, `AUTH_*`, etc. (brand/service - not the GitHub org login).
- **`NEXT_PUBLIC_`** (or the framework’s public prefix) **only** for values that are truly public in the browser bundle. Never put tokens, private keys, or webhook secrets behind a public prefix.
- Prefer descriptive names over abbreviations that only one person understands.

Examples (names only): `LAKEHOUSE_API_BASE_URL`, `NEXT_PUBLIC_DOCS_SITE_URL`, `AUTH_OIDC_CLIENT_ID`.

## Environments

| Environment | May use production secrets? | Notes |
| --- | --- | --- |
| **Production** | Yes (production values) | Linked shared vars + project-specific prod values |
| **Preview** | **No** | Non-prod / staging credentials only |
| **Development** | **No** | Local/dev credentials only |

Preview and Development must never point at production databases, payment keys, or live third-party secrets.

## Local development

```bash
# From a linked project directory (Sen or approved operator)
vercel env pull .env.local
```

- Writes **`.env.local`** (or the path you pass).
- **`.env*` is always gitignored** and never committed.
- Secret scanning (gitleaks workflow template) treats committed env files as deny-list failures - do not “fix” by renaming.

## Prefer OIDC over long-lived tokens

- Use **Vercel OIDC federation** (and other OIDC/trusted-publishing paths) instead of long-lived cloud keys or `VERCEL_TOKEN`-style secrets in CI when the platform supports it.
- Prefer short-lived, scoped credentials. Document any unavoidable long-lived secret in the [secrets inventory](secrets-inventory.template.md) with a short rotation cadence.

## Agents / automation

Without Sen’s **explicit** in-band approval, do **not**:

- Create, edit, or delete Vercel environment variables (UI, API, or CLI).
- Run `vercel env add`, `vercel env rm`, or equivalent.

Reading docs and drafting inventory **names** is fine. Pulling env locally is only for machines Sen has already linked.

## Related templates

- Inventory (names only): [secrets-inventory.template.md](secrets-inventory.template.md)
- Rotation checklist: [secrets-rotation-checklist.md](secrets-rotation-checklist.md)
- Important credentials live in the **owner’s vault** (Sen’s Google Drive) - never copy values into git.
