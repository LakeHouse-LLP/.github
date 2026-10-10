# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- Absorb-legacy pointer: [docs/absorb-legacy.md](docs/absorb-legacy.md) and one-line `AGENTS.md` row pointing at the `sen-guide-absorb-repo` skill (no duplicated absorb steps).
- Template curation pointer: [docs/template-curation.md](docs/template-curation.md) and one-line `AGENTS.md` row pointing at the `lakehouse-template-curation` skill (org skills use the `lakehouse-*` prefix; no duplicated curation steps).
- Continuous self-improvement: house rule in `AGENTS.md`, [docs/lessons.md](docs/lessons.md) log, PR template **What did we learn?**, and CONTRIBUTING section on org-wide lesson flow into `Template-*` repos.
- Brand kit **v0.3** under `brand/` (tokens, writing, final assets, Python build scripts); profile/README header + tagline; `scripts/copy-lint.mjs`; Sen-only avatar (`final/png/appicon-1024.png`) and social preview (`final/social-preview.png`) steps.
- Merge queue canonical policy: [docs/merge-queue.md](docs/merge-queue.md); `merge_group` on required CI workflows/templates; Sen-only ruleset click-path; agents never enqueue/merge.
- Vercel env canonical rules: [docs/deploy/vercel-env.md](docs/deploy/vercel-env.md), secrets inventory + rotation templates; AGENTS.md Never-do for mutating Vercel env without Sen approval.

### Changed

- Dual public templates: **Template-Widget** (LakeHouse widgets) and recreated **Template-OpenSource** (general OSS, no widget concepts). `Template-OpenSource` removed from retired-names (active again; note that an earlier repo of that name was renamed to Template-Widget on 2026-10-09). Four-template chooser in [docs/naming.md](docs/naming.md).

### Added

- Contributor growth: friendly `CONTRIBUTING.md` (Mac/Windows + Codespaces), `GOVERNANCE.md`, `ROADMAP.md`, starter-issue + listings guides, maintainer playbook, `good first issue` / `help wanted` labels, welcome workflow template, `.all-contributorsrc`, `.devcontainer/`.
- Discoverability / SEO: `docs/discoverability.md`, awesome-lists, docs-site (Astro Starlight), SEO + launch + search/analytics checklists, `CITATION.cff`, `scripts/discoverability-check.mjs`, workflow template.
- Org profile README positioned as **LakeHouse Studio** (digital office / lakeside home office).

### Changed

- Brand kit is **dark-mode-only** with single accent `#7DFFFF`; light assets removed.
- `org.json` `brand` → `LakeHouse Studio`.

### Added (release system)

- Release system: `docs/releasing.md`, `.github/release.yml`, release-notes template, reusable `release` workflow, public/private/version-pr workflow templates, `brand/` placeholders, repo metadata + pre-release checklists, `scripts/create-release-tag.mjs`.
- Labels `breaking-change` and `chore` for release-notes grouping.
- `.lakehouse/org.json` as the source of truth for `orgName`, `brand`, `packageScope`, and `domain`.
- `.lakehouse/pins.json` for action SHAs and reusable workflow paths; `scripts/check-pins.mjs`.
- Org-name lint (`scripts/org-name-lint.mjs`) + `org-defaults-ci` workflow + `org-name-lint` workflow template.
- House rule: repo scripts are cross-platform Node `.mjs` (not bash).
- `docs/org-rename-runbook.md` (before / during / after, including squatting the old org name).

### Changed

- Workflows and docs prefer `org.json` / `${{ github.repository_owner }}` over a hardcoded org login.

### Added (scaffold)

- Org profile README, community health files (Code of Conduct, Contributing, Security, Support).
- `AGENTS.md` / `CLAUDE.md` house rules and Never do list.
- `retired-names.txt`, Sen-only GitHub settings doc, changelog convention doc.
- Issue forms (bug / feature / docs), PR template, labels, reusable label-sync workflow.
- Workflow templates: CI, gitleaks, tier-guard, changelog-check.
