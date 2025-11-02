import py5
import random
from color_theme import set_theme, pick_color
from tiles import tile_grid, tile_triangle, tile_square

set_theme("eighties")
tile_size = 75

def setup():
    py5.size(600, 600)
    py5.no_stroke()
    py5.background(pick_color(0))
    for x, y in tile_grid(py5.width, py5.height, tile_size):
        tile_triangle(x, y, tile_size,
                      pick_color(range_a=1, range_b=6),
                      random.randint(0, 3))

    py5.save('/tmp/static_sketch.png')

py5.run_sketch()
