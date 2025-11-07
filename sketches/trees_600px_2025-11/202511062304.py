import math
from random import randint

import py5

from lines import Point, Tree
from palettes import Palette
from tiles import Tile, tile_grid

p = Palette("spaceink")

size = 600


def setup() -> None:
    """Set py5."""
    py5.size(size, size)
    py5.background(p.colors[0])
    tile_size = 10
    for x, y in tile_grid(size, size, tile_size):
        tile = Tile(x, y, tile_size)
        tile.lines(p.color(1), 0.3, randint(0, 1))

    tile_size = 120
    c = [
        p.color(9),
        p.color(5),
        p.color(4),
        p.color(12),
        p.color(11),
        p.color(13),
    ]
    for x, y in tile_grid(size, size, tile_size):
        tree = Tree(
            Point(x + tile_size // 2, y + tile_size - 7),
            length=25,
            branches_num=randint(3, 6),
            branching_angle=math.radians(randint(30, 40)),
            max_depth=8,
            min_branch_length=1,
            length_reduction=0.87,
            line_weight=1.15,
            colors=c,
            symmetric=False,
        )
        tree.grow()
        tree.draw()

    py5.save("/tmp/tree.png")


py5.run_sketch()
