import turtle
from build_level import Levels
from Gamster import Player
from Items import GoodItem
from Maze1 import level_1
from Maze2 import level_2
from Maze3 import level_3
from Maze4 import level_4
from Maze5 import level_5
from exit import Exit


Items = []
enemies = []
exit = []
key = []
door = []
player = Player(turtle)
levels = [level_1, level_2, level_3, level_4, level_5]

def setup_maze(levels):
    """Set up the screen and get the character at each x, y coordinate, calculate the screen x, y coordinates
    and check if it is an each character to representing a component of a game."""
    set_up = turtle.Screen()
    player = Player(turtle)
    level = Levels(turtle.Turtle())
    set_up.tracer(0)
    set_up.bgcolor("pink")
    set_up.title("Maze King Game")
    set_up.setup(800, 800)
    for y in range(len(levels)):
        for x in range(len(levels[y])):
            character = levels[y][x]
            screen_x = -338 + (x * 26)
            screen_y = 338 - (y * 26)
            if character == "E":
                exit.append(Exit(screen_x, screen_y))

            if character == "X":
                level.draw()
                level.painter.goto(screen_x, screen_y)
                level.painter.stamp()

            if character == "P":
                player.draw()
                player.painter.goto(screen_x, screen_y)

            if character == "T":
                Items.append(GoodItem(screen_x, screen_y))

def player_move():
    player.painter.listen()
    player.painter.onkey(player.move_right, "Right")
    player.painter.onkey(player.move_up, "Up")
    player.painter.onkey(player.move_down, "Down")
    player.painter.onkey(player.move_left, "Left")
    point = []
    for Item in Items:
        if player.is_collision(Item):
            player.painter.point += Item.point
            print("Player Point: {}".format(player.painter.point))
            Item.destroy()
            Items.remove(Item)
    for ex in exit:
        if player.is_collision(ex):
            point.append(player.painter.point)
            ex.destroy_exit()
            exit.remove(ex)
            player.num_level += 1
            print(f"In this level you got {sum(point)}/600")
            print("You win")