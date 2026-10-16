# CI runner queue relief (private / self-hosted)

Private LakeHouse repos share **one** self-hosted Windows runner. GitHub-hosted minutes on private repos are **not** allowed (ZERO COST). Use these patterns so superseded and docs-only runs do not sit in a multi-hour queue.

## 1. Concurrency (PR / branch only)

Add to every PR-driven workflow (and keep on `merge_group` when present):

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}
  cancel-in-progress: ${{ github.ref != format('refs/heads/{0}', github.event.repository.default_branch) }}
```

- Cancels superseded runs for the same PR or feature branch.
- **Does not** cancel in-progress jobs on the default branch (release tagging / publish).
- **Do not** put `cancel-in-progress: true` on release / version-publish workflows that push to `main` or tags.

Canonical starters: `workflow-templates/ci.yml`, `workflow-templates/ci-private.yml`.

## 2. Docs-only `paths-ignore` (heavy jobs only)

On expensive CI / gitleaks (not on metadata checks):

```yaml
on:
  pull_request:
    paths-ignore:
      - "**/*.md"
      - "docs/**"
      - "release-notes/**"
```

Keep **`require-release-notes`** and **`changelog-check`** **without** this `paths-ignore` so docs / notes PRs still get a required status when heavy CI is skipped.

## 3. Metadata jobs and `runs-on`

| Visibility | `runs-on` for metadata (changelog, release-notes, labels, PR body) |
| --- | --- |
| **Public** | `ubuntu-latest` (GitHub-hosted) |
| **Private** | Self-hosted labels only; keep the job **lightweight** (checkout + shell/`gh`, no full build) |

Never move private metadata checks to `ubuntu-latest` (burns private Actions minutes). Prefer:

```yaml
runs-on: ${{ github.event.repository.private && fromJSON('["self-hosted"]') || fromJSON('["ubuntu-latest"]') }}
defaults:
  run:
    shell: bash
```

## 4. Repos with local workflows

After updating templates here, open a small PR in each **private** repo whose `.github/workflows/*` are **not** `uses:` callers of this defaults repo: add the same concurrency + heavy-job `paths-ignore`, and ensure metadata workflows stay lightweight on self-hosted.

Merge with a **merge commit** only when required checks are green (never merge red or unrun).
