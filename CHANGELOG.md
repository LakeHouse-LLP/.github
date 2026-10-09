# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

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
