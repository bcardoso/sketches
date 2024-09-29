import py5
import random
from color_theme import set_theme, pick_color
from tiles import tile_triangle

set_theme("eighties")
tile_size = 100

def setup():
    py5.size(600, 600)
    py5.no_stroke()
    py5.background(pick_color(0))
    for x in range(0, py5.width, tile_size):
        for y in range(0, py5.height, tile_size):
            if (x+y)%2==0 or y==x+tile_size or y==x+tile_size*2:
                tile_triangle(x, y, tile_size,
                              pick_color(range_a=8),
                              random.randint(0, 3))

    py5.save('/tmp/static_sketch.png')

py5.run_sketch()
