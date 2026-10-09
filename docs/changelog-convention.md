# Changelog convention

## Keep a Changelog

Every durable repo keeps a root `CHANGELOG.md` following [Keep a Changelog](https://keepachangelog.com/):

- Top section is **`## [Unreleased]`**.
- Categories as needed: Added, Changed, Deprecated, Removed, Fixed, Security.
- Release sections use semver headings when you cut a release.

## Changesets (pnpm)

pnpm monorepos **also** use [changesets](https://github.com/changesets/changesets):

- Add a markdown file under `.changeset/` for user-facing changes.
- CI may aggregate changesets into `CHANGELOG.md` on release.

## PR gate

Each PR must either:

1. Modify `CHANGELOG.md` and/or add/update files under `.changeset/`, or
2. Have the **`skip-changelog`** label (chores, template-only, etc.).

Use the org **`changelog-check`** workflow template. Labels are defined in [`.github/labels.yml`](../.github/labels.yml).
