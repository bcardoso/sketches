import py5
from color_theme import set_theme, pick_color
from tiles import tile_grid, tile_bits
from series import binary_seq

set_theme("mocha")

def setup():
    py5.size(600, 600)
    py5.smooth()
    py5.background(pick_color(2))
    tile_size = 30
    bin_seq = binary_seq(bits=9, shuffle=False)
    for x, y in tile_grid(py5.width, py5.height, tile_size):
        tile_bits(x, y, tile_size,
                  next(bin_seq),
                  pick_color(range_a=1, range_b=3),
                  pick_color(range_a=8, range_b=15),
                  pick_color(1))

    py5.save('/tmp/static_sketch.png')

py5.run_sketch()
