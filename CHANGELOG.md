# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Changed

- Renamed template references: `Template-OpenSource` → `Template-Widget` (retired name recorded). Public repos documented as standalone agent-friendly widgets ([docs/naming.md](docs/naming.md)).

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
