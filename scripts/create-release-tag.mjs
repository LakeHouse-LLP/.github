#!/usr/bin/env node
/**
 * Create an annotated SemVer release tag from package.json (CI only).
 * Single-package: vX.Y.Z — monorepo: pass --name <pkg> for pkg@X.Y.Z
 * Cross-platform Node. Do not create release tags by hand.
 */
import { spawnSync } from "node:child_process";
import { existsSync, readFileSync } from "node:fs";
import process from "node:process";

function run(cmd, args) {
  const r = spawnSync(cmd, args, {
    encoding: "utf8",
    stdio: ["ignore", "pipe", "pipe"],
  });
  if (r.status !== 0) {
    console.error(r.stderr || r.stdout || `${cmd} failed`);
    process.exit(r.status ?? 1);
  }
  return (r.stdout || "").trim();
}

function parseArgs(argv) {
  const out = {
    name: null,
    packageJson: "package.json",
    dryRun: false,
    push: false,
  };
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--name") out.name = argv[++i];
    else if (a === "--package-json") out.packageJson = argv[++i];
    else if (a === "--dry-run") out.dryRun = true;
    else if (a === "--push") out.push = true;
    else if (a === "--help" || a === "-h") {
      console.log(
        "Usage: node scripts/create-release-tag.mjs [--name <pkg>] [--package-json path] [--push] [--dry-run]"
      );
      process.exit(0);
    } else {
      console.error(`Unknown arg: ${a}`);
      process.exit(2);
    }
  }
  return out;
}

function main() {
  const opts = parseArgs(process.argv);
  if (!existsSync(opts.packageJson)) {
    console.error(`::error::Missing ${opts.packageJson}`);
    process.exit(1);
  }
  const pkg = JSON.parse(readFileSync(opts.packageJson, "utf8"));
  const version = pkg.version;
  if (!version) {
    console.error("::error::package.json has no version");
    process.exit(1);
  }
  const tag = opts.name ? `${opts.name}@${version}` : `v${version}`;
  if (!/^(v\d+\.\d+\.\d+[\w.-]*|[\w.-]+@\d+\.\d+\.\d+[\w.-]*)$/.test(tag)) {
    console.error(`::error::Refusing unexpected tag shape: ${tag}`);
    process.exit(1);
  }

  const existing = spawnSync(
    "git",
    ["rev-parse", "-q", "--verify", `refs/tags/${tag}`],
    { encoding: "utf8" }
  );
  if (existing.status === 0) {
    console.log(`Tag already exists: ${tag}`);
    process.exit(0);
  }

  const msg = `Release ${tag}`;
  console.log(`Creating annotated tag ${tag}`);
  if (opts.dryRun) {
    console.log(`[dry-run] git tag -a ${tag} -m ${JSON.stringify(msg)}`);
    process.exit(0);
  }
  run("git", ["tag", "-a", tag, "-m", msg]);
  if (opts.push) {
    run("git", ["push", "origin", tag]);
    console.log(`Pushed ${tag}`);
  } else {
    console.log("Tag created locally. Pass --push from CI to publish the tag.");
  }
}

main();
