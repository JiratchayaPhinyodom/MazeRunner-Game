import math
from Maze1 import wall_1
from Maze2 import wall_2
from Maze3 import wall_3
from Maze4 import wall_4
from Maze5 import wall_5
walls = [wall_1, wall_2, wall_3, wall_4, wall_5]

class Player:
    def __init__(self, painter):
        """Create painter and num_level = 0 in __init__."""
        self.painter = painter
        self.num_level = 0

    def draw(self):
        """Draw the character of player that cane move."""
        self.painter.register_shape("mushroom.gif")
        self.painter.shape("mushroom.gif")
        self.painter.penup()
        self.painter.speed(0)
        self.painter.point = 0


    def move_up(self):
        """Create the function that player can move up but can't move in to the walls."""
        if (self.painter.xcor(), self.painter.ycor() + 26) not in walls[self.num_level]:
            self.painter.goto(self.painter.xcor(), self.painter.ycor() + 26)

    def move_down(self):
        """Create the function that player can move down but can't move in to the walls."""
        if (self.painter.xcor(), self.painter.ycor() - 26) not in walls[self.num_level]:
            self.painter.goto(self.painter.xcor(), self.painter.ycor() - 26)

    def move_left(self):
        """Create the function that player can move left but can't move in to the walls."""
        if (self.painter.xcor() - 26, self.painter.ycor()) not in walls[self.num_level]:
            self.painter.goto(self.painter.xcor() - 26, self.painter.ycor())

    def move_right(self):
        """Create the function that player can move right but can't move in to the walls."""
        if (self.painter.xcor() + 26, self.painter.ycor()) not in walls[self.num_level]:
            self.painter.goto(self.painter.xcor() + 26, self.painter.ycor())

    def is_collision(self, other):
        """Create the function calculate distance that player move near other things if distance < 5 return true."""
        distance = math.sqrt((self.painter.xcor() - other.xcor())**2 + (self.painter.ycor() - other.ycor())**2)
        if distance < 5:
            return True
        else:
            return False





