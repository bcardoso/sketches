import py5
import random
from color_theme import set_theme, pick_color
from tiles import tile_grid, tile_arc

set_theme("dracula")

def setup():
    py5.size(600, 600)
    py5.smooth()
    py5.background(pick_color(0))
    tile_size = 25
    for x, y in tile_grid(py5.width, py5.height, tile_size):
        tile_arc(x, y, tile_size, pick_color(11), 1, random.randint(0,1))
        tile_arc(x, y, tile_size+y/6, pick_color(range_a=10, range_b=15), 2, random.randint(0,1))

    py5.save('/tmp/static_sketch.png')

py5.run_sketch()
