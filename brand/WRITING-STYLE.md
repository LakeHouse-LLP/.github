# LakeHouse Studio: writing style guide

> v0.3 (October 9, 2026: taste-skill copy rules added). English is the primary language; Chinese guidance is included where it applies.
> In short: **write like a thoughtful architect explaining something to a colleague over coffee.** Warm, plain, confident. Never hype.

## 1. Voice
Our voice stays the same everywhere.

| We sound | Like this | Not like this |
|---|---|---|
| **Warm** | "Your timesheet is saved. Have a good evening." | "Timesheet persistence operation completed successfully." |
| **Plain** | "Exports every sheet to PDF." | "Leverages a robust pipeline to seamlessly streamline deliverables." |
| **Confident** | "This replaces 40 clicks with one." | "This might possibly help save some time, hopefully!" |
| **Precise** | "Renumbers 128 doors on Level 3." | "Fixes your doors." |
| **Never hype** | "New: InDesign Helper places sheet images automatically." | "Game-changing AI revolutionizes InDesign!!!" (with a rocket emoji) |

## 2. Tone (it shifts with context)
| Context | Tone | Example |
|---|---|---|
| Onboarding, empty states | Welcoming, light, the house metaphor allowed | "Welcome in. Start in the Studio with your first Revit model." |
| Everyday UI | Brief, neutral, invisible | "Export 12 sheets" |
| Errors | Calm, specific, helpful. No blame, no jokes | "Couldn't reach the license server. Check your connection and try again." |
| Docs | Clear, step by step, patient | "1. Open the Workshop tab. 2. Choose **Batch export**." |
| Release notes | Factual, user benefit first | "Timesheets now total by project phase." |
| Social | Friendly, a little personal, specific | "Built a small tool this week that renames Revit views by sheet number." |

## 3. Mechanics (English)
- **US English.** Use sentence case for headings, buttons and menu items ("Export sheets", not "Export Sheets").
- **Address the reader as "you".** Use "we" for LakeHouse. Use "I" only in Sen's personal posts.
- **Use active voice and present tense.** Lead with the verb in buttons: *Save*, *Export sheets*, *Start timer*.
- **Keep sentences short.** About 20 words or fewer; one idea per sentence.
- **Numbers:** numerals for all quantities in UI ("3 sheets"). Units with a space: `12 mm`, `3.2 m`, `40 h`. Use imperial/metric as the project is set; never mix them in one string.
- **Dates:** in UI, use `Oct 9, 2026`. In logs and files, use ISO `2026-10-09`. Times with a zone label ("10:30 AM ET").
- **Use the Oxford comma.** No exclamation marks in UI. At most one in a social post.
- **Zero em dashes and zero en dashes** (U+2014, U+2013), in English and Chinese (no 破折号 either). They're the clearest tell of machine-written copy. Use a period, comma, colon or parentheses instead. Ranges use a plain hyphen: `2-4`, `9:00-17:00`, `A-D`.
- **Middle dot (·):** at most one per line, and only between two short metadata items ("Revit 2025 · 1.4.0"). Never as a decorative strip of words ("Studio · Workshop · Library").
- **Labels are literal.** Section titles say what's in the section ("Install", "Release notes"), never poetic ("Field notes", "From the bench", "The quiet hours").
- **Emoji:** none in product UI, docs, release notes or brand assets. At most one in a personal social post.
- **Bold** is for UI labels in docs ("Click **Export**"). Use `code` for file names, commands, parameters and token names.
- **Accessibility in text:** use meaningful link text ("Read the export guide"), not "click here". Write alt text for every image.

## 4. Chinese guidance (中文写作)
- 用在：给中文用户的界面、文档和社交媒体（如小红书、微信公众号）。英文是源语言，中文要意译，不要逐字翻译。
- **品牌名不翻译：** 写 `LakeHouse Studio`，中英文之间加半角空格：`欢迎来到 LakeHouse Studio`。
- **语气：** 亲切、简洁、专业，用"你"，不用"您"（正式合同和发票除外）。不用网络流行语和夸张词（"颠覆""炸裂""yyds""赋能""闭环"）。
- **标点：** 中文句子用全角标点（，。：；？），英文、数字、代码保持半角。数字与单位之间加空格：`12 mm`、`40 小时`。
- **术语：** 软件名和专有名词保留英文（Revit、Rhino、InDesign、Keynote、Excel）。房间名首次出现写作"工作室（Studio）"，之后可只用中文。
- **按钮：** 2-4 个字，动词开头：`导出图纸`、`开始计时`、`保存`。
- **错误提示：** 先说发生了什么，再说怎么办："无法连接许可证服务器。请检查网络后重试。"
- **字体：** Noto Sans SC，正文行高 1.7，不使用伪粗体或斜体。

## 5. Glossary

### 5.1 Product and brand
| Term | Use | Notes |
|---|---|---|
| LakeHouse Studio | Full brand name | Never Lakehouse / Lake House |
| LakeHouse | Short form | After first mention |
| LakeHouse-LLP | GitHub org handle only | Not used in prose |
| LakeHouse *Noun* | Product names: LakeHouse Timesheet, LakeHouse InDesign Helper, LakeHouse FM, LakeHouse for Revit, LakeHouse for Rhino | Title case, plain nouns |
| room | A product area: Studio, Workshop, Library, Office, Theater, Game room | Capitalize as nav names; use lightly |
| helper | A small, focused tool inside a host app (InDesign Helper, Excel Helper) | Prefer it to "bot", "agent", "copilot" |
| assistant | A production assistant that runs multi-step jobs (batch export, QA) | Say what it does; don't personify it |
| plugin | Code that runs inside Revit, Rhino, InDesign, etc. | Not "add-on" or "extension" (except in Chrome/VS Code) |
| app | The LakeHouse desktop or web app | |
| workspace | One office's account (team, projects, settings) | Not "tenant" in UI |

### 5.2 AEC terms (write them exactly like this)
| Term | Notes |
|---|---|
| AEC | Architecture, engineering and construction. Spell it out on first use in public copy |
| BIM | Building information modeling (lowercase when spelled out) |
| Revit, Rhino, Grasshopper, AutoCAD, InDesign, Keynote, Excel | Official casing. Not REVIT, rhino3d |
| family, type, instance, parameter (shared/project) | Revit concepts, lowercase |
| view, sheet, title block, viewport, schedule | Revit/CAD documentation, lowercase |
| level, grid, room, area, space | Lowercase. "room" here means the BIM element; disambiguate from our rooms when needed |
| model, central model, linked model, workset | Lowercase |
| drawing set, issue, revision, transmittal | Documentation workflow |
| SD, DD, CD, CA | Schematic design, design development, construction documents, construction administration. Spell out on first use |
| phase, project number, fee, hours | Timesheet vocabulary. Use "hours", not "time units" |
| FM | Facility management. Spell out on first use; "FM" after |
| AR / VR / XR | Augmented / virtual / extended reality. "VR walkthrough", not "metaverse" |
| NYC | OK in casual copy; "New York" in formal copy |

## 6. Patterns

### 6.1 README
```markdown
![LakeHouse Studio](./brand/readme-header.png)

# LakeHouse Timesheet
Simple timesheets for small design offices. Track hours by project and phase, export to Excel.

## What it does
- Start and stop timers from the desktop app or the Revit ribbon
- Totals by project, phase and person
- One-click export to `.xlsx`

## Install
…exact steps…

## Quick start
…3-5 steps with a screenshot (dark UI)…

## Part of LakeHouse Studio
A second home for your design practice. This tool lives in the **Office**.

## License
```
Rules: start with one sentence of what it does, for whom. No badges wall (3 max). Dark screenshots. No client project imagery in examples. Use sample models only (e.g. the Autodesk sample projects, or our own "Lake Cabin" demo model).

### 6.2 Release notes
```markdown
## LakeHouse for Revit 1.4.0 (Oct 9, 2026)

### New
- **Batch export** now names PDFs from the sheet number and name.

### Improved
- Renumbering 500+ doors is about 3× faster.

### Fixed
- The timer no longer stops when Revit loses focus. (#142)

### Heads-up
- Requires Revit 2024 or later.
```
Group as New / Improved / Fixed / Heads-up. Lead each item with the user benefit. Use past tense for fixes ("no longer…"). Link issues. Don't write "various bug fixes" without listing them.

### 6.3 Error messages
Formula: **what happened + why (if known) + what to do.** No blame, no "Oops!", no error code alone.

| Don't write | Write |
|---|---|
| "Error 0x80004005." | "Couldn't save the timesheet. The file is open in Excel. Close it and try again. (Code 0x80004005)" |
| "Invalid input!" | "Enter hours as a number, like 7.5." |
| "Oops! Something went wrong :)" | "Export stopped at sheet A-201. The view has no crop region. Add one, then resume." |
| "You entered the wrong license key." | "That license key doesn't match. Check for extra spaces, or copy it again from your email." |

Always offer a way forward (Retry, Open log, Contact support). Keep technical details behind "Show details".

### 6.4 UI microcopy
- **Buttons:** verb plus object. *Export sheets*, *Start timer*, *Place images*. Avoid *OK*/*Submit*. Destructive actions name the object: *Delete 3 views*.
- **Confirmations:** "Delete 3 views? This can't be undone." → [Cancel] [Delete 3 views]
- **Success:** brief and specific: "Exported 24 sheets to /Issue-05." Add one warm touch occasionally ("Saved. Nice work today.") but never in repeated actions.
- **Empty states:** what this is, plus the first action. "No timesheets yet. Start a timer to log your first hours."
- **Loading:** say what's happening: "Reading 1,204 elements…" and give "Step 2 of 4" for long jobs.
- **Settings:** use labels as nouns ("Default export folder") and helper text as a sentence.
- **Tooltips:** at most one sentence, no period for fragments.

### 6.5 Commits and PR titles (Conventional Commits)
Format: `type(scope): imperative summary`, lowercase, no period, ≤72 characters.

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`. Scopes: package or room (`tokens`, `revit`, `rhino`, `indesign`, `timesheet`, `fm`, `web`, `desktop`).
```
feat(timesheet): add totals by project phase
fix(revit): keep timer running when revit loses focus
docs(tokens): document color.accent as provisional
refactor(rhino): move eto styles to design-tokens
feat(tokens)!: rename color.brand to color.accent
```
Breaking changes: add `!` and a `BREAKING CHANGE:` footer. PR titles use the same format. The PR body has **What**, **Why**, **How to test** and **Screenshots (dark)**. Never mention clients, client projects or employer work in commits, branches, PRs or issue text, and don't commit client files or Ennead content.

### 6.6 Documentation
- Structure: overview (what and who) → install → quick start → how-to guides → reference → troubleshooting.
- Title tasks as "How to…" or with a verb ("Export a drawing set").
- Use numbered steps, one action per step, UI labels in **bold**, results in plain text: "**Export** opens the export panel."
- Give each code block a language and something copyable. Screenshots show dark UI at 2× resolution, cropped tight, with alt text.
- Explain *why* briefly when it helps a designer decide.

### 6.7 Social posts
- Show real work: a GIF of a tool saving clicks, a before/after, a small lesson learned. One idea per post.
- Structure: hook (a specific problem) → what we made → a short demo → link. 280 characters or fewer for X; LinkedIn may run longer, with short paragraphs.
- Hashtags: 0-3, relevant only (#Revit #AEC #BIM).
- Use the social card (`social-preview.png`) or dark UI captures.

> **X:** Renaming 300 Revit views by sheet number used to take an afternoon. LakeHouse for Revit does it in one click now. Free for small offices → github.com/LakeHouse-LLP
>
> **小红书/微信:** 做了一个小工具：Revit 视图按图纸编号一键重命名，以前要一下午，现在一秒钟。LakeHouse Studio，给设计师和小事务所的"第二个家"。

## 7. Words to avoid
| Avoid | Use instead |
|---|---|
| revolutionary, game-changing, disruptive, next-gen, cutting-edge | say what changed and by how much |
| seamless(ly), effortless(ly), magic(al) | "in one step", "automatically" |
| leverage, utilize, synergy, empower, unlock | use, help, let you |
| robust, powerful, best-in-class, world-class | specific capability or number |
| simply, just, easy, obviously | (delete; it's not easy for everyone) |
| AI-powered as a headline | describe the task; mention AI in detail only if relevant |
| 10x, rocket emoji, "crush it", "ninja", "rockstar" | (delete) |
| elevate, unleash, delve, tapestry, game-changer, next-level, "in the world of", "it's not just X, it's Y" | (delete; say the concrete thing) |
| "under one roof", "all-in-one", "your one-stop" | name the three things it does |
| poetic labels: "Field notes", "Crafted with care", "The quiet hours" | literal labels: "Docs", "Changelog" |
| user error, invalid, illegal, fatal, abort | "couldn't", "doesn't match", "stopped" |
| click here | descriptive link text |
| whitelist/blacklist, master/slave | allowlist/blocklist, main/primary |
| guys | everyone, folks, team |
| Lakehouse, Lake House | LakeHouse |
| 赋能、颠覆、闭环、抓手、yyds、绝绝子 | 帮助、改进、完成、具体说明 |

## 8. Confidentiality: never mention
- **Clients:** no client names, project names, locations, drawings, models, screenshots or "trusted by" logos unless the client has given written permission. Write "a 12-person studio in Brooklyn", or better, nothing at all.
- **Ennead Architects:** never mention or reference Ennead projects, people, standards, templates, tools or internal content in any LakeHouse material: code, docs, examples, commits, social posts or sample data. LakeHouse is Sen's independent work. Build demos from our own sample models.
- **No secrets in text:** never put API keys, license keys, server names or internal paths in docs, screenshots or logs shared publicly.
- When in doubt, leave it out and ask Sen.

## 9. Checklist before you publish
- [ ] Name written as LakeHouse / LakeHouse Studio
- [ ] Says what it does, for whom, in the first sentence
- [ ] No hype words or AI filler (§7), no exclamation marks in UI
- [ ] Zero em or en dashes; ranges with a hyphen
- [ ] Middle dot at most once per line; no emoji
- [ ] Taglines and headlines short and specific (headline at most 2 lines, subtext at most 20 words)
- [ ] Errors say what happened and what to do
- [ ] Sentence case; numbers and units formatted
- [ ] Screenshots dark, with alt text, and no client or Ennead content
- [ ] Chinese version uses full-width punctuation, keeps the brand name in English, and has spaces around Latin text
