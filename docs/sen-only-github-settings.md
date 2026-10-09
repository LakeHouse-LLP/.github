# GitHub UI settings only Sen can change

These org/repo controls are **owner-only**. Agents and contributors must not change them via API, UI, or automation unless Sen explicitly directs it in-band.

## Org

| Setting | Intent |
| --- | --- |
| **Member privileges** | Base permissions, forking, pages creation, etc. Keep aligned with ZERO COST / Free plan. |
| **Public-repo rulesets** | Branch/tag protection for public repos. Require PRs into default branches without blocking stacked PRs whose base is a feature branch. Enable **merge queue** on `main` for public repos ([merge-queue.md](merge-queue.md)). |
| **Tag protection** | Block force-moves and deletes of release tags (`v*` / `*@*`). |
| **Merge methods** | Allow **merge commits** only; turn **off squash** and **rebase** merges org-wide or per repo. |
| **Private vulnerability reporting** | Enable for public (and private as needed) repos so [SECURITY.md](../SECURITY.md) works. |
| **Discussions** | Enable where questions and **release announcements** should go. Create categories: **Ideas**, **Q&A**, **Show and tell**. |
| **Immutable releases** | Enable so published release assets/tags cannot be overwritten (see [releasing.md](releasing.md)). |
| **Org profile + pinned repos** | Keep [`profile/README.md`](../profile/README.md) strategy; pin flagship OSS + docs entry ([discoverability.md](discoverability.md)). |
| **Actions → fork PRs** | Require approval for first-time contributors’ workflows ([maintainer-playbook.md](maintainer-playbook.md)). |

## Merge queue ruleset (public repos)

**Availability (verified):** GitHub documents merge queues for **public repositories owned by an organization** (including Free), or **private** repos on **Enterprise Cloud** only. Do **not** enable paid plans for private-repo queues.

Do this on each **public** repo (`.github`, `Template-Widget`, `Template-OpenSource`, public widgets/OSS):

### A. Repo merge methods

1. Repo → **Settings** → **General** → **Pull Requests**.
2. Enable **Allow merge commits**.
3. Disable **Allow squash merging** and **Allow rebase merging**.

### B. Ruleset on `main` (preferred)

1. Repo → **Settings** → **Rules** → **Rulesets** → **New branch ruleset** (or org-level ruleset targeting public repos if you use one).
2. **Ruleset name:** e.g. `main-merge-queue`.
3. **Enforcement status:** Active.
4. **Bypass list:** only Sen (or empty - Sen uses admin bypass only when necessary).
5. **Target branches:** Include default branch **`main`** (exact name - merge queue must not use `*` wildcards on classic protection; keep the target exact).
6. Under **Branch rules**, enable at least:
 - **Restrict deletions**
 - **Require a pull request before merging** (do **not** apply this rule in a way that blocks PRs whose base is a **feature branch** for stacks - target **`main` only**)
 - **Require status checks to pass** → add the required check job names (e.g. `lint`, `ci`, `gitleaks`, …) that your workflows report
 - **Require merge queue**
7. Open **Require merge queue** / merge queue configuration and set:
 - **Merge method:** **Merge commit** (not squash / rebase)
 - **Build concurrency:** `3`
 - **Maximum pull requests to merge** (max group): `5`
 - **Minimum pull requests to merge:** `1`
 - **Wait time:** `5` minutes
 - **Only merge non-failing pull requests:** enabled
 - **Status check timeout:** `60` minutes (or `30` if CI is consistently fast)
8. **Save changes**.
9. Confirm required workflows include `on.merge_group` ([merge-queue.md](merge-queue.md)).

### C. Private repos (no queue)

1. Do **not** turn on Require merge queue (unavailable / would need Enterprise Cloud).
2. Ruleset on `main`: require PR, require status checks, **require branch to be up to date** before merging.
3. Merge method: **merge commit** only.
4. Sen merges manually (bottom-up for stacks).

## Brand assets (GitHub UI)

1. **Org avatar:** Organization → **Settings** → **Profile** → upload [`brand/final/png/appicon-1024.png`](../brand/final/png/appicon-1024.png) (square L1 app icon).
2. **Per-repo social preview:** each public repo → **Settings** → **General** → **Social preview** → upload [`brand/final/social-preview.png`](../brand/final/social-preview.png) (1280×640).

Favicon guidance for sites/apps: [`brand/README.md`](../brand/README.md).

## Per repository (Sen checklist)

- [ ] Description, **8-20 topics**, homepage (custom `domain` - see [discoverability.md](discoverability.md))
- [ ] Social preview uploaded (`brand/final/social-preview.png`)
- [ ] Org avatar uploaded once (`brand/final/png/appicon-1024.png`)
- [ ] Discussions on + categories (Ideas, Q&A, Show and tell)
- [ ] First-time contributor workflow **approval** required
- [ ] Immutable releases on
- [ ] Tag rulesets for release tags
- [ ] Private vulnerability reporting on
- [ ] Merge commits only (squash/rebase off)
- [ ] **Public:** merge queue ruleset on `main` (section above)
- [ ] **Private:** up-to-date + green CI; no merge queue
- [ ] npm **OIDC trusted publishing** configured for packages (no long-lived npm tokens)
- [ ] Signing keys for annotated/signed tags (optional but preferred)
- [ ] Google Search Console + Bing Webmaster + Cloudflare Web Analytics ([search-and-analytics.md](search-and-analytics.md))
- [ ] After metadata is set on this `.github` repo: remove `DISCOVERABILITY_REQUIRE_METADATA: "false"` from `org-defaults-ci`
- [ ] Seed **3-5** `good first issue` / `help wanted` issues ([starter-issues.md](starter-issues.md))

## Also Sen-only (related)

- Repository **visibility** changes.
- Org/repo **secrets**, **variables**, and **rulesets** beyond what Free plan allows Sen to configure.
- Creating/deleting org secrets for CI (prefer OIDC over secrets).
- **Vercel** team Shared Environment Variables and project env vars ([deploy/vercel-env.md](deploy/vercel-env.md)) - agents must not mutate without explicit approval.
- Approving merges / **merge-queue enqueues** into `Template-*` and `.github`.
- Publishing draft GitHub Releases.
- Uploading final **brand** assets into [`brand/`](../brand/).
- **Owner’s vault** (Google Drive) for important credential values.

See [AGENTS.md](../AGENTS.md) **Never do** list.
