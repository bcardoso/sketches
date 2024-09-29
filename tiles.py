import py5
import random
import yaml

# * Color theme

base16_yaml = "/home/bruno/bin/git/base16-default-schemes/ocean.yaml"

def load_base16_palette (file_path):
    with open(file_path, 'r') as f:
        palette_data = yaml.safe_load(f)
    return ["#" + color for color in list(palette_data.values())[2:]]

palette = load_base16_palette(base16_yaml)

def color_picker (n=1, any=False, range_a=None, range_b=None):
    if any or isinstance(range_a, int) or isinstance(range_b, int):
        return random.choice(palette[range_a:range_b])
    else:
        return palette[n]


# * Tiles

tile_size = 40

def tile_square (x, y, size, fill):
    py5.fill(fill)
    py5.stroke(fill)
    py5.stroke_weight(0)
    py5.rect(x, y, x+size, y+size)

def tile_triangle (x, y, size, fill, r=0):
    py5.fill(fill)
    py5.stroke(fill)
    py5.stroke_weight(0)
    if r == 0:
        # ◸ upper left
        py5.triangle(x,y, x,y+size, x+size,y)
    elif r == 1:
        # ◺ lower left
        py5.triangle(x,y, x,y+size, x+size,y+size)
    elif r == 2:
        # ◹ upper right
        py5.triangle(x,y, x+size,y, x+size,y+size)
    else:
        # ◿ lower right
        py5.triangle(x,y+size, x+size,y, x+size,y+size)


# * Setup

def setup():
    py5.size(520, 520)
    # py5.background('#004477') # dark blue background
    # py5.no_smooth()
    # py5.no_loop()
    py5.frame_rate(8)
    for x in range(0, py5.width, tile_size):
        for y in range(0, py5.height, tile_size):
            tile_square(x, y, tile_size, color_picker(range_a=9))
            tile_triangle(x, y, tile_size, color_picker(7), r=0)

    py5.save('/tmp/static_sketch.png')

def draw():
    for x in range(0, py5.width, tile_size):
        for y in range(0, py5.height, tile_size):
            tile_square(x, y, tile_size, color_picker(range_a=9))
            tile_triangle(x, y, tile_size,
                          color_picker(any=True), random.randint(0, 3))

py5.run_sketch()
