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
    """Draw only a gentle, line-free inner vignette for the map edge."""
    scale = 4
    side = SIZE * scale
    center = side // 2
    radius = 226 * scale
    image = Image.new("RGBA", (side, side), (0, 0, 0, 0))

    shadow_mask = Image.new("L", (side, side), 0)
    draw = ImageDraw.Draw(shadow_mask)
    vignette_width = 56 * scale
    for offset in range(vignette_width + 1):
        ratio = offset / vignette_width
        alpha = int(13 * (1 - ratio) * (1 - ratio))
        current_radius = radius - offset
        draw.ellipse(
            (center - current_radius, center - current_radius,
             center + current_radius, center + current_radius),
            fill=alpha,
        )
    shadow = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    shadow.putalpha(shadow_mask.filter(ImageFilter.GaussianBlur(2 * scale)))
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
