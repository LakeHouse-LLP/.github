#!/usr/bin/env node
/**
 * Verify workflow uses: pins match .lakehouse/pins.json (single source of truth).
 * Cross-platform Node (Mac / Windows / Linux). Do not use bash scripts.
 */
import { spawnSync } from "node:child_process";
import { readFileSync, readdirSync, existsSync } from "node:fs";
import { join } from "node:path";
import process from "node:process";

function repoRoot() {
  const r = spawnSync("git", ["rev-parse", "--show-toplevel"], {
    encoding: "utf8",
  });
  if (r.status === 0 && r.stdout.trim()) {
    return r.stdout.trim();
  }
  return process.cwd();
}

function listYml(dir) {
  if (!existsSync(dir)) return [];
  return readdirSync(dir)
    .filter((n) => n.endsWith(".yml") || n.endsWith(".yaml"))
    .map((n) => join(dir, n));
}

function main() {
  const root = repoRoot();
  const pinsPath = join(root, ".lakehouse", "pins.json");
  if (!existsSync(pinsPath)) {
    console.error(`::error::Missing ${pinsPath}`);
    process.exit(1);
  }

  const pins = JSON.parse(readFileSync(pinsPath, "utf8"));
  const expected = {};
  for (const meta of Object.values(pins.actions || {})) {
    expected[meta.uses] = meta.sha;
  }

  const toolGitleaks = pins.tools?.gitleaks || {};
  const gitleaksVer = toolGitleaks.version;
  const gitleaksSha = toolGitleaks.sha256?.linux_x64;

  const workflowPaths = [
    ...listYml(join(root, ".github", "workflows")),
    ...listYml(join(root, "workflow-templates")),
  ].sort();

  const usesRe =
    /uses:\s*(?<action>[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+)@(?<sha>[0-9a-f]{40})/g;
  const verRe = /GITLEAKS_VERSION:\s*"([^"]+)"/;
  const shaRe = /GITLEAKS_SHA256:\s*"([0-9a-f]{64})"/;

  const errors = [];
  for (const path of workflowPaths) {
    const text = readFileSync(path, "utf8");
    const rel = path.slice(root.length + 1).replace(/\\/g, "/");
    for (const m of text.matchAll(usesRe)) {
      const action = m.groups.action;
      const sha = m.groups.sha;
      if (!(action in expected)) {
        errors.push(
          `${rel}: action ${action}@${sha} not listed in .lakehouse/pins.json`
        );
        continue;
      }
      if (expected[action] !== sha) {
        errors.push(
          `${rel}: ${action} pinned to ${sha}, pins.json expects ${expected[action]}`
        );
      }
    }
    if (rel.includes("gitleaks") || text.includes("GITLEAKS_VERSION")) {
      const vm = text.match(verRe);
      const sm = text.match(shaRe);
      if (gitleaksVer && vm && vm[1] !== gitleaksVer) {
        errors.push(
          `${rel}: GITLEAKS_VERSION=${vm[1]}, pins.json expects ${gitleaksVer}`
        );
      }
      if (gitleaksSha && sm && sm[1] !== gitleaksSha) {
        errors.push(`${rel}: GITLEAKS_SHA256 mismatch vs pins.json`);
      }
    }
  }

  if (errors.length) {
    console.log("::error::Workflow pins do not match .lakehouse/pins.json");
    for (const e of errors) console.log(e);
    process.exit(1);
  }

  console.log("check-pins OK — workflows match .lakehouse/pins.json");
}

main();
