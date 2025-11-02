import math
from dataclasses import dataclass
from textwrap import fill

import py5


def tile_grid(width: int, height: int, tile_size: int) -> tuple[int, int]:
    """Return the points of a tile grid.

    Yields:
        tuple[int, int]: The point in the tile grid.

    """
    for x in range(0, width, tile_size):
        for y in range(0, height, tile_size):
            yield (x, y)


@dataclass
class Tile:
    """A tile."""

    x: float
    y: float
    size: float
    fill_color: str | None = None

    def square(self, color: str | None = None) -> None:
        """Draw squared tile."""
        py5.fill(color or self.fill_color)
        py5.stroke(color or self.fill_color)
        py5.rect(self.x, self.y, self.size, self.size)

    def layered_squares(
        self,
        fill_color1: str,
        fill_color2: str,
        scale: float = 10.0,
        layers: int = 7,
    ) -> None:
        """Draw layered squares within tile."""
        for d in range(layers + 1):
            self.square(
                self.x + (d * scale),
                self.y + (d * scale),
                self.size - (2 * d * scale),
                fill_color1 if d % 2 == 0 else fill_color2,
            )

    def triangle(self, color: str, r: int = 0) -> None:
        """Draw a triangle within tile."""
        py5.fill(color)
        py5.stroke(color)
        x, y, size = self.x, self.y, self.size
        if r == 0:
            # ◸ upper left
            py5.triangle(x, y, x, y + size, x + size, y)
        elif r == 1:
            # ◹ upper right
            py5.triangle(x, y, x + size, y, x + size, y + size)
        elif r == 2:
            # ◿ lower right
            py5.triangle(x, y + size, x + size, y, x + size, y + size)
        else:
            # ◺ lower left
            py5.triangle(x, y, x, y + size, x + size, y + size)

    def arcs(self, color: str, weight: float = 3.0, r: int = 0) -> None:
        """Draw composable arcs within tile."""
        py5.no_fill()
        py5.stroke(color)
        py5.stroke_weight(weight)
        x, y, size = self.x, self.y, self.size
        if r == 0:
            py5.arc(x, y, size, size, 0, py5.PI / 2)
            py5.arc(
                x + size, y + size, size, size, py5.PI, py5.PI + py5.PI / 2
            )
        else:
            py5.arc(x + size, y, size, size, py5.PI / 2, py5.PI)
            py5.arc(x, y + size, size, size, py5.PI + py5.PI / 2, 2 * py5.PI)

    def lines(self, color: str, weight: float = 3.0, r: int = 0) -> None:
        """Draw composable lines within tile."""
        py5.no_fill()
        py5.stroke(color)
        py5.stroke_weight(weight)
        x, y, size = self.x, self.y, self.size
        if r == 0:
            py5.line(x, y + size / 2, x + size / 2, y)
            py5.line(x + size / 2, y + size, x + size, y + size / 2)
        else:
            py5.line(x, y + size / 2, x + size / 2, y + size)
            py5.line(x + size / 2, y, x + size, y + size / 2)

    def bits(
        self,
        binary: str,
        color0: str,
        color1: str,
        stroke_color: str | None = None,
    ) -> None:
        """Draw squared binary bits within tile."""
        x, y, size = self.x, self.y, self.size
        part = math.floor(math.sqrt(len(binary)))
        size //= part
        pos = 0
        for i in range(part):
            for j in range(part):
                c = color1 if binary[-1 * pos] == "1" else color0
                py5.fill(c)
                py5.stroke(stroke_color or c)
                py5.rect(x + i * size, y + j * size, size, size)
                pos += 1
