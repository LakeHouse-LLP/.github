# Pre-release checklist

Complete before Sen publishes a draft GitHub Release. Copy into the release PR or Discussion as needed.

## Legal and third-party

- [ ] License headers present on first-party source where the repo requires them
- [ ] Third-party **NOTICE** (or equivalent) updated for bundled dependencies
- [ ] License field / `LICENSE` file matches the intended SPDX license

## Security

- [ ] Secrets scan clean (gitleaks / org secret scan workflow)
- [ ] No client data, Ennead content, or credentials in the tree, artifacts, or notes
- [ ] Open security advisories reviewed; none block this release (or release is an advisory fix)
- [ ] Attestations and SHA256 checksums will be attached by CI

## Product / docs

- [ ] Docs and README updated for user-facing changes
- [ ] Version consistency: package.json / changesets / tags / release title agree (SemVer)
- [ ] External links checked (docs on custom `domain` from `.lakehouse/org.json`, not `*.github.io`)
- [ ] Accessibility spot-check for UI surfaces (contrast, focus, alt text on new media)
- [ ] Supported **Revit**, **Rhino**, and **OS** versions noted in release notes when relevant

## Process

- [ ] Changelog / changesets complete; breaking changes have migration notes
- [ ] CI green on the version PR and on the release tag workflow
- [ ] Release created as **draft**; assets + notes reviewed
- [ ] Announcement ready (GitHub **Discussions** post)
- [ ] Sen publishes the release (immutable releases enabled - no later asset overwrite)
