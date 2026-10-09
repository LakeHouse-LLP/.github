# Repository metadata standard

Apply to every durable repo (skip empty squat orgs and throwaway sandboxes unless Sen says otherwise).

## Description

- One or two sentences; start with the product or template name (`brand` from `.lakehouse/org.json`).
- No client names; no secrets; no “WIP” as the permanent description.

## Topics

Use lowercase GitHub topics. Prefer a stable core set plus repo-specific tags:

| Topic | When |
| --- | --- |
| `lakehouse` | All org product/template repos (brand, not org login) |
| `revit` / `rhino` / `grasshopper` | When applicable |
| `typescript` / `dotnet` / … | Primary stack |
| `monorepo` | Template-Monorepo descendants |
| `opensource` | Public OSS repos |

Do not put the GitHub **org login** in topics if it would churn on rename; use the **brand** slug.

## Homepage

- Set the repo **Website** field to a path on the custom **`domain`** from `.lakehouse/org.json` (never `*.github.io`).
- Until `domain` is replaced with a real host, leave homepage empty or use the GitHub repo URL temporarily — **Sen decides**.

## Social preview

- Upload a **1280×640** image (see [`brand/`](../brand/) social-preview placeholders).
- Prefer brand-consistent light or dark asset; no client/Ennead content.

## README header

1. Logo via `<picture>` with light/dark (`brand/` or repo `docs/media/`).
2. Badge row: **CI**, **release**, **license**, and **Scorecard** (public repos).
3. Badge and link URLs must be built from **`github.repository_owner`** / `org.json` — do not hardcode the org login. Template:

```markdown
<!-- Substitute OWNER from github.repository_owner or org.json orgName; REPO is this repo name -->
[![CI](https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/OWNER/REPO/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/OWNER/REPO)](https://github.com/OWNER/REPO/releases)
[![License](https://img.shields.io/github/license/OWNER/REPO)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/OWNER/REPO/badge)](https://securityscorecards.dev/viewer/?uri=github.com/OWNER/REPO)
```

## Sen-only UI checklist (metadata-related)

See [sen-only-github-settings.md](sen-only-github-settings.md) for the full list. Metadata-adjacent items:

- [ ] Repository description, topics, homepage
- [ ] Social preview image
- [ ] Discussions enabled (for release announcements)
- [ ] Immutable releases enabled
- [ ] Tag protection rulesets (no move/delete of release tags)
- [ ] Private vulnerability reporting
- [ ] Merge method = merge commit only
