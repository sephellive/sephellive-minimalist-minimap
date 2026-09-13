"""Build the original UI textures shipped by Sephellive Minimalist Minimap.

This script intentionally does not read or transform textures from third-party
addons. It produces clean-room PNG source images for DDS conversion.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


SIZE = 512
OUT = Path(__file__).resolve().parents[1] / "build" / "textures"


def make_frame() -> None:
    """Create the required but visually neutral background layer."""
    Image.new("RGBA", (8, 8), (0, 0, 0, 0)).save(OUT / "sep_minimap_frame.png")


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
    """Create labels plus a hairline overlay that conceals the faceted clip."""
    scale = 4
    side = SIZE * scale
    center = side // 2
    alpha_mask = Image.new("L", (side, side), 0)
    mask_draw = ImageDraw.Draw(alpha_mask)

    # rounded="1" is polygonal in X-Ray. This narrow annulus covers only that
    # final edge; unlike the old mask it does not create a broad dark frame.
    for radius in range(264, 0, -1):
        if radius < 249:
            alpha = 0
        elif radius < 253:
            alpha = int(210 * (radius - 249) / 4)
        elif radius <= 257:
            alpha = 210
        elif radius < 264:
            alpha = int(210 * (264 - radius) / 7)
        else:
            alpha = 0
        scaled_radius = radius * scale
        mask_draw.ellipse(
            (center - scaled_radius, center - scaled_radius,
             center + scaled_radius, center + scaled_radius),
            fill=alpha,
        )

    edge = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    edge.putalpha(alpha_mask)
    image = edge.resize((SIZE, SIZE), Image.Resampling.LANCZOS)

    labels = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(labels)
    font = label_font(32)
    neutral = (205, 209, 207, 235)
    centered_text(draw, (256, 51), "N", font, (222, 94, 38, 255))
    centered_text(draw, (461, 256), "E", font, neutral)
    centered_text(draw, (256, 461), "S", font, neutral)
    centered_text(draw, (51, 256), "W", font, neutral)
    image = Image.alpha_composite(image, labels)
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
