import turtle
from Maze1 import wall_1
from Maze2 import wall_2
from Maze3 import wall_3
from Maze4 import wall_4
from Maze5 import wall_5
walls = [wall_1, wall_2, wall_3, wall_4, wall_5]

turtle.register_shape("water.gif")
class GoodItem(turtle.Turtle):
    """Create class that are the turtle function."""
    def __init__(self, x, y):
        """Create the turtle is __init__, create shape of item."""
        turtle.Turtle.__init__(self)
        self.shape("water.gif")
        self.penup()
        self.point = 100
        self.goto(x, y)

    def destroy(self):
        """Create the function that can hide the turtle of item."""
        self.hideturtle()
