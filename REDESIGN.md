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

## Decisions to confirm (owner)
- `_posts/2025-03-08-ultrabook-intro.md` was an untracked local draft; it is
  committed on this branch and will be published on merge.
- ASE Program Committee: site says 2024 (found on the ASE 2024 committee page);
  the resume says 2025 and no ASE 2025 committee page lists you.
- CV mirrors resume v7 minus the phone number, including "Pangu" and team size.
- Email chenfsd@gmail.com is shown in the footer/CV.
- X handle is @boyuan_chen (@nemocbb now 404s).
- Photos: only scenery, no people (6 frames approved on 2026-10-06).
- Your About portrait (images/profile.png) is kept; talk cards/pages now use
  scenery posters and load YouTube only on click, so no speaker thumbnails show.
- CATO News item: numbers corrected to the paper (10% goodput, 41.1%
  utilization); the 'internally deployed into Huawei Cloud / Ascend' claim is
  yours and kept. Remove it if it should not be public.
- `site.url` stays https://chenboyuan.com (apex) so feed entry ids don't change.

## Found in your existing pages (not changed)
- /humanizer/ is broken on the live site too: its inline DATA has raw newlines
  inside JS strings and a schema render() no longer expects. The daily job on
  your other machine writes it; fix the generator (json.dumps) there.
- /realmaster/ shows generated listings under a 'HouseSigma, Zolo, CREA' source
  credit. Both are left off the Projects page until fixed.

## How to preview / ship
- `bundle exec jekyll serve --config _config.yml,_config.dev.yml`
- Ship: `git checkout master && git merge redesign && git push` (GitHub Pages builds master).

## Next steps
- Add more scenery photos: `uv run scripts/photos.py add <jpg>` then edit `_data/photos.yml`.
