import py5
import math

def tile_grid (width, height, size):
    for x in range(0, width, size):
        for y in range(0, height, size):
            yield (x, y)

def tile_square (x, y, size, fill):
    py5.fill(fill)
    py5.stroke(fill)
    py5.rect(x, y, size, size)

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

def tile_arc (x, y, size, color, weight=3, r=0):
    py5.no_fill()
    py5.stroke(color)
    py5.stroke_weight(weight)
    if r == 0:
        py5.arc(x,y, size,size, 0, py5.PI/2)
        py5.arc(x+size, y+size, size,size, py5.PI, py5.PI+py5.PI/2)
    else:
        py5.arc(x+size, y, size,size, py5.PI/2,py5.PI)
        py5.arc(x, y+size, size,size, py5.PI+py5.PI/2,2*py5.PI)

def tile_line (x, y, size, color, weight=3, r=0):
    py5.no_fill()
    py5.stroke(color)
    py5.stroke_weight(weight)
    if r == 0:
        py5.line(x,y+size/2, x+size/2,y)
        py5.line(x+size/2,y+size, x+size,y+size/2)
    else:
        py5.line(x,y+size/2, x+size/2,y+size)
        py5.line(x+size/2,y, x+size,y+size/2)

def tile_bits (x, y, size, bits, c0, c1, cs=None):
    part = math.floor(math.sqrt(len(bits)))
    size = size//part
    pos = 0
    for i in range(part):
        for j in range(part):
            if bits[-1*pos]=='1':
                c = c1
            else:
                c = c0
            py5.fill(c)
            py5.stroke(cs or c)
            py5.rect(x + i*size, y + j*size, size, size)
            pos += 1
