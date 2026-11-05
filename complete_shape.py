import math
import random
import sys
import time
import turtle


class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0):
        if sides < 3:
            raise ValueError("A polygon needs at least 3 sides.")
        if side_length <= 0:
            raise ValueError("side_length must be greater than 0.")
        if pen_size <= 0:
            raise ValueError("pen_size must be greater than 0.")

        self.x = x
        self.y = y
        self.sides = sides
        self.side_length = side_length
        self.color = color
        self.pen_size = pen_size
        self.angle = angle

        self._turtle = turtle.Turtle()
        self._turtle.hideturtle()
        self._turtle.speed(0)
        self._turtle.penup()

    def draw(self):
        t = self._turtle
        t.penup()
        t.goto(self.x, self.y)
        t.setheading(self.angle)
        t.color(self.color)
        t.pensize(self.pen_size)
        t.pendown()
        for _ in range(self.sides):
            t.forward(self.side_length)
            t.left(360 / self.sides)
        t.penup()

    def move_to(self, x, y):
        self.x = x
        self.y = y
        self._turtle.clear()
        self.draw()


def make_screen(title):
    screen = turtle.Screen()
    screen.setup(850, 600)
    screen.title(title)
    screen.bgcolor("black")
    screen.tracer(0)
    return screen


def static_art():
    screen = make_screen("Student Polygon Art")
    colors = ["cyan", "turquoise", "orange", "yellowgreen", "deepskyblue",
              "salmon", "plum", "lightgreen", "gold", "pink", "white"]
    rng = random.Random(12)

    polygons = []
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


def animated_art():
    screen = make_screen("Student Animated Polygon Art")
    rng = random.Random(17)
    colors = ["cyan", "springgreen", "orange", "deepskyblue", "plum", "yellow"]

    shapes = []
    for _ in range(12):
        x = rng.randint(-290, 210)
        y = rng.randint(-170, 120)
        shape = Polygon(x, y, rng.randint(3, 6), rng.randint(35, 105),
                        rng.choice(colors), rng.randint(1, 6),
                        rng.randint(0, 359))
        shape.draw()
        shapes.append((shape, x, y, rng.random() * 6.28))

    for frame in range(100):
        for shape, home_x, home_y, phase in shapes:
            x = home_x + 32 * math.cos(frame * 0.07 + phase)
            y = home_y + 23 * math.sin(frame * 0.07 + phase)
            shape.move_to(x, y)
        screen.update()
        time.sleep(0.045)

    screen.mainloop()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "animated":
        animated_art()
    else:
        static_art()