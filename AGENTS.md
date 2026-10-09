# LakeHouse - agent & human house rules

Org-wide defaults. Current GitHub `orgName`, `brand`, `packageScope`, and public `domain` are defined in [`.lakehouse/org.json`](.lakehouse/org.json). Action / reusable-workflow pins: [`.lakehouse/pins.json`](.lakehouse/pins.json).

Epics live in [SenZhang-Plus/SenZhang-Todo](https://github.com/SenZhang-Plus/SenZhang-Todo), not GitHub Issues. Sen is the sole owner who reviews and merges; there is no second owner and no auto-archive.

`CLAUDE.md` imports this file - keep rules here.

## Org decisions

| Topic | Decision |
| --- | --- |
| Cost | **ZERO COST** - GitHub Free only (no Team, no paid Secret Protection) |
| Public runners | GitHub-hosted only |
| Private runners | Self-hosted only |
| Public + self-hosted | **Never** |
| Merge method | **Merge commits only** (never squash or rebase-merge) |
| Epics | SenZhang-Plus/SenZhang-Todo |
| Templates | Four: `Template-Monorepo`, `Template-Sandbox`, `Template-Widget`, `Template-OpenSource` - see [docs/naming.md](docs/naming.md) |
| Org defaults | This `.github` / `defaultsRepo` repository |
| Disposable private | `sandbox-*`, `legacy-*` |
| Public widgets | From **Template-Widget** - plain names; LakeHouse host extensibility |
| Public OSS | From **Template-OpenSource** - plain names; **no** widget concepts |
| Package scope | Brand-based from `org.json` (`packageScope`) - **not** the org login; widgets use `@lakehouse/widget-sdk` |
| Public links | Custom `domain` from `org.json` - **never** `*.github.io` |
| Retired names | See [retired-names.txt](retired-names.txt) - do not reuse (`Template-OpenSource` is **active**, not retired) |
| Org rename | [docs/org-rename-runbook.md](docs/org-rename-runbook.md) |

Settings only Sen changes in the GitHub UI: [docs/sen-only-github-settings.md](docs/sen-only-github-settings.md).

## Merge queue

- Canonical policy: [docs/merge-queue.md](docs/merge-queue.md).
- **Public** repos: require merge queue on `main` (Free plan allows public org repos only). Merge method = **merge commit**.
- **Private** repos: no queue on Free - manual merge commits + up-to-date + green CI.
- Required CI workflows must include `merge_group:` (in addition to `pull_request` with no branches filter).
- Agents **never enqueue or merge** PRs (including merge queue). Sen does.

## Stacked PRs

- Prefer small stacked PRs; each branch is based on the previous feature branch.
- List the full stack in every PR body (position, parent, children).
- Merge **bottom-up** with **merge commits**, then retarget the next PR to `main` and (on public repos) Sen enqueues it.
- Recommended zero-cost tool: **`git rebase --update-refs`** (Git 2.38+). See [CONTRIBUTING.md](CONTRIBUTING.md).
- CI: `on.pull_request` with **no `branches` filter**, plus `merge_group` for the queue.
- Rulesets that require PRs must **not** block stacked PRs into feature branches.
- Exception: senzhang-todo-style ledger/data edits may go straight to `main`.

## Changelog

- Keep a Changelog with **Unreleased**.
- pnpm repos: changesets under `.changeset/`.
- Each PR touches CHANGELOG/changeset **or** has `skip-changelog`.

## Org identity (rename-safe)

- Read `orgName` / `brand` / `packageScope` / `domain` from `.lakehouse/org.json`.
- In GitHub Actions runtime steps, prefer `${{ github.repository_owner }}` over hardcoding the login.
- Reusable workflow `uses:` strings must be literals - copy the owner from `org.json` / pins when calling from other repos, and update them during rename (see pins.json + runbook).
- CI **org-name-lint** fails if the org login is hardcoded outside the allowlist.

## Never do

Agents and contributors must **never**:

1. **Change visibility** of any repository (public ↔ private).
2. **Change org/repo settings, rulesets, or secrets** (Sen-only in the GitHub UI / approved channels).
3. **Force-push** to any branch on `origin` (including “their” feature branches on shared remotes when policy forbids it - default: no force-push to org remotes).
4. **Delete or rename** repositories, branches, or tags.
5. **Merge** into `Template-*` or `.github`, or **enqueue** PRs on the merge queue (Sen merges / enqueues those).
6. **Vendor** shared code (copy-paste org libraries into repos); consume shared packages (e.g. `@lakehouse/widget-sdk`) or templates instead.
7. **Push to an unexpected remote** (only the repo’s configured `origin` for this org / the intended fork; never add or push to unrelated remotes).
8. **Hardcode the GitHub org login** in workflows, badges, or docs (use `org.json` or `github.repository_owner`; allowlisted files only for historical/rename notes).
9. **Create, edit, or delete Vercel environment variables** (UI, API, or `vercel env add` / `vercel env rm`) without Sen’s **explicit** in-band approval. Shared vs project rules: [docs/deploy/vercel-env.md](docs/deploy/vercel-env.md).

## Scripts

- Repo scripts under `scripts/` are **cross-platform Node `.mjs`** (Sen develops on Mac and Windows).
- Do **not** add bash `.sh` (or Python) scripts for house tooling - use `node scripts/….mjs`.
- Examples: `node scripts/org-name-lint.mjs`, `node scripts/check-pins.mjs`, `node scripts/create-release-tag.mjs`, `node scripts/copy-lint.mjs`.
- Exception: `brand/build_*.py` are brand-kit tooling (Python), not general repo automation.

## Deploy / Vercel env

- Canonical rules: [docs/deploy/vercel-env.md](docs/deploy/vercel-env.md).
- Multi-project values → **team Shared Environment Variables** (linked); project-only values stay on the project.
- Inventory (names only) + rotation: [docs/deploy/secrets-inventory.template.md](docs/deploy/secrets-inventory.template.md), [docs/deploy/secrets-rotation-checklist.md](docs/deploy/secrets-rotation-checklist.md).
- Important credential values live in the **owner’s vault** - never in git.

## Releases

- Follow [docs/releasing.md](docs/releasing.md). Draft releases first; Sen publishes.
- Only CI creates release tags (`create-release-tag.mjs`). Never tag releases by hand.
- npm via **OIDC trusted publishing** (no long-lived tokens). Immutable releases = Sen-only UI setting.

## Brand & discoverability

- Brand kit **v0.3**: [`brand/`](brand/) (`BRAND.md`, `DESIGN-SYSTEM.md`, `WRITING-STYLE.md`, `tokens.json`, `final/`).
- Locked: L1 mark; Geist / Geist Mono; dark only on grey ramp `#161616` / `#1E1E1E` / `#262626` / `#2E2E2E` / `#383838`; accent `#7DFFFF`; tagline *A second home for your design practice.* Default theme only; semantic skins are a higher layer.
- Brand tooling (not CI): `python brand/build_tokens.py` and `python brand/build_logos.py`.
- Writing: [brand/WRITING-STYLE.md](brand/WRITING-STYLE.md). **No em dashes or en dashes.** Avoid banned hype words (§7). Run `node scripts/copy-lint.mjs`.
- Follow [docs/discoverability.md](docs/discoverability.md) for README/topics/pins/profile.
- Docs site decision: [docs/docs-site.md](docs/docs-site.md) (Astro Starlight on custom domain).

## Contributors

- Friendly path: [CONTRIBUTING.md](CONTRIBUTING.md), [GOVERNANCE.md](GOVERNANCE.md), [docs/maintainer-playbook.md](docs/maintainer-playbook.md).
- Never run fork PR code on self-hosted runners; never `pull_request_target` + checkout of PR head.
- Seed `good first issue` / `help wanted` per [docs/starter-issues.md](docs/starter-issues.md).

## Allowed defaults for agents

- Open **draft** PRs; leave merge to Sen for protected/template/org-default repos.
- Use workflow templates under `workflow-templates/` with actions **pinned by SHA** (from `.lakehouse/pins.json`), least-privilege `permissions:`, and the correct runner tier.
- Sync labels via the reusable `label-sync` workflow; labels must exist in each target repo.
- For public repos: DCO `Signed-off-by` on commits.
- Prefer merge commits when merging is explicitly allowed by Sen.

## Security & secrets

- No secrets or client content in issues, PRs, logs, or artifacts.
- Report vulnerabilities via GitHub **private vulnerability reporting** ([SECURITY.md](SECURITY.md)).
- Do not enable or depend on paid GitHub Secret Protection; use free scanning (e.g. gitleaks CLI in CI) only.
