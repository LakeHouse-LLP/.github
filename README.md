<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="brand/logo-dark.svg">
    <img src="brand/logo-light.svg" alt="LakeHouse brand logo (placeholder — Sen uploads final artwork)" width="320">
  </picture>
</p>

<p align="center">
  <a href="docs/releasing.md">Releasing</a> ·
  <a href="docs/repo-metadata.md">Metadata &amp; badges</a> ·
  <a href="brand/USAGE.md">Brand</a> ·
  <a href="docs/pre-release-checklist.md">Pre-release checklist</a>
</p>

# .github

Org-wide shared defaults for the organization described in [`.lakehouse/org.json`](.lakehouse/org.json) (`brand` / `orgName`).

Sen reviews and merges. ZERO COST / GitHub Free. Do not merge without Sen.

Identity, package scope, and public domain live in `.lakehouse/org.json`. Action and reusable-workflow pins live in [`.lakehouse/pins.json`](.lakehouse/pins.json). Releasing: [docs/releasing.md](docs/releasing.md). Rename: [docs/org-rename-runbook.md](docs/org-rename-runbook.md).

Badge URL templates (substitute `OWNER` from `github.repository_owner` / `org.json`): see [docs/repo-metadata.md](docs/repo-metadata.md).

## Contents

| Path | Purpose |
| --- | --- |
| [profile/README.md](profile/README.md) | Org profile README |
| [brand/](brand/) | Logo / social preview placeholders + usage |
| [.lakehouse/org.json](.lakehouse/org.json) | `orgName`, `brand`, `packageScope`, `domain` |
| [.lakehouse/pins.json](.lakehouse/pins.json) | Action SHAs + reusable workflow paths |
| [AGENTS.md](AGENTS.md) / [CLAUDE.md](CLAUDE.md) | House rules + Never do |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution + stacked PR workflow |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Contributor Covenant 3.0 |
| [SECURITY.md](SECURITY.md) | Private vulnerability reporting |
| [SUPPORT.md](SUPPORT.md) | Help channels |
| [retired-names.txt](retired-names.txt) | Names not to reuse |
| [docs/releasing.md](docs/releasing.md) | Tags, changesets, notes, rollback |
| [docs/pre-release-checklist.md](docs/pre-release-checklist.md) | Before Sen publishes |
| [docs/repo-metadata.md](docs/repo-metadata.md) | Description, topics, homepage, badges |
| [docs/media-convention.md](docs/media-convention.md) | `docs/media/` for templates |
| [docs/sen-only-github-settings.md](docs/sen-only-github-settings.md) | UI settings only Sen changes |
| [docs/changelog-convention.md](docs/changelog-convention.md) | Changelog / changesets |
| [docs/org-rename-runbook.md](docs/org-rename-runbook.md) | Org rename before / during / after |
| [.github/release.yml](.github/release.yml) | Auto release-notes config |
| [.github/release-notes-template.md](.github/release-notes-template.md) | Release body template |
| [.github/ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE/) | Bug / feature / docs forms |
| [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md) | Default PR template |
| [.github/labels.yml](.github/labels.yml) | Canonical labels |
| [.github/workflows/](.github/workflows/) | label-sync, org-defaults-ci, release (reusable) |
| [workflow-templates/](workflow-templates/) | Starter workflows (CI, release, …) |
| [scripts/](scripts/) | Node `.mjs` tools |

## Quick policies

- Public → GitHub-hosted runners; private → self-hosted; never self-hosted on public.
- Merge commits only.
- Epics: [SenZhang-Plus/SenZhang-Todo](https://github.com/SenZhang-Plus/SenZhang-Todo).
- Do not hardcode the GitHub org login — use `org.json` or `${{ github.repository_owner }}`.
- Scripts are Node `.mjs` (not bash).
