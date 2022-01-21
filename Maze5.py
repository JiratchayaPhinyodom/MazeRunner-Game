level_5 = [
"X P XXXXXXXXXXXXXXXXXXXXXX",
"X                 X      X",
"X                 X      X",
"XXXXX   XXXXXX    X  XXXXX",
"X       X         X      X",
"X   T   X         X      X",
"XXXXXXXXX         XXXX   X",
"X                 X      X",
"X  T      X       X      X",
"X     X   X    XXXX      X",
"X     X   X    X      T  X",
"X     X   X    X         X",
"X  XXXXXXXX    XXXX   XXXX",
"X  X           X      X  X",
"X  X        XXXX      X  X",
"X  XXX                   X",
"X    X       T           X",
"X    X                XXXX",
"XXX  X  XXXXXXXXXXX      X",
"X    X  X                X",
"X    X  X    T           X",
"X  XXX  XXXXX    X    XXXX",
"X    X   T  X    X       X",
"X    X      X    X       X",
"XXXXXXXXXXXXXXXXXXXXXX E X",
]
wall_5 = []
for y in range(len(level_5)):
    for x in range(len(level_5[y])):
        character = level_5[y][x]
        screen_x = -338 + (x * 26)
        screen_y = 338 - (y * 26)
        if character == "X":
            wall_5.append((screen_x, screen_y))