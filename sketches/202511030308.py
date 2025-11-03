from dataclasses import dataclass

import py5

from lines import Point, Tree
from palettes import Palette

p = Palette("default-dark")

size = 600


def setup() -> None:
    """Set py5."""
    py5.size(size, size)
    py5.background(p.colors[0])

    tree = Tree(
        Point(size // 2, size - 70),
        length=120,
        branches_num=8,
        branching_angle=0.666,
        max_depth=16,
        min_branch_length=5,
        length_reduction=0.75,
        line_weight=1.75,
        colors=p.range(9),
        symmetric=False,
    )
    tree.grow()
    tree.draw()

    py5.save("/tmp/tree.png")


py5.run_sketch()
