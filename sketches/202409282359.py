import py5
import random
from color_theme import set_theme, pick_color
from tiles import tile_square, tile_triangle

set_theme("ocean")
tile_size = 40

def setup():
    py5.size(600, 600)
    py5.no_stroke()
    py5.frame_rate(8)
    for x in range(0, py5.width, tile_size):
        for y in range(0, py5.height, tile_size):
            tile_square(x, y, tile_size, pick_color(range_a=9))
            tile_triangle(x, y, tile_size,
                          pick_color(range_a=2, range_b=8),
                          random.randint(0, 3))

    py5.save('/tmp/static_sketch.png')

# def draw():
#     for x in range(0, py5.width, tile_size):
#         for y in range(0, py5.height, tile_size):
#             tile_square(x, y, tile_size, pick_color(range_a=9))
#             tile_triangle(x, y, tile_size,
#                           pick_color(any=True),
#                           random.randint(0, 3))

py5.run_sketch()
