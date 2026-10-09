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
| **Discussions** | Enable where questions and **release announcements** should go. |
| **Immutable releases** | Enable so published release assets/tags cannot be overwritten (see [releasing.md](releasing.md)). |

## Per repository (Sen checklist)

- [ ] Description, topics, homepage (custom `domain` — see [repo-metadata.md](repo-metadata.md))
- [ ] Social preview (1280×640 from [`brand/`](../brand/) or repo media)
- [ ] Discussions on
- [ ] Immutable releases on
- [ ] Tag rulesets for release tags
- [ ] Private vulnerability reporting on
- [ ] Merge commits only (squash/rebase off)
- [ ] npm **OIDC trusted publishing** configured for packages (no long-lived npm tokens)
- [ ] Signing keys for annotated/signed tags (optional but preferred)

## Also Sen-only (related)

- Repository **visibility** changes.
- Org/repo **secrets**, **variables**, and **rulesets** beyond what Free plan allows Sen to configure.
- Creating/deleting org secrets for CI (prefer OIDC over secrets).
- Approving merges into `Template-*` and `.github`.
- Publishing draft GitHub Releases.
- Uploading final **brand** assets into [`brand/`](../brand/).

See [AGENTS.md](../AGENTS.md) **Never do** list.
