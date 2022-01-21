level_3 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXX",
"X            X           X",
"X         T  X           X",
"X    XXXXXXXXX    XXX    X",
"X                 X      X",
"X         T       X      X",
"XXXXXXXXXXXXXX    X      X",
"X            X    X   T  X",
"X            X    X      X",
"X     P      X    X      X",
"X                 X      X",
"X   XXXX          X      X",
"X   X  X     XXXXXX   X  X",
"X   X  X     X  T X   X  X",
"X   X  X          X   X  X",
"XXXXX  XXXXXXXXXXXX   XXXX",
"X                        X",
"X            T           X",
"X    XXX          XXXX   X",
"X      X     X    X      X",
"X      X     X    X      X",
"XXXX E X     X    X   X  X",
"X            X  T     X  X",
"X            X        X  X",
"XXXXXXXXXXXXXXXXXXXXXXXXXX",
]
wall_3 = []
for y in range(len(level_3)):
    for x in range(len(level_3[y])):
        character = level_3[y][x]
        screen_x = -338 + (x * 26)
        screen_y = 338 - (y * 26)
        if character == "X":
            wall_3.append((screen_x, screen_y))