import py5
import random
from color_theme import set_theme, pick_color
from tiles import tile_grid, tile_line

set_theme("dracula")

def setup():
    py5.size(600, 600)
    py5.background(pick_color(0))
    py5.stroke_cap(py5.PROJECT)
    tile_size = 20
    for x, y in tile_grid(py5.width, py5.height, tile_size):
        py5.point(x, y)
        tile_line(x, y, tile_size, pick_color(10), 3, random.randint(0,1))
    tile_size = 40
    for x, y in tile_grid(py5.width, py5.height, tile_size):
        tile_line(x, y, tile_size, pick_color(12), 3, random.randint(0,1))

    py5.save('/tmp/static_sketch.png')

py5.run_sketch()
