"""EXERCISE: finish the Polygon class. Use import turtle (not selective imports)."""
import turtle


class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0):
        """Store the first vertex, number of sides, side length, color,
        line width, angle, and an internal turtle.Turtle object.
        Reject sides < 3, side_length <= 0, and pen_size <= 0.
        """
        # TODO: initialize your object's state and its own turtle.Turtle()
        raise NotImplementedError

    def draw(self):
        """Draw a regular polygon using left(360 / sides)."""
        # TODO: lift pen; go to starting vertex; set heading/color/pensize;
        #       lower pen; draw sides; lift pen.
        raise NotImplementedError

    def move_to(self, x, y):
        """Update the starting vertex; clear only this polygon; redraw."""
        # TODO: update this object's position, then clear and redraw.
        raise NotImplementedError
