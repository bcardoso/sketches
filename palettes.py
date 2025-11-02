"""Color palettes from base16 schemes.

Usage:

  from palette import Palette
  palette = Palette("nord")

About base16 & color schemes:
- https://github.com/chriskempson/base16
- https://github.com/chriskempson/base16-default-schemes
- https://github.com/chriskempson/base16-schemes-source
"""

import os
import random
from dataclasses import dataclass

import yaml

palettes_dir = "palettes/"


def palette_files() -> list[str]:
    """Return a list of known palette files."""
    return [f for f in os.listdir(palettes_dir) if f.endswith(".yaml")]


def palettes() -> None:
    """Return a list of known palettes."""
    return [f.removesuffix(".yaml") for f in palette_files()]


def palette_path(palette: str) -> str:
    """Return the path for palette."""
    return os.path.join(palettes_dir, palette.removesuffix(".yaml") + ".yaml")


def palette_colors(palette: str) -> list[str]:
    """Return the palette colors for palette."""
    path = palette_path(palette)
    with open(path, encoding="utf-8") as f:
        colors: dict[str, str] = yaml.safe_load(f)
    return [
        "#" + value.lower()
        for key, value in colors.items()
        if key.startswith("base")
    ]


def print_colors(palette: str) -> None:
    """Print a numbered list of palette colors."""
    print("Palette:", palette)
    for i, c in enumerate(palette_colors(palette)):
        print(f"{i:2}: {c}")


@dataclass
class Palette:
    """Palette colors."""

    name: str = "ocean"
    colors: list[str] | None = None

    def __post_init__(self) -> None:
        """Set palette colors."""
        self.name = self.name.removesuffix(".yaml")
        self.colors = palette_colors(self.name)

    def color(self, n: int = 0) -> str:
        """Pick a color by index N."""
        max = len(self.colors) - 1
        return self.colors[n if n <= max else max]

    def random(self) -> str:
        """Return a random color."""
        return random.choice(self.colors)

    def range(self, a: int | None = None, b: int | None = None) -> str:
        """Return a random color between index A and B."""
        return random.choice(self.colors[a:b])
