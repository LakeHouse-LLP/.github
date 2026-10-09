# Secrets rotation checklist

Use when rotating any credential listed in the [secrets inventory](secrets-inventory.template.md). **Sen** (or someone Sen explicitly approves) performs Vercel mutations. Agents draft checklists; they do not run `vercel env add/rm` without approval.

## Before

- [ ] Inventory row identified (name, scope, linked projects, environments)
- [ ] Source of truth confirmed (**owner’s vault** for important credentials)
- [ ] Replacement credential generated in the upstream provider
- [ ] Confirm Preview/Development will get **non-prod** replacements only
- [ ] Note whether the value is **shared** (update once, keep links) or **project**-level

## During

- [ ] Store the new value in the **owner’s vault** first
- [ ] Update Vercel (team shared var and/or project env) for the correct environments only
- [ ] Remove or overwrite the old value in Vercel (no lingering prod secret on Preview/Development)
- [ ] If CI used a long-lived token, prefer migrating to **OIDC** instead of rotating in place when possible
- [ ] Redeploy or invalidate previews that must pick up the new value

## After

- [ ] Smoke-test Production (and Preview if affected)
- [ ] Update inventory: **Last rotated**, cadence, Notes
- [ ] Revoke the old credential at the upstream provider
- [ ] Confirm `.env*` files on laptops are refreshed via `vercel env pull` where needed (never commit them)

## Emergency

- [ ] Revoke upstream credential immediately
- [ ] Rotate Vercel values for all linked projects/environments
- [ ] Check gitleaks / git history if exposure was via commit (follow [SECURITY.md](../../SECURITY.md))
