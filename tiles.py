import py5

tile_size = 50

def tile_square (x, y, size, fill):
    py5.fill(fill)
    py5.stroke(fill)
    py5.rect(x, y, x+size, y+size)

def tile_triangle (x, y, size, fill, r=0):
    py5.fill(fill)
    py5.stroke(fill)
    if r == 0:
        # ◸ upper left
        py5.triangle(x,y, x,y+size, x+size,y)
    elif r == 1:
        # ◹ upper right
        py5.triangle(x,y, x+size,y, x+size,y+size)
    elif r == 2:
        # ◿ lower right
        py5.triangle(x,y+size, x+size,y, x+size,y+size)
    else:
        # ◺ lower left
        py5.triangle(x,y, x,y+size, x+size,y+size)
