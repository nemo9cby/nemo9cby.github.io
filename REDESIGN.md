# 2026-10 redesign: notes and next steps

Branch: `redesign` (based on `origin/master` @ 5f84d3f). Nothing has been pushed.

## What changed
- New look inspired by khou22.com: full-bleed hero photo, oversized Mona Sans
  type filled with photographs, Charter/Charis SIL reading text, dark navy band,
  justified photo gallery with lightbox, dark mode. Old Minimal Mistakes theme,
  jQuery and icon fonts removed.
- Content framework kept: `_pages/about.md` still holds About Me / News /
  Selected Publications (the home layout splits it at each `##`), posts stay in
  `_posts`, publications and talks use the academicpages collections.
- New: /photography/, /portfolio/ (Projects), real /talks/, /publications/, /cv/.
- Content refreshed from resume v7 and a verified sweep of public links
  (37 publications/theses, 12 talks, projects, profiles).

## Decisions (owner answers, 2026-10-07)
- ASE Program Committee: 2024 (confirmed). The resume PDF still says 2025.
- "A Hitchhiker's guide towards training" (2025-03-08) was an untracked local
  draft you don't remember: moved to `_drafts/ultrabook-intro.md`, not published.
- CV page links `files/Boyuan_Chen_CV.pdf`: resume v7 re-rendered without the phone
  number and with ASE 2024 (WeasyPrint 68.0 + the original PDF's embedded Charter
  fonts; copy at ~/Downloads/Recents/Boyuan_Chen_Resume_Kami_v7_web.pdf). Your
  original v7 HTML/PDF still say ASE 2025.
- Email is never plain text on the site: it is drawn as SVG outlines
  (`_includes/email-svg.html`, regenerate with `uv run scripts/email_svg.py ADDRESS`)
  and site.js builds the mailto: from `author.email_parts`. Feed has no email.
- Talk covers are the real YouTube thumbnails; the player loads on click.
- CV mirrors resume v7 minus the phone number, including "Pangu" and team size.
- CV Education adds "M.A.Sc. (2017)" (your York M.A.Sc. thesis is public and listed
  on /publications/); the resume shows only the Ph.D.
- CATO News item: numbers corrected to the paper (10% goodput, 41.1%
  utilization); the 'internally deployed into Huawei Cloud / Ascend' claim stays (OK'd).
- About portrait (images/profile.png) kept.
- ICSE 2017 and ASE 2018 talks are listed with you as speaker (first author;
  the programs don't name presenters). Correct if someone else presented.
- `site.url` stays https://chenboyuan.com (apex) so feed entry ids don't change.
- Photos: only scenery, no people (6 frames approved on 2026-10-06).

## /humanizer/ and /realmaster/ (diagnosed 2026-10-07, not yet changed)
### humanizer
- Publisher: OpenClaw cron agent turn "Sync Humanizer Page to GitHub Pages" (daily 23:00)
  on the gateway Mac (Nemos-MacBook-Pro-4584.local, likely Nemo-mbp15). Not on this Mac.
- Blank page: data is spliced into `const DATA` through a step that turns `\n` escapes
  into real newlines (e.g. re.sub with a string replacement), so the script fails to
  parse. 22 of 27 versions, including the live one.
- Schema drift: render() expects the 2026-02-22 fields; later data uses ~20 key sets,
  and the live DATA is a single object, not a list.
- Resets: agents sometimes overwrite the log instead of appending (02-28, 03-20).
- Silent failure: nothing pushed since 2026-03-20 while the job reports ok.
- Privacy: the page source and public git history hold an AI-invented "I own NVDA"
  line, 43 unpublished XHS drafts, bot-check scores, strategy labels and replies to
  208 named X accounts.
- Fix if kept: pause the job first; data.json + JSON.parse + a normalizer; an
  append-only JSONL log written by code (json.dump); verify the push.
### realmaster
- Everything shown is generated mock data (2026-02-22 Codex run) but credited to
  HouseSigma/Zolo/CREA and "Claude API"; fake sales use real street names; the AI tab
  is canned text that contradicts the charts; dates show a day early; favicon 404;
  mobile overflow; data stops at 2025-12.
- The scraper never produced usable sold dates (7,012 of 7,364 rows have none).
- Source is uncommitted (~/Projects/vibe_ideas/realmaster); a HouseSigma access token
  is hardcoded in 24 backend files: move it to .env, gitignore, log out to revoke it.
- Options: label as a demo and fix (recommended) / real monthly aggregates / remove.
### Security on this Mac (m4p)
- ~/.openclaw/exec-approvals.json: security=full, ask=off (remote agents run any command).
- ~/.zsh_history has an OPENCLAW_GATEWAY_TOKEN export: rotate it and delete the line.

## How to preview / ship
- `bundle exec jekyll serve --config _config.yml,_config.dev.yml`
- Ship (another machine pushes to master, so update first):
  `git fetch origin && git checkout master && git merge --ff-only origin/master && git merge --ff-only redesign && git push`.
  If the second ff-only fails, rebase `redesign` onto `origin/master` first.

## Next steps
- Add more scenery photos: `uv run scripts/photos.py add <jpg>` then edit `_data/photos.yml`.
