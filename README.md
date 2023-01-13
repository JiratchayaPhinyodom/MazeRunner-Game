# Maze Runner Game
In this project, I implement a maze runner game, as shown.

# Overview
The rules are that the player must find the exit of the maze. 
And along the way there will be items to collect points.

# Modules
My project consists of seven modules,that completed by me.
In addition, keep a list of objects for 5 level of the maze.

## 1.Module `account.py`
This module contains the `PlayerAccount` class for creating each user account.

        class PlayerAccount:`
                def __init__(self, email, username, password, db):
                        self.email = email
                        self.username = username
                        self.password = password
                        self.db = db
                        db.register(self)

                def __repr__(self):
                        """The object representation can be changed by implementing the __repr__ method,
                which is required to a string."""

## 2.Module `database.py`
This module contains `AccountDB` class for creating a database format file.

        import json


        class AccountDB:
        def __init__(self, game):
            self.game = game
        
        
        def register(self, game_account):
            """Create game account in new_data to input the data in this function
        and create the condition if number of character = 0 will print Do not let any fields empty else ask a question
        if player want to save the account it's will save the data in file data.json."""
        
        def change_username(self, email, username, password, new_username):
            """Create the function that can change the username if email in the data.json file and correct username
        and password the username can be change in the data.json file."""

        def change_password(self, email, username, password, new_password):
            """Create the function that can change the password if email in the data.json file and correct username
        and password the password can be change in the data.json file."""
        
        def find_username(self, email, username):
            """Create the function that can find the username if email in data.json and correct username that will show 
        the account exists in the system."""

        def login(self, email, password):
            """Create the function that can login the account in this function before play game."""
        
        def logout(self, email, password):
            """Create the function that can logout after the game has end."""
        
        def __repr__(self):
            """The object representation can be changed by implementing the __repr__ method,
        which is required to a string."""

## 3. Module `Maze 1, Maze 2, Maze 3, Maze4 and Maze 5`
These modules are the objects of maze that can import the wall in to the `setup_maze.py` and `Gamster.py`.

## 4.Module `build_level.py`
This module contains the `Levels` class for creating the block of walls.

        class Levels:
            def __init__(self, painter):
                self.painter = painter
        
            def draw(self):
                """Draw the function that create the block of wall."""

## 5.Module `Items.py`
This module contains the `GoodItem(turtle.Turtle)` class for creating the good item.

        class GoodItem(turtle.Turtle):
            """Create class that are the turtle function."""
            def __init__(self, x, y):
                turtle.Turtle.__init__(self)
                self.shape("water.gif")
                self.penup()
                self.point = 100
                self.goto(x, y)
        
            def destroy(self):
                """Create the function that can hide the turtle of item."""

## 6. Module `exit.py`
This module contains the `Exit(turtle.Turtle)` class for creating the door.

        class Exit(turtle.Turtle):
            def __init__(self, x, y):
                turtle.Turtle.__init__(self)
                self.shape("door.gif")
                self.color("Black")
                self.penup()
                self.goto(x, y)
        
            def destroy_exit(self):
                """Create the function that can hide the turtle of door."""

## 7.Module `Gamster.py`
This module contains the `Player` class for creating the character of player and setting the limit of player's movement.

        class Player:
            def __init__(self, painter):
                self.painter = painter
                self.num_level = 0
        
            def draw(self):
                """Draw the character of player that cane move."""
        
            def move_up(self):
                """Create the function that player can move up but can't move in to the walls."""

            def move_down(self):
                """Create the function that player can move down but can't move in to the walls."""

            def move_left(self):
                """Create the function that player can move left but can't move in to the walls."""
        
            def move_right(self):
                """Create the function that player can move right but can't move in to the walls."""

            def is_collision(self, other):
                """Create the function calculate distance that player move near other things 
            if distance < 5 return true."""

## 8. Module `setup_maze.py`
This module contains the `setup_maze(levels)` and `player_move()` function for set the screen of the game, 
draw the walls of each level, set the player's key moves and set the conditions when player crashes into objects.

#Running Tests
Tests can be performed by running the `main.py`.

