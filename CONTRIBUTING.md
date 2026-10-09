# Contributing to LakeHouse Studio

Thanks for stopping by — we are glad you are here. This guide gets you productive quickly on **Mac or Windows**. Public repos are either LakeHouse **widgets** (`Template-Widget`) or general **open-source** projects (`Template-OpenSource`) — see [docs/naming.md](docs/naming.md#which-template-should-i-use). Sen reviews and merges; please open a **draft PR** and do not merge into `Template-*` or `.github` yourself.

House rules (agents and humans): [AGENTS.md](AGENTS.md). Code of conduct: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Governance & response times: [GOVERNANCE.md](GOVERNANCE.md).

Identity / domain: [`.lakehouse/org.json`](.lakehouse/org.json).

## Find something to work on

1. Browse issues labeled **`good first issue`** or **`help wanted`** (see [docs/starter-issues.md](docs/starter-issues.md)).
2. Say hi in **Discussions** (Ideas / Q&A / Show and tell — Sen enables categories).
3. Skim [ROADMAP.md](ROADMAP.md) so your idea fits the direction.

## 5-minute setup (Mac & Windows)

Works the same on macOS and Windows (PowerShell or Terminal). Need **Git**, **Node.js 22+**, and a GitHub account.

```bash
# 1) Fork the repo on GitHub, then clone your fork (replace OWNER/REPO)
git clone https://github.com/OWNER/REPO.git
cd REPO

# 2) Install dependencies (pick what the repo uses)
# pnpm (preferred in monorepos):
corepack enable
pnpm install
# or: npm ci   /   npm install

# 3) Run the smoke checks used in this defaults repo (adapt per product repo)
node scripts/org-name-lint.mjs
node scripts/check-pins.mjs

# 4) Create a branch and open a draft PR when ready
git checkout -b fix/my-change
```

### Codespaces / Dev Container

Open the repo in **GitHub Codespaces** or VS Code Dev Containers — the checked-in [`.devcontainer/devcontainer.json`](.devcontainer/devcontainer.json) provides Node 22 and common tooling. First boot may take a few minutes; then run the same install/smoke commands as above.

### DCO (public repos)

Sign off commits:

```bash
git commit -s -m "Describe your change"
```

## Pull requests (short path)

1. Keep the PR small; prefer [stacked PRs](#stacked-prs) for larger work.
2. Fill the PR template (summary, stack, tests, checklist).
3. Touch `CHANGELOG.md` / `.changeset/` **or** add the `skip-changelog` label.
4. Wait for CI (GitHub-hosted on public repos). Maintainers will not run untrusted fork code on self-hosted runners — see [docs/maintainer-playbook.md](docs/maintainer-playbook.md).
5. Sen merges with a **merge commit** only (never squash/rebase-merge).

## Org constraints (summary)

- **ZERO COST** — GitHub Free only.
- **Runners** — Public: GitHub-hosted. Private: self-hosted. Never self-hosted on public.
- **Epics** — [SenZhang-Plus/SenZhang-Todo](https://github.com/SenZhang-Plus/SenZhang-Todo), not GitHub Issues.
- **Naming** — Four templates (`Template-Monorepo`, `Template-Sandbox`, `Template-Widget`, `Template-OpenSource`). See [docs/naming.md](docs/naming.md).
- **Identity** — Do not hardcode the GitHub org login; use `org.json` or `${{ github.repository_owner }}`.

## Merge queue (public repos)

On GitHub Free, the **merge queue is available for public org repos only** (private needs Enterprise Cloud — we stay ZERO COST). Public repos require the queue on `main` with **merge commits**. Private repos: manual merge commits + up-to-date branch + green CI. Full policy: [docs/merge-queue.md](docs/merge-queue.md). **Sen** enqueues and merges — contributors do not.

## Stacked PRs

Prefer **small stacked PRs**: each branch is based on the previous feature branch.

1. PR 1: `feature/a` → `main`
2. PR 2: `feature/b` → `feature/a`
3. List the stack in every PR body
4. Merge **bottom-up**: only PRs targeting `main` enter the merge queue; after the base lands, retarget the next PR to `main`, then Sen enqueues it

Recommended tool: `git rebase --update-refs` (Git 2.38+). CI must use `pull_request` with **no `branches` filter**, plus `merge_group` for queue checks. Exception: senzhang-todo-style ledger edits may go straight to `main`.

## Changelog & releases

- Keep a Changelog + changesets for pnpm repos — [docs/changelog-convention.md](docs/changelog-convention.md)
- Releases: [docs/releasing.md](docs/releasing.md)

## Recognition

We use [All Contributors](https://allcontributors.org/). After your PR lands, you may appear in the README contributors table (see [`.all-contributorsrc`](.all-contributorsrc)).

## Questions

Use **Discussions** (not blank issues). Support expectations: [SUPPORT.md](SUPPORT.md).
