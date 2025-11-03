import random

import py5

from palettes import Palette
from tiles import Tile, tile_grid

p = Palette("eighties")

size = 600
tile_size = 30


def setup() -> None:
    """Set py5."""
    py5.size(size, size)
    py5.no_stroke()
    py5.background(p.color(0))

    for x, y in tile_grid(py5.width, py5.height, tile_size):
        tile = Tile(x, y, tile_size)
        tile.triangle(p.random(2, 8), random.randint(0, 3))

    py5.save("/tmp/static_sketch.png")


py5.run_sketch()
