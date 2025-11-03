import math
import random
from collections import namedtuple
from dataclasses import dataclass

import py5

Point = namedtuple("Point", ["x", "y"])


def random_point(x_min: int, x_max: int, y_min: int, y_max: int) -> Point:
    """Return a random point as a tuple."""
    return Point(random.randint(x_min, x_max), random.randint(y_min, y_max))


def distance(a: Point, b: Point) -> float:
    """Return the distance between points A and B."""
    return math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)


def midpoint(a: Point, b: Point) -> Point:
    """Return the midpoint between A and B."""
    return Point((a.x + b.x) / 2, (a.y + b.y) / 2)


def endpoint(
    a: Point, length: float, angle: float, degrees: bool = False
) -> Point:
    """Return the endpoint for length and angle.

    Args:
        a: Starting point
        length: Distance from starting point
        angle: Angle in radians (0 = east, -π/2 = north) or in degrees
        degrees: If True, consider angle in degrees

    """
    if degrees:
        angle = math.radians(angle)
    x = a.x + math.cos(angle) * length
    y = a.y + math.sin(angle) * length
    return Point(x, y)


def divide_points(x: float, n: int) -> list[float]:
    """Divide interval [-x, +x] into N equidistant points."""
    x = abs(x)
    if n > 1:
        n -= 1
        step = (2 * x) / n
        return [-x + i * step for i in range(n + 1)]
    else:
        return [random.choice([-x, x])]


@dataclass
class Line:
    """A line."""

    a: Point
    b: Point

    def draw(self, stroke: str = "#000", weight: int = 1) -> None:
        """Draw line."""
        py5.stroke(stroke)
        py5.stroke_weight(weight)
        py5.line(self.a.x, self.a.y, self.b.x, self.b.y)


@dataclass
class Tree:
    """A generative tree."""

    root: Point
    length: float = 120
    angle: float = -math.pi / 2
    depth: int = 0
    branches_num: int = 2
    branching_angle: float = math.pi / 5  # 36 degrees
    length_reduction: float = 0.75
    min_branch_length: float = 10
    max_depth: int = 10
    symmetric: bool = True
    line_weight: int = 3
    line_weight_relative: bool = False
    colors: str | list[str] | None = None

    def __post_init__(self) -> None:
        """Initialize branches."""
        self.branches = []

    def branch_color(self) -> str:
        """Return the branch color."""
        if self.colors is None:
            return "#000"
        elif isinstance(self.colors, str):
            return self.colors
        elif len(self.colors) > self.depth:
            return self.colors[self.depth]
        else:
            return self.colors[self.depth % len(self.colors)]

    def branch_line_weight(self) -> int:
        """Return the branch line weight."""
        if self.line_weight_relative:
            # Calculate line weight based on depth (thicker near trunk)
            return max(1, (self.max_depth - self.depth) * 1.5)
        else:
            return self.line_weight

    def branch_length(self) -> float:
        """Return the length of the branches."""
        if self.symmetric:
            length = self.length * self.length_reduction
        else:
            length = self.length * random.uniform(0.5, 0.8)
        return length

    def branches_angles(self) -> list[float]:
        """Return the angles of the branches."""
        if self.symmetric:
            angles = divide_points(self.branching_angle, self.branches_num)
        else:
            angles = divide_points(
                self.branching_angle, random.randint(2, self.branches_num)
            )
        return angles

    def grow(self) -> None:
        """Recursively grow the tree branches."""
        if (
            self.length < self.min_branch_length
            or self.depth >= self.max_depth
            or self.branches_num < 1
        ):
            return

        # Calculate end point
        self.end_point = endpoint(self.root, self.length, self.angle)

        # Create branches
        if self.depth < self.max_depth - 1:
            branches = []
            for angle in self.branches_angles():
                branches.append(
                    Tree(
                        self.end_point,
                        self.branch_length(),
                        self.angle + angle,
                        self.depth + 1,
                        self.branches_num,
                        symmetric=self.symmetric,
                        line_weight=self.branch_line_weight(),
                        line_weight_relative=self.line_weight_relative,
                        colors=self.colors,
                    )
                )

            self.branches.extend(branches)

        # Grow child branches recursively
        for branch in self.branches:
            branch.grow()

    def draw(self) -> None:
        """Draw this branch and all child branches recursively."""
        if not hasattr(self, "end_point"):
            return

        # Draw current branch
        line = Line(self.root, self.end_point)
        line.draw(self.branch_color(), self.branch_line_weight())

        # Draw child branches
        for branch in self.branches:
            branch.draw()
