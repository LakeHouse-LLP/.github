# Repository metadata standard

Superseded in detail by **[discoverability.md](discoverability.md)** for `Template-LakeHouse-Widget`, `Template-LakeHouse-OpenSource`, their public descendants, and this `.github` repo. This page remains the short checklist for all durable repos. Naming: [naming.md](naming.md).

## Description

- One or two sentences; start with **LakeHouse Studio** or the product name.
- No client names; no secrets; no “WIP” as the permanent description.

## Topics

**8-20** lowercase topics. Pool includes: `lakehouse-studio`, `widget`, `widgets`, `design-tools`, `revit`, `rhino`, `grasshopper`, `bim`, `aec`, `architecture`, `indesign`, `agent-friendly`, plus stack tags. Prefer brand slugs over the GitHub org login.

## Homepage

- Custom **`domain`** from `.lakehouse/org.json` (never `*.github.io`).

## Social preview

- **1280×640** dark [`brand/final/social-preview.png`](../brand/final/social-preview.png). Accent `#7DFFFF` only.

## README header

1. Dark header (`brand/final/readme-header.png` or `brand/final/lakehouse-mark.svg`) - **no light variant**.
2. Keyword-rich **first paragraph** ([discoverability.md](discoverability.md)).
3. Badge row: CI, release, license, Scorecard (public). URLs from `github.repository_owner` / `org.json`:

```markdown
<!-- Substitute OWNER from github.repository_owner or org.json orgName; REPO is this repo name -->
[![CI](https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/OWNER/REPO/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/OWNER/REPO)](https://github.com/OWNER/REPO/releases)
[![License](https://img.shields.io/github/license/OWNER/REPO)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/OWNER/REPO/badge)](https://securityscorecards.dev/viewer/?uri=github.com/OWNER/REPO)
```

## Sen-only UI checklist (metadata-related)

See [sen-only-github-settings.md](sen-only-github-settings.md) and [search-and-analytics.md](search-and-analytics.md).

- [ ] Repository description, topics (8-20), homepage
- [ ] Social preview image
- [ ] Discussions enabled
- [ ] Immutable releases / tag protection
- [ ] Private vulnerability reporting
- [ ] Merge commits only
- [ ] Search Console + Bing + analytics
