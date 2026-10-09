# GitHub UI settings only Sen can change

These org/repo controls are **owner-only**. Agents and contributors must not change them via API, UI, or automation unless Sen explicitly directs it in-band.

## Org

| Setting | Intent |
| --- | --- |
| **Member privileges** | Base permissions, forking, pages creation, etc. Keep aligned with ZERO COST / Free plan. |
| **Public-repo rulesets** | Branch/tag protection for public repos. Require PRs into default branches without blocking stacked PRs whose base is a feature branch. |
| **Tag protection** | Block force-moves and deletes of release tags (`v*` / `*@*`). |
| **Merge methods** | Allow **merge commits** only; turn **off squash** and **rebase** merges org-wide or per repo. |
| **Private vulnerability reporting** | Enable for public (and private as needed) repos so [SECURITY.md](../SECURITY.md) works. |
| **Discussions** | Enable where questions and **release announcements** should go. Create categories: **Ideas**, **Q&A**, **Show and tell**. |
| **Immutable releases** | Enable so published release assets/tags cannot be overwritten (see [releasing.md](releasing.md)). |
| **Org profile + pinned repos** | Keep [`profile/README.md`](../profile/README.md) strategy; pin flagship OSS + docs entry ([discoverability.md](discoverability.md)). |
| **Actions → fork PRs** | Require approval for first-time contributors’ workflows ([maintainer-playbook.md](maintainer-playbook.md)). |

## Per repository (Sen checklist)

- [ ] Description, **8–20 topics**, homepage (custom `domain` — see [discoverability.md](discoverability.md))
- [ ] Social preview (1280×640 dark [`brand/social-preview.png`](../brand/social-preview.png))
- [ ] Discussions on + categories (Ideas, Q&A, Show and tell)
- [ ] First-time contributor workflow **approval** required
- [ ] Immutable releases on
- [ ] Tag rulesets for release tags
- [ ] Private vulnerability reporting on
- [ ] Merge commits only (squash/rebase off)
- [ ] npm **OIDC trusted publishing** configured for packages (no long-lived npm tokens)
- [ ] Signing keys for annotated/signed tags (optional but preferred)
- [ ] Google Search Console + Bing Webmaster + Cloudflare Web Analytics ([search-and-analytics.md](search-and-analytics.md))
- [ ] After metadata is set on this `.github` repo: remove `DISCOVERABILITY_REQUIRE_METADATA: "false"` from `org-defaults-ci`
- [ ] Seed **3–5** `good first issue` / `help wanted` issues ([starter-issues.md](starter-issues.md))

## Also Sen-only (related)

- Repository **visibility** changes.
- Org/repo **secrets**, **variables**, and **rulesets** beyond what Free plan allows Sen to configure.
- Creating/deleting org secrets for CI (prefer OIDC over secrets).
- **Vercel** team Shared Environment Variables and project env vars ([deploy/vercel-env.md](deploy/vercel-env.md)) — agents must not mutate without explicit approval.
- Approving merges into `Template-*` and `.github`.
- Publishing draft GitHub Releases.
- Uploading final **brand** assets into [`brand/`](../brand/).
- **Owner’s vault** (Google Drive) for important credential values.

See [AGENTS.md](../AGENTS.md) **Never do** list.
