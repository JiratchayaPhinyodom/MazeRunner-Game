
class Levels:
    """Maintains the objects which acn build the wall."""
    def __init__(self, painter):
        """Create painter in __init__."""
        self.painter = painter

    def draw(self):
        """Draw the function that create the block of wall."""
        self.painter.shape("square")
        self.painter.color("white")
        self.painter.penup()
        self.painter.speed(0)




