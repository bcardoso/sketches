import py5
from color_theme import set_theme, pick_color
from tiles import tile_grid, tile_square_depth

set_theme("nord")

def setup():
    py5.size(600, 600)
    py5.smooth()
    py5.background(pick_color(0))
    tile_size = 50
    for x, y in tile_grid(py5.width, py5.height, tile_size):
        tile_square_depth(x, y, tile_size,
                          pick_color(0),
                          pick_color(range_a=4, range_b=16),
                          scale=2,
                          depth=12)

    py5.save('/tmp/static_sketch.png')

py5.run_sketch()
