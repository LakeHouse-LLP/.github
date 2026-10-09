#!/usr/bin/env node
/**
 * Fail if hardcoded org login strings appear outside the allowlist.
 * Cross-platform Node (Mac / Windows / Linux). Do not use bash scripts.
 */
import { spawnSync } from "node:child_process";
import { readFileSync, readdirSync, statSync, existsSync } from "node:fs";
import { join, relative, sep } from "node:path";
import process from "node:process";

// Built in pieces so this file does not itself contain the forbidden org-login literals.
const PATTERN_SRC = "LakeHouse" + "-LLP|lakehouse" + "-llp";
const PATTERN = new RegExp(PATTERN_SRC);
const ALLOWLIST_FILE =
  process.env.ORG_NAME_LINT_ALLOWLIST || ".lakehouse/org-name-lint-allowlist.txt";

function repoRoot() {
  const r = spawnSync("git", ["rev-parse", "--show-toplevel"], {
    encoding: "utf8",
  });
  if (r.status === 0 && r.stdout.trim()) {
    return r.stdout.trim();
  }
  return process.cwd();
}

function loadAllowlist(path) {
  if (!existsSync(path)) {
    console.error(`::error::Missing allowlist: ${path}`);
    process.exit(1);
  }
  return readFileSync(path, "utf8")
    .split(/\r?\n/)
    .map((l) => l.trim())
    .filter((l) => l && !l.startsWith("#"));
}

function matchGlob(rel, pattern) {
  if (rel === pattern) return true;
  if (!pattern.includes("*")) return false;
  const escaped = pattern
    .split("**")
    .map((part) =>
      part.replace(/[.+^${}()|[\]\\]/g, "\\$&").replace(/\*/g, "[^/]*")
    )
    .join(".*");
  return new RegExp(`^${escaped}$`).test(rel);
}

function isAllowed(rel, patterns) {
  return patterns.some((pat) => matchGlob(rel, pat));
}

function listGitFiles(root) {
  const r = spawnSync(
    "git",
    ["ls-files", "-z", "-c", "-o", "--exclude-standard"],
    { cwd: root, encoding: "utf8" }
  );
  if (r.status !== 0) return null;
  return r.stdout.split("\0").filter(Boolean);
}

function walkFiles(dir, root, out) {
  for (const name of readdirSync(dir)) {
    if (name === ".git") continue;
    const full = join(dir, name);
    const st = statSync(full);
    if (st.isDirectory()) walkFiles(full, root, out);
    else out.push(relative(root, full).split(sep).join("/"));
  }
}

function listFiles(root) {
  const git = listGitFiles(root);
  if (git) return git;
  const out = [];
  walkFiles(root, root, out);
  return out;
}

function main() {
  const root = repoRoot();
  const patterns = loadAllowlist(join(root, ALLOWLIST_FILE));
  const hits = [];

  for (const rel of listFiles(root)) {
    if (isAllowed(rel, patterns)) continue;
    const full = join(root, rel);
    let data;
    try {
      data = readFileSync(full);
    } catch {
      continue;
    }
    if (data.subarray(0, 8192).includes(0)) continue;
    let text;
    try {
      text = data.toString("utf8");
    } catch {
      continue;
    }
    const lines = text.split(/\r?\n/);
    for (let i = 0; i < lines.length; i++) {
      if (PATTERN.test(lines[i])) {
        hits.push(`${rel}:${i + 1}:${lines[i]}`);
      }
    }
  }

  if (hits.length) {
    console.log("::error::Hardcoded org login found outside allowlist.");
    console.log(`Pattern: /${PATTERN_SRC}/`);
    console.log(
      "Prefer .lakehouse/org.json (orgName) or ${{ github.repository_owner }}."
    );
    console.log(`Allowed paths: ${ALLOWLIST_FILE}`);
    console.log("");
    console.log(hits.join("\n"));
    process.exit(1);
  }

  console.log("org-name-lint OK (no disallowed matches).");
}

main();
