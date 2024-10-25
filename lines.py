from collections import namedtuple
import random
import math
import py5

Point = namedtuple("Point", ["x", "y"])

def random_point (x_min:int, x_max:int, y_min:int, y_max:int) -> Point:
    """Return a random point as a tuple."""
    return Point(random.randint(x_min, x_max), random.randint(y_min, y_max))

def distance (a:Point, b:Point) -> float:
    """Return the distance between points A and B."""
    return math.sqrt((b.x - a.x)**2 + (b.y - a.y)**2)

def midpoint (a:Point, b:Point) -> Point:
    """Return the midpoint between A and B."""
    return Point((a.x + b.x)/2, (a.y + b.y)/2)

def line (a:Point, b:Point, stroke:str="#000", stroke_weight:int=1):
    py5.stroke(stroke)
    py5.stroke_weight(stroke_weight)
    py5.line(a.x, a.y, b.x, b.y)
