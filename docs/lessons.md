# Lessons log

Short dated entries for friction found while shipping work. Any lesson that comes up repeatedly gets **promoted** to a house rule (`AGENTS.md`), a script under `scripts/`, or a CI check.

Statuses: `open` (still hurts), `fixed` (resolved in-repo), or `promoted` (now a rule, script, or check).

How org-wide lessons reach other repos: [CONTRIBUTING.md](../CONTRIBUTING.md#org-wide-lessons).

## Format

```markdown
### YYYY-MM-DD - short title

- **Lesson:** one sentence.
- **Action:** what to do next (or what was done).
- **Status:** open | fixed | promoted
```

## Entries

<!-- Newest first. Keep each entry short. -->

### 2026-10-16 - private repo access for org CI PRs

- **Lesson:** A Cloud Agent GitHub App installed only on the public defaults repo cannot list or PR private org repos that share the Windows runner.
- **Action:** Sen grants the app All repositories (or each private runner consumer); then re-run queue-relief PRs per [docs/ci-runner-queue.md](ci-runner-queue.md).
- **Status:** open
