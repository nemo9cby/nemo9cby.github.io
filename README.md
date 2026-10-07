# chenboyuan.com

Personal site of Boyuan Chen, built with Jekyll and served by GitHub Pages
(`www.chenboyuan.com`). It started from the academicpages template; the
design, layouts and styles have since been rewritten.

## Run it locally

```sh
bundle install
bundle exec jekyll serve --config _config.yml,_config.dev.yml
```

Then open http://localhost:4000.

## Where things live

| What | Where |
| --- | --- |
| Home page text (About Me, News, Selected Publications) | `_pages/about.md`. The layout splits it at each `##` heading; hero photo, tagline and the photo-filled statement are in its front matter |
| Blog posts | `_posts/YYYY-MM-DD-title.md` (`math: true` or `$$...$$` loads MathJax) |
| Publications | `_publications/*.md`, one file per paper (`venue`, `status`, `authors`, `paperurl`, `links`) |
| Talks | `_talks/*.md` (`youtube_id` embeds the video; `featured: true` shows it on the home page) |
| Projects | `_data/projects.yml` |
| CV | `_pages/cv.md` |
| Navigation | `_data/navigation.yml` |
| Styles | `_sass/site/*.scss` (plain CSS; GitHub Pages compiles with Ruby Sass 3.7) |
| Scripts | `assets/js/site.js` (nav, lightbox, news toggle) |

`humanizer/` and `realmaster/` are standalone pages with their own markup.

## Adding photographs

Only scenery: no people in the frame.

```sh
uv run scripts/photos.py add ~/Pictures/selected/DSC01234.jpg
```

This writes WebP sizes to `images/photos/` with all metadata (including GPS)
removed, records size, colour and camera settings in `_data/photo_meta.yml`,
and appends a stub to `_data/photos.yml`. Fill in its `title`, `place` and
`alt` there; the order of that file is the gallery order.

`uv run scripts/photos.py social DSC01234` makes the 1200x630 link-preview
image (`images/og-image.jpg`).

Tests: `cd scripts && uv run --with pillow --with pyyaml --with pytest pytest -q`
