
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXX",
"X                  P     X",
"X         T              X",
"X  XXXXXXXXXXXXXXXXXXXXXXX",
"X                        X",
"X                        X",
"XXXXXXXXXXXXXXXXXXXXXXX  X",
"X   T                    X",
"X                        X",
"X  XXXXXXXXXXXXXXXXXXXXXXX",
"X T                      X",
"X                        X",
"XXXXXXXXXXXXXXXXXXXXXXX  X",
"X                  T     X",
"X                        X",
"X  XXXXXXXXXXXXXXXXXXXXXXX",
"X                        X",
"X          T             X",
"XXXXXXXXXXXXXXXXXXXXXXX  X",
"X                        X",
"X           T            X",
"X  XXXXXXXXXXXXXXXXXXXXXXX",
"X                        X",
"X                     E  X",
"XXXXXXXXXXXXXXXXXXXXXXXXXX",
]
wall_1 = []
for y in range(len(level_1)):
    for x in range(len(level_1[y])):
        character = level_1[y][x]
        screen_x = -338 + (x * 26)
        screen_y = 338 - (y * 26)
        if character == "X":
            wall_1.append((screen_x, screen_y))
