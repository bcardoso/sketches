import py5
from color_theme import set_theme, pick_color
from tiles import tile_grid
from series import binary_seq
import math

set_theme("ocean")

def bit_tile (x, y, n, tile_size):
    part = math.floor(math.sqrt(len(n)))
    size = tile_size//part
    pos = 0
    for i in range(part):
        for j in range(part):
            if n[-1*pos]=='1':
                c = pick_color(range_a=8, range_b=8)
            else:
                c = pick_color(range_a=0, range_b=2)
            py5.fill(c)
            py5.stroke(1)
            py5.rect(x + i*size, y + j*size, size, size)
            pos += 1

def setup():
    py5.size(600, 600)
    py5.smooth()
    py5.background(pick_color(2))
    tile_size = 32
    bin_seq = binary_seq(bits=16, shuffle=False)
    for x, y in tile_grid(py5.width, py5.height, tile_size):
        bit_tile(x, y, next(bin_seq), tile_size)

    py5.save('/tmp/static_sketch.png')

py5.run_sketch()
