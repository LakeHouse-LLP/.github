# Merge queue (org canonical)

**Verified against GitHub docs (2026-10):** [Merge queues](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue) are available in **any public repository owned by an organization**, or in **private** repositories owned by organizations on **GitHub Enterprise Cloud**. On **GitHub Free**, that means **public org repos only**. LakeHouse stays ZERO COST → enable the queue on public repos; keep manual merges on private repos.

## Public repos (queue required on `main`)

Applies to: `.github`, `Template-Widget`, `Template-OpenSource`, and every public widget/OSS repo made from them.

- Require the **merge queue** on `main` via a **repository ruleset** (or classic branch protection — prefer rulesets).
- **Merge method: merge commit** only (house rule — never squash or rebase).
- Recommended small-org queue settings (why: few concurrent PRs; avoid huge batched deploys; keep CI load predictable):

| Setting | Recommended | Why |
| --- | --- | --- |
| Build concurrency | **3** | Enough parallel `merge_group` checks without stampeding Actions |
| Max group size | **5** | Caps how many PRs land together |
| Min group size | **1** | Do not block a lone ready PR |
| Wait time | **5 minutes** | Short window to batch neighbors without long idle waits |
| Only merge non-failing PRs | **Enabled** | Required checks must pass |
| Status check timeout | **30–60 minutes** | Fits normal public GitHub-hosted CI |

Exact Sen UI clicks: [sen-only-github-settings.md](sen-only-github-settings.md#merge-queue-ruleset-public-repos).

## Private repos (no queue on Free)

Applies to: `Template-Monorepo`, `Template-Sandbox`, `sandbox-*`, `legacy-*`.

- Merge queue **not available** without Enterprise Cloud — do not enable paid plans for this.
- Manual **bottom-up** merges with **merge commits**.
- Require **up-to-date branch** + **green CI** before merging (ruleset / branch protection).

## CI: `merge_group`

Every **required** check workflow must trigger on:

```yaml
on:
  pull_request:   # no branches: filter — stacked PRs into feature branches still run
  merge_group:    # merge queue temporary branches
```

Without `merge_group`, queued PRs never get status checks and the queue fails. Public `merge_group` jobs use **GitHub-hosted** runners (never self-hosted on public repos).

This repo’s `org-defaults-ci` and the CI-oriented `workflow-templates/*` include `merge_group`.

## Stacked PRs + the queue

1. Only PRs whose **base is `main`** enter the merge queue.
2. Stack mid-layers target the previous feature branch → they get `pull_request` CI, **not** the queue.
3. Merge **bottom-up**: when the base PR is ready, **Sen** enqueues it (merge commit via the queue).
4. After it lands, **retarget** the next PR to `main`, wait for green CI, then **Sen** enqueues that one.

Agents and contributors **never** enqueue or merge — Sen does ([AGENTS.md](../AGENTS.md)).

## Related

- [CONTRIBUTING.md](../CONTRIBUTING.md) — stacked PR workflow  
- Merge commits only — org merge-method settings (Sen-only)  
