"""Build the original UI textures shipped by Sephellive Minimalist Minimap.

This script intentionally does not read or transform textures from third-party
addons. It produces clean-room PNG source images for DDS conversion.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


SIZE = 512
OUT = Path(__file__).resolve().parents[1] / "build" / "textures"


def make_frame() -> None:
    """Mask Anomaly's polygonal map clip behind a smooth, line-free edge shade."""
    scale = 4
    side = SIZE * scale
    center = side // 2
    image = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    shadow_mask = Image.new("L", (side, side), 0)
    draw = ImageDraw.Draw(shadow_mask)
    # The HUD stretches its background slightly wider than the map frame.
    # A compensated ellipse therefore becomes a visually round mask in-game.
    for radius in range(246, 0, -1):
        if radius < 208:
            alpha = 0
        elif radius < 220:
            alpha = int(220 * (radius - 208) / 12)
        elif radius <= 230:
            alpha = 220
        elif radius < 246:
            alpha = int(220 * (246 - radius) / 16)
        else:
            alpha = 0
        radius_x = int(radius * 0.965 * scale)
        radius_y = radius * scale
        draw.ellipse(
            (center - radius_x, center - radius_y,
             center + radius_x, center + radius_y),
            fill=alpha,
        )
    shadow = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    shadow.putalpha(shadow_mask.filter(ImageFilter.GaussianBlur(0.75 * scale)))
    image = Image.alpha_composite(image, shadow)
    image.resize((SIZE, SIZE), Image.Resampling.LANCZOS).save(OUT / "sep_minimap_frame.png")


def label_font(size: int) -> ImageFont.FreeTypeFont:
    for path in (Path("C:/Windows/Fonts/segoeuib.ttf"), Path("C:/Windows/Fonts/arialbd.ttf")):
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def centered_text(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str,
                  font: ImageFont.FreeTypeFont, fill: tuple[int, int, int, int]) -> None:
    box = draw.textbbox((0, 0), text, font=font)
    draw.text((xy[0] - (box[2] - box[0]) // 2, xy[1] - (box[3] - box[1]) // 2 - box[1]), text, font=font, fill=fill)


def make_compass() -> None:
    """Create a label-only compass: coloured N, neutral remaining directions."""
    image = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    font = label_font(32)
    neutral = (205, 209, 207, 235)
    centered_text(draw, (256, 51), "N", font, (222, 94, 38, 255))
    centered_text(draw, (461, 256), "E", font, neutral)
    centered_text(draw, (256, 461), "S", font, neutral)
    centered_text(draw, (51, 256), "W", font, neutral)
    image.save(OUT / "sep_minimap_compass.png")


def make_player_arrow() -> None:
    """Create a small, soft-coloured forward arrow for the player marker."""
    image = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.polygon([(32, 13), (45, 47), (32, 39), (19, 47)], fill=(172, 83, 42, 205))
    draw.polygon([(32, 18), (39, 40), (32, 35), (25, 40)], fill=(223, 126, 68, 220))
    image.save(OUT / "sep_minimap_player.png")


def make_counter_background() -> None:
    """Create a neutral transparent backing for Anomaly's required counter node."""
    Image.new("RGBA", (8, 8), (0, 0, 0, 0)).save(OUT / "sep_minimap_counter.png")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    make_frame()
    make_compass()
    make_player_arrow()
    make_counter_background()


if __name__ == "__main__":
    main()
