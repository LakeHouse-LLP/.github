# Contributing

Thanks for contributing. Read [AGENTS.md](AGENTS.md) for org house rules and the **Never do** list. Sen reviews and merges; do not merge into `Template-*` or `.github` yourself.

Current org login, brand, package scope, and public domain: [`.lakehouse/org.json`](.lakehouse/org.json). Pins: [`.lakehouse/pins.json`](.lakehouse/pins.json).

## Org constraints (summary)

- **ZERO COST** — GitHub Free plan only (no Team, no paid Secret Protection).
- **Runners** — Public repos: GitHub-hosted only. Private repos: self-hosted only. Never put self-hosted runners on public repos.
- **Merges** — Merge commits only. Never squash or rebase-merge on GitHub.
- **Epics** — Live in [SenZhang-Plus/SenZhang-Todo](https://github.com/SenZhang-Plus/SenZhang-Todo), not GitHub Issues.
- **Naming** — `Template-Monorepo`, `Template-Sandbox`, `Template-OpenSource` are templates; this defaults repo holds org defaults; `sandbox-*` / `legacy-*` are private disposable; open-source repos use plain names. See [retired-names.txt](retired-names.txt).
- **Identity** — Do not hardcode the GitHub org login. Use `.lakehouse/org.json` or `${{ github.repository_owner }}`. See [docs/org-rename-runbook.md](docs/org-rename-runbook.md).

## Stacked PRs

Prefer **small stacked PRs**: each branch is based on the previous feature branch (not always on `main`).

1. Open PR 1: `feature/a` → `main`.
2. Open PR 2: `feature/b` → `feature/a` (and so on).
3. In **every** PR body, fill the **Stack** section (position, parent PR, child PRs).
4. **Merge bottom-up** with a **merge commit** (never squash/rebase-merge).
5. After the base PR merges, **retarget** the next PR to `main` (or the new base), then merge.

### Recommended tool: `git rebase --update-refs`

Built into Git (2.38+) — zero cost, no extra service:

```bash
# While on the tip of the stack, after updating an earlier commit:
git rebase --update-refs main

# Or interactively, keeping dependent branches moving with you:
git rebase -i --update-refs main
```

Workflow sketch:

```bash
git checkout -b feature/1 main
# ... commit ...
gh pr create --base main

git checkout -b feature/2 feature/1
# ... commit ...
gh pr create --base feature/1
# Edit PR body Stack section.

# After review of feature/1: merge with merge commit on GitHub.
git checkout feature/2
git fetch origin
git rebase --update-refs origin/main
# Retarget PR 2 to main, then merge with merge commit.
```

Alternatives (also fine if you already use them): [git-spr](https://github.com/ejoffe/spr), [ghstack](https://github.com/ezyang/ghstack), Graphite free CLI. Prefer one tool per stack and keep the Stack section accurate.

### CI and rulesets for stacks

- CI must run on `pull_request` **with no `branches:` filter**, so PRs into feature branches still get checks.
- Org/repo **rulesets that require PRs must not block** stacked PRs whose base is a feature branch (require PRs into `main` / protected defaults only, or allow the stack pattern Sen configures).

### Exception

Ledger / data edits in the style of **senzhang-todo** may go **straight to `main`** when that repo’s process says so (no stack required).

## Changelog

- Follow [Keep a Changelog](https://keepachangelog.com/). Keep an **Unreleased** section.
- **pnpm** monorepos: also use [changesets](https://github.com/changesets/changesets) under `.changeset/`.
- Every PR must either:
  - touch `CHANGELOG.md` and/or add a changeset, **or**
  - carry the `skip-changelog` label.
- The `changelog-check` workflow template enforces this.

## Org name lint

PRs must not introduce hardcoded GitHub org login strings outside the allowlist (see `.lakehouse/org-name-lint-allowlist.txt`). Run locally:

```bash
node scripts/org-name-lint.mjs
node scripts/check-pins.mjs
```

## Pull requests

Use the org PR template. Checklist highlights:

- CI green on the PR (including when base is a feature branch).
- CHANGELOG / changeset or `skip-changelog`.
- No secrets or client content.
- Docs / README updated when behavior changes.
- **DCO sign-off** (`Signed-off-by:`) on commits for **public** repos.
- Merge with a **merge commit** only.

## Issues

Use the YAML issue forms (bug / feature / docs). Blank issues are off; questions go to **Discussions**. Labels are defined in [`.github/labels.yml`](.github/labels.yml); sync them into each repo with the reusable [label-sync](.github/workflows/label-sync.yml) workflow.

## Code of conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
