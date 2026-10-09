# Releasing

Org-wide release rules for repositories under this GitHub organization. Identity and public links: [`.lakehouse/org.json`](../.lakehouse/org.json). Action pins: [`.lakehouse/pins.json`](../.lakehouse/pins.json). Scripts are Node `.mjs` only.

**Sen reviews and publishes.** Releases are created as **drafts** first; Sen publishes (or approves) after the [pre-release checklist](pre-release-checklist.md).

## Tags and versioning (SemVer)

| Repo kind | Tag shape | Example |
| --- | --- | --- |
| Single-package | `vX.Y.Z` | `v1.4.0` |
| Monorepo package | `<pkg>@X.Y.Z` | `cli@1.4.0` |
| Pre-release | append `-rc.N` or `-beta.N` | `v2.0.0-rc.1`, `cli@2.0.0-beta.2` |

### Monorepo tag scheme (chosen default)

Use **`<pkg>@X.Y.Z`** (not `<service>/vX.Y.Z`).

- Aligns with npm package names and [changesets](https://github.com/changesets/changesets).
- Avoids ambiguous `v` prefixes when many packages share one repo.
- If an existing repo already uses `<service>/vX.Y.Z`, **Sen decides** whether to migrate or document an exception; do not invent a third scheme.

### Tag rules

- Tags are **annotated** (`git tag -a`).
- **Signed** where keys are available (SSH or GPG signing — Sen configures).
- **Protected** against force-moves and deletes (rulesets — Sen-only UI).
- **Only CI creates release tags**, never humans from a laptop. Local `git tag` for releases is forbidden.

## Changelog and changesets

- [Keep a Changelog](https://keepachangelog.com/) sections: **Added**, **Changed**, **Deprecated**, **Removed**, **Fixed**, **Security**.
- **changesets** drive `CHANGELOG.md` and version bumps (required for pnpm repos; recommended elsewhere).
- Highlight **breaking changes** with migration notes in the changeset and release notes.
- Each changelog entry links its PR.
- PRs must touch CHANGELOG/changeset or carry `skip-changelog` (see [changelog-convention.md](changelog-convention.md)).

## Release notes

- Config: [`.github/release.yml`](../.github/release.yml) — auto-generated notes grouped by labels; excludes bots and chores.
- Body template: [`.github/release-notes-template.md`](../.github/release-notes-template.md) — highlights, breaking/upgrade steps, changelog link, checksums/attestation, supported Revit / Rhino / OS where relevant.

## Release workflow

High-level pipeline (see workflow templates `release-public` / `release-private` / `version-pr` and reusable `.github/workflows/release.yml`):

1. **Version PR** — changesets (or equivalent) bumps versions and CHANGELOG; merge with a **merge commit** (`workflow-templates/version-pr.yml`).
2. **Tag** — CI creates the annotated SemVer tag with `node scripts/create-release-tag.mjs [--name <pkg>] --push` (never by hand).
3. **Build** — produce artifacts on the correct runner tier.
4. **Checksums** — SHA256 for each uploaded asset.
5. **Attestation** — `actions/attest-build-provenance` (pinned in `pins.json`).
6. **Upload** — attach assets to a **draft** GitHub Release.
7. **Publish packages** — **npm OIDC trusted publishing** (provenance; **no long-lived npm tokens**). Sen configures the trusted publisher on the npm side.
8. **Publish release** — Sen turns the draft into a published release after checklist + approval.

### Runner tiers

| Visibility | Runner | Template |
| --- | --- | --- |
| Public | GitHub-hosted (`ubuntu-latest`) | `workflow-templates/release-public.yml` |
| Private | Self-hosted | `workflow-templates/release-private.yml` |

Never use self-hosted runners on public repos.

### Immutable releases

Turn on **immutable releases** in the GitHub UI (Sen-only). After publish, release assets/tags must not be overwritten. See [sen-only-github-settings.md](sen-only-github-settings.md).

## Rollback / yank

1. **Do not delete tags** if immutable releases / tag protection forbid it (preferred).
2. **Yank npm**: `npm unpublish <pkg>@<version>` only within npm’s yank window, or deprecate: `npm deprecate <pkg>@<version> "message"`. Prefer **deprecate** + publish a fixed version.
3. **GitHub Release**: mark the release as **unpublished** / draft only if policy allows; otherwise edit the release body with a **YANKED** banner linking to the replacement version. With immutable releases, do not replace assets — publish a new patch.
4. **Announce** in Discussions (and security advisory if needed).
5. Record the yank in CHANGELOG under **Removed** or **Fixed** as appropriate.

## Media and brand

- Org placeholders and usage: [`brand/`](../brand/).
- Per-repo media convention: [media-convention.md](media-convention.md) (`docs/media/` in templates and product repos).

## Related

- [pre-release-checklist.md](pre-release-checklist.md)
- [repo-metadata.md](repo-metadata.md)
- [CONTRIBUTING.md](../CONTRIBUTING.md) (stacked PRs, merge commits)
