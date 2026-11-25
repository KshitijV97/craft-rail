"""Generate the documentation site's 1200x630 link-preview image.

Maintainer-only tool. It needs Pillow, which is deliberately not a CraftRail
dependency: the Core and validator stay standard-library-only, and the docs
build only serves the committed PNG. Run it when the brand text or colors change:

    python3 -m pip install pillow
    python3 tools/generate_og_image.py

Colors match docs/stylesheets/extra.css and the rail mark in docs/images/favicon.svg.
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "docs" / "images" / "og-image.png"

WIDTH, HEIGHT = 1200, 630
NAVY = "#132a3a"
NAVY_DARK = "#0b1b26"
TEAL = "#087e70"
MINT = "#68d6b0"
WHITE = "#ffffff"
MUTED = "#a9bfcc"

TITLE = "CraftRail"
TAGLINE = "Guardrails for agent-driven development"
SUBTITLE = "Git-native, agent-neutral engineering framework"
FOOTER = "craft-rail-docs.vercel.app"

# (path, face index for .ttc collections). First existing file wins.
BOLD_FONTS = [
    ("/System/Library/Fonts/HelveticaNeue.ttc", 1),
    ("/System/Library/Fonts/Helvetica.ttc", 1),
    ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 0),
    ("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 0),
]
REGULAR_FONTS = [
    ("/System/Library/Fonts/HelveticaNeue.ttc", 0),
    ("/System/Library/Fonts/Helvetica.ttc", 0),
    ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 0),
    ("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 0),
]


def load_font(candidates: list[tuple[str, int]], size: int) -> ImageFont.FreeTypeFont:
    for path, index in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size, index=index)
    sys.exit("No usable font found; add a local TrueType font path to the candidate list.")


def draw_rail_mark(draw: ImageDraw.ImageDraw, x: int, y: int, size: int) -> None:
    """Scaled copy of the favicon: rounded navy tile, two rails, three ties."""
    scale = size / 64
    draw.rounded_rectangle(
        (x, y, x + size, y + size), radius=round(14 * scale), fill=NAVY_DARK, outline=TEAL, width=2
    )
    stroke = round(5 * scale)

    def pt(px: float, py: float) -> tuple[float, float]:
        return (x + px * scale, y + py * scale)

    for rail_x in (20, 44):
        draw.line([pt(rail_x, 13), pt(rail_x, 51)], fill=MINT, width=stroke)
    for tie_y in (22, 32, 42):
        draw.line([pt(20, tie_y), pt(44, tie_y)], fill=MINT, width=stroke)
    radius = stroke / 2
    for px, py in ((20, 13), (20, 51), (44, 13), (44, 51)):
        cx, cy = pt(px, py)
        draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), fill=MINT)


def main() -> None:
    image = Image.new("RGB", (WIDTH, HEIGHT), NAVY)
    draw = ImageDraw.Draw(image)

    # Accent band on the left edge and a thin rule above the footer.
    draw.rectangle((0, 0, 16, HEIGHT), fill=TEAL)
    draw.line([(96, 520), (WIDTH - 96, 520)], fill="#294b5f", width=2)

    left = 96
    draw_rail_mark(draw, left, 112, 120)

    draw.text((left, 270), TITLE, font=load_font(BOLD_FONTS, 104), fill=WHITE)
    draw.text((left, 400), TAGLINE, font=load_font(BOLD_FONTS, 46), fill=MINT)
    draw.text((left, 462), SUBTITLE, font=load_font(REGULAR_FONTS, 30), fill=MUTED)
    draw.text((left, 548), FOOTER, font=load_font(REGULAR_FONTS, 28), fill=MUTED)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT, format="PNG", optimize=True)
    print(f"Wrote {OUTPUT.relative_to(ROOT)} ({OUTPUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
