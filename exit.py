import turtle
turtle.register_shape("door.gif")

class Exit(turtle.Turtle):
    """Create class that are the turtle function."""
    def __init__(self, x, y):
        """Create the turtle is __init__, create shape of door."""
        turtle.Turtle.__init__(self)
        self.shape("door.gif")
        self.color("Black")
        self.penup()
        self.goto(x, y)

    def destroy_exit(self):
        """Create the function that can hide the turtle of door."""
        self.hideturtle()
