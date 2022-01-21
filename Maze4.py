level_4 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXX",
"X       X          X     X",
"X       X          X     X",
"X   X   X  X  X    XXXX  X",
"X   X   X  X  X          X",
"X   XXXXX  X  X          X",
"X   X      X  X      P   X",
"X   X      X  X          X",
"X   X      X  X          X",
"X   X  T   X  XXXXXXXX   X",
"X   X      X  X      X   X",
"X   X      X  X      X   X",
"X   X      X     X   XXXXX",
"X   X   XXXX  T  X       X",
"X   X   X  X     X     T X",
"X   X   X  XXXXXXXXXXX   X",
"X   X   X            X   X",
"X   X   X  T         X   X",
"X   X   XXXXX    X   X   X",
"X   X  T    X    X   X   X",
"X   X       X    X   X   X",
"X   XXXXX   X  T X   X   X",
"X                X   X   X",
"X                X   X   X",
"XXX E XXXXXXXXXXXXXXXXXXXX",
]
wall_4 = []
for y in range(len(level_4)):
    for x in range(len(level_4[y])):
        character = level_4[y][x]
        screen_x = -338 + (x * 26)
        screen_y = 338 - (y * 26)
        if character == "X":
            wall_4.append((screen_x, screen_y))