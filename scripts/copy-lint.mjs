#!/usr/bin/env node
/**
 * Cheap copy lint aligned with brand/WRITING-STYLE.md:
 * - no em dash (U+2014) or en dash (U+2013)
 * - banned hype / filler words (whole word)
 * Scans markdown outside brand/ (brand kit may mention banned forms as examples).
 */
import { spawnSync } from "node:child_process";
import { readFileSync } from "node:fs";
import { join } from "node:path";
import process from "node:process";

const EM = "\u2014";
const EN = "\u2013";

const BANNED = [
  "revolutionary",
  "game-changing",
  "game-changer",
  "disruptive",
  "next-gen",
  "cutting-edge",
  "seamlessly",
  "seamless",
  "effortlessly",
  "effortless",
  "leverage",
  "utilize",
  "synergy",
  "empower",
  "unlock",
  "robust",
  "best-in-class",
  "world-class",
  "delve",
  "tapestry",
  "unleash",
  "elevate",
  "next-level",
  "all-in-one",
  "one-stop",
  "under one roof",
];

function repoRoot() {
  const r = spawnSync("git", ["rev-parse", "--show-toplevel"], {
    encoding: "utf8",
  });
  return r.status === 0 && r.stdout.trim() ? r.stdout.trim() : process.cwd();
}

function listFiles(root) {
  const r = spawnSync(
    "git",
    ["ls-files", "-z", "-c", "-o", "--exclude-standard"],
    { cwd: root, encoding: "utf8" }
  );
  if (r.status !== 0) return [];
  return r.stdout.split("\0").filter(Boolean);
}

function main() {
  const root = repoRoot();
  const hits = [];

  for (const rel of listFiles(root)) {
    if (!rel.endsWith(".md")) continue;
    if (rel.startsWith("brand/")) continue;
    const text = readFileSync(join(root, rel), "utf8");
    const lines = text.split(/\r?\n/);
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];
      if (line.includes(EM) || line.includes(EN)) {
        hits.push(`${rel}:${i + 1}: em/en dash`);
      }
      const lower = line.toLowerCase();
      for (const w of BANNED) {
        if (w.includes(" ")) {
          if (lower.includes(w)) hits.push(`${rel}:${i + 1}: banned "${w}"`);
        } else {
          const re = new RegExp(`\\b${w.replace(/-/g, "\\-")}\\b`, "i");
          if (re.test(line)) hits.push(`${rel}:${i + 1}: banned "${w}"`);
        }
      }
    }
  }

  if (hits.length) {
    console.log("::error::copy-lint failed (see brand/WRITING-STYLE.md).");
    console.log(hits.slice(0, 50).join("\n"));
    if (hits.length > 50) console.log(`… and ${hits.length - 50} more`);
    process.exit(1);
  }
  console.log("copy-lint OK");
}

main();
