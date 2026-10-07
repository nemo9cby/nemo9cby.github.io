# /// script
# requires-python = ">=3.10"
# dependencies = ["fonttools>=4.47", "brotli"]
# ///
"""Draw an email address as SVG outlines (no text), so scrapers can't read it.

    uv run scripts/email_svg.py someone@example.com > _includes/email-svg.html

The glyphs come from Mona Sans (the site's UI font, fetched from Google Fonts)
at weight 500, width 100. The SVG uses fill="currentColor" and an em-based height, so it follows the
surrounding text colour and size.
"""

import io
import re
import sys
import urllib.request

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

CSS_URL = "https://fonts.googleapis.com/css2?family=Mona+Sans:wdth,wght@75..125,200..900"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def latin_font() -> TTFont:
    css = fetch(CSS_URL).decode()
    blocks = re.findall(r"/\* latin \*/\s*@font-face\s*{[^}]*?url\((https://[^)]+\.woff2)\)", css)
    if not blocks:
        sys.exit("error: could not find the latin Mona Sans font in the Google Fonts CSS")
    font = TTFont(io.BytesIO(fetch(blocks[0])))
    return instancer.instantiateVariableFont(font, {"wght": 500, "wdth": 100})


def outline(text: str, font: TTFont) -> tuple[str, int, int]:
    cmap, glyphs, hmtx = font.getBestCmap(), font.getGlyphSet(), font["hmtx"]
    ascent, descent = font["hhea"].ascent, font["hhea"].descent
    pen = SVGPathPen(glyphs, ntos=lambda v: str(round(v)))  # whole font units are plenty
    x = 0
    for ch in text:
        name = cmap.get(ord(ch))
        if name is None:
            sys.exit(f"error: the font has no glyph for {ch!r}")
        glyphs[name].draw(TransformPen(pen, (1, 0, 0, -1, x, ascent)))
        x += hmtx[name][0]
    return pen.getCommands(), x, ascent - descent


def main() -> None:
    if len(sys.argv) != 2 or "@" not in sys.argv[1]:
        sys.exit(__doc__)
    font = latin_font()
    d, width, height = outline(sys.argv[1], font)
    em = height / font["head"].unitsPerEm  # box height in ems, so it sizes like the text around it
    print(
        f'<svg class="email-svg" viewBox="0 0 {width} {height}" height="{em:.3f}em" aria-hidden="true" focusable="false">'
        f'<path fill="currentColor" d="{d}"/></svg>'
    )


if __name__ == "__main__":
    main()
