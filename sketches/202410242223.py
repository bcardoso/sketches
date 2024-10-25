import py5
import random
from color_theme import set_theme, pick_color
from lines import random_point, distance, midpoint

set_theme("nord")

def setup():
    py5.size(600, 600)
    py5.smooth()
    py5.background(pick_color(0))

    def p ():
        offset = 20
        return random_point(offset, py5.width-offset,
                            offset, py5.height-offset)

    while True:
        a, b, c = p(), p(), p()
        if distance(a,b)>500 and distance(b,c)>500 and distance(c,a)>500:
            break

    py5.stroke_weight(5)
    py5.stroke(pick_color(5))
    py5.point(a.x, a.y)
    py5.point(b.x, b.y)
    py5.point(c.x, c.y)
    s = p()
    for _ in range(0, 5000):
        r = random.randint(1, 6)
        if r <= 2:
            s = midpoint(s, a)
        elif r <= 4:
            s = midpoint(s, b)
        else:
            s = midpoint(s, c)
        py5.stroke(pick_color(any=True))
        py5.point(s.x, s.y)

    py5.save('/tmp/static_sketch.png')

py5.run_sketch()
