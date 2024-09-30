import py5
import random
from color_theme import set_theme, pick_color
from tiles import tile_grid, tile_line

set_theme("default-dark")
tile_size = 12

def setup():
    py5.size(600, 600)
    py5.background(pick_color())
    py5.stroke_cap(py5.PROJECT)

    def prob(p=0.5):
        return random.randint(0,100) < p*100

    def rand(n=1):
        return random.randint(0, n)

    sw=4
    for x, y in tile_grid(py5.width, py5.height, tile_size):
        if prob(0.1):
            tile_line(x, y, tile_size, pick_color(15), sw, rand())
        if prob(0.15):
            tile_line(x, y, tile_size, pick_color(9), sw, rand())
        if prob(0.20):
            tile_line(x, y, tile_size, pick_color(10), sw, rand())

    py5.save('/tmp/static_sketch.png')

py5.run_sketch()
