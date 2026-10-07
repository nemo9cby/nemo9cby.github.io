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
- CV page links the resume PDF as-is: `files/Boyuan_Chen_CV.pdf` (copy of
  Boyuan_Chen_Resume_Kami_v7.pdf). It contains your phone number and plain email.
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

## To clean up last (owner: 'leave to the end')
- /humanizer/ is broken on the live site too: its inline DATA has raw newlines
  inside JS strings and a schema render() no longer expects. The daily job on
  your other machine writes it; fix the generator (json.dumps) there.
- /realmaster/ shows generated listings under a 'HouseSigma, Zolo, CREA' source
  credit. Both are left off the Projects page until fixed.

## How to preview / ship
- `bundle exec jekyll serve --config _config.yml,_config.dev.yml`
- Ship (another machine pushes to master, so update first):
  `git fetch origin && git checkout master && git merge --ff-only origin/master && git merge --ff-only redesign && git push`.
  If the second ff-only fails, rebase `redesign` onto `origin/master` first.

## Next steps
- Add more scenery photos: `uv run scripts/photos.py add <jpg>` then edit `_data/photos.yml`.
