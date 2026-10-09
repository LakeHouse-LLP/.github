# .github

Org-wide shared defaults for the **[`.lakehouse/org.json`](.lakehouse/org.json)** organization (`brand` / `orgName`).

Sen reviews and merges. ZERO COST / GitHub Free. Do not merge without Sen.

Identity, package scope, and public domain live in `.lakehouse/org.json`. Action and reusable-workflow pins live in [`.lakehouse/pins.json`](.lakehouse/pins.json). Rename procedure: [docs/org-rename-runbook.md](docs/org-rename-runbook.md).

## Contents

| Path | Purpose |
| --- | --- |
| [profile/README.md](profile/README.md) | Org profile README |
| [.lakehouse/org.json](.lakehouse/org.json) | `orgName`, `brand`, `packageScope`, `domain` |
| [.lakehouse/pins.json](.lakehouse/pins.json) | Action SHAs + reusable workflow paths |
| [AGENTS.md](AGENTS.md) / [CLAUDE.md](CLAUDE.md) | House rules + Never do |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution + stacked PR workflow |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Contributor Covenant 3.0 |
| [SECURITY.md](SECURITY.md) | Private vulnerability reporting |
| [SUPPORT.md](SUPPORT.md) | Help channels |
| [retired-names.txt](retired-names.txt) | Names not to reuse |
| [docs/sen-only-github-settings.md](docs/sen-only-github-settings.md) | UI settings only Sen changes |
| [docs/changelog-convention.md](docs/changelog-convention.md) | Changelog / changesets |
| [docs/org-rename-runbook.md](docs/org-rename-runbook.md) | Org rename before / during / after |
| [.github/ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE/) | Bug / feature / docs forms |
| [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md) | Default PR template |
| [.github/labels.yml](.github/labels.yml) | Canonical labels |
| [.github/workflows/](.github/workflows/) | label-sync (reusable) + org-defaults-ci |
| [workflow-templates/](workflow-templates/) | Starter workflows |
| [scripts/](scripts/) | Node `.mjs` tools (org-name-lint, check-pins) |

## Quick policies

- Public → GitHub-hosted runners; private → self-hosted; never self-hosted on public.
- Merge commits only.
- Epics: [SenZhang-Plus/SenZhang-Todo](https://github.com/SenZhang-Plus/SenZhang-Todo).
- Do not hardcode the GitHub org login — use `org.json` or `${{ github.repository_owner }}`.
