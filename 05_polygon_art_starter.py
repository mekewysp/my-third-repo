"""EXERCISE: make overlapping polygon art like the reference image.
Complete polygon_shape.py first. Then adjust the parameters below to
create your own composition. The example uses a black background.
"""
import turtle
import random
from polygon_shape import Polygon

screen = turtle.Screen()
screen.setup(850, 600)
screen.title("Student Polygon Art")
screen.bgcolor("black")
screen.tracer(0)  # We draw the whole scene before refreshing the screen.

colors = ["cyan", "turquoise", "orange", "yellowgreen", "deepskyblue",
          "salmon", "plum", "lightgreen", "gold", "pink", "white"]
rng = random.Random(12)

polygons = []  # Hold references so the Polygon objects remain accessible.
for _ in range(20):
    sides = rng.randint(3, 6)
    side_length = rng.randint(35, 120)
    x = rng.randint(-350, 260)
    y = rng.randint(-225, 180)
    color = rng.choice(colors)
    pen_size = rng.randint(1, 7)
    angle = rng.randint(0, 359)
    polygon = Polygon(x, y, sides, side_length, color, pen_size, angle)
    polygon.draw()
    polygons.append(polygon)

screen.update()
screen.mainloop()
