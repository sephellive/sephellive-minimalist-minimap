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
    """Draw a thin anti-aliased rim and a restrained inner map vignette."""
    scale = 4
    side = SIZE * scale
    center = side // 2
    radius = 226 * scale
    image = Image.new("RGBA", (side, side), (0, 0, 0, 0))

    shadow = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    draw = ImageDraw.Draw(shadow)
    for offset in range(34 * scale):
        ratio = offset / (34 * scale)
        alpha = int(4 + 58 * ratio * ratio)
        current_radius = radius - offset
        draw.ellipse(
            (center - current_radius, center - current_radius,
             center + current_radius, center + current_radius),
            outline=(0, 0, 0, alpha),
            width=scale,
        )
    image = Image.alpha_composite(image, shadow.filter(ImageFilter.GaussianBlur(1.25 * scale)))

    rim = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    rim_draw = ImageDraw.Draw(rim)
    rim_draw.ellipse(
        (center - radius, center - radius, center + radius, center + radius),
        outline=(8, 10, 11, 205),
        width=2 * scale,
    )
    rim_draw.ellipse(
        (center - radius + 4 * scale, center - radius + 4 * scale,
         center + radius - 4 * scale, center + radius - 4 * scale),
        outline=(110, 87, 60, 85),
        width=scale,
    )
    image = Image.alpha_composite(image, rim)
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
    """Create an original, unobtrusive forward arrow for the player marker."""
    image = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.polygon([(32, 4), (54, 55), (32, 45), (10, 55)], fill=(19, 15, 11, 210))
    draw.polygon([(32, 8), (49, 51), (32, 41), (15, 51)], fill=(204, 78, 29, 255))
    draw.polygon([(32, 15), (39, 40), (32, 35), (25, 40)], fill=(244, 133, 53, 255))
    image.save(OUT / "sep_minimap_player.png")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    make_frame()
    make_compass()
    make_player_arrow()


if __name__ == "__main__":
    main()
