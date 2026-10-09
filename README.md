<p align="center">
  <img src="brand/logo.svg" alt="LakeHouse Studio logo (placeholder — Sen uploads final artwork)" width="360">
</p>

<p align="center">
  <a href="docs/discoverability.md">Discoverability</a> ·
  <a href="docs/releasing.md">Releasing</a> ·
  <a href="docs/seo-checklist.md">SEO checklist</a> ·
  <a href="brand/USAGE.md">Brand</a>
</p>

# .github

**LakeHouse Studio** org-wide shared defaults — the GitHub backbone for an all-in-one digital office for designers and small offices (Revit, Rhino, Grasshopper, and day-to-day design tools), with a calm lakeside home-office feel. This repository holds community health files, release and SEO standards, brand placeholders, and reusable workflow templates for Template-OpenSource and related public repos.

Sen reviews and merges. ZERO COST / GitHub Free. Do not merge without Sen.

Identity and public domain: [`.lakehouse/org.json`](.lakehouse/org.json). Pins: [`.lakehouse/pins.json`](.lakehouse/pins.json). Brand: dark-only, accent `#7DFFFF` ([`brand/`](brand/)).

## Contents

| Path | Purpose |
| --- | --- |
| [profile/README.md](profile/README.md) | Org profile README (LakeHouse Studio) |
| [brand/](brand/) | Dark-only logo / social preview placeholders |
| [CITATION.cff](CITATION.cff) | Citation metadata |
| [docs/discoverability.md](docs/discoverability.md) | Descriptions, topics, pins, profile strategy |
| [docs/docs-site.md](docs/docs-site.md) | Astro Starlight org docs decision |
| [docs/seo-checklist.md](docs/seo-checklist.md) | Reusable SEO checklist |
| [docs/search-and-analytics.md](docs/search-and-analytics.md) | Search Console, Bing, analytics (Sen) |
| [docs/launch-checklist.md](docs/launch-checklist.md) | Launch channels checklist |
| [docs/awesome-lists.md](docs/awesome-lists.md) | Awesome-list submission guide |
| [docs/releasing.md](docs/releasing.md) | Tags, changesets, notes, rollback |
| [docs/pre-release-checklist.md](docs/pre-release-checklist.md) | Before Sen publishes a release |
| [docs/repo-metadata.md](docs/repo-metadata.md) | Short metadata checklist |
| [docs/media-convention.md](docs/media-convention.md) | `docs/media/` for templates |
| [docs/sen-only-github-settings.md](docs/sen-only-github-settings.md) | UI settings only Sen changes |
| [AGENTS.md](AGENTS.md) / [CLAUDE.md](CLAUDE.md) | House rules + Never do |
| [workflow-templates/](workflow-templates/) | Starter workflows (incl. discoverability-check) |
| [scripts/](scripts/) | Node `.mjs` tools |

## Quick policies

- Public → GitHub-hosted runners; private → self-hosted; never self-hosted on public.
- Merge commits only.
- Epics: [SenZhang-Plus/SenZhang-Todo](https://github.com/SenZhang-Plus/SenZhang-Todo).
- Do not hardcode the GitHub org login — use `org.json` or `${{ github.repository_owner }}`.
- Scripts are Node `.mjs` (not bash).
- Dark mode only; single accent `#7DFFFF`.
