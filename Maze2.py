level_2 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXX",
"X     X P X              X",
"X     X   X              X",
"X  XXXX   XXXXXXXXXXXXX  X",
"X  X  X               X  X",
"X  X  X        T      X  X",
"X  X  XXXXXXXXXXXXXX  X  X",
"X  X               X  X  X",
"X                  X  X  X",
"X    T   XXXXXXXX  X  X  X",
"X        X  T   X  X  X  X",
"X  X     X      X  X  X  X",
"X  XXXXXXX  XXXXX  X  X  X",
"X  X     X         X  X  X",
"X  X     X         X  X  X",
"X  X     XXXXXXXX  X  X  X",
"X  X  X            X  X  X",
"X  X  X     T      X  X  X",
"X  X  XXXXXXXXXXXXXX  X  X",
"X  X           T      X  X",
"X  X                  X  X",
"X  XXXXXXXXXXXXXXXXXXXX  X",
"X                        X",
"X      T                 X",
"XXXXXXXXXXXXXXXXX E XXXXXX",
]

wall_2 = []
for y in range(len(level_2)):
    for x in range(len(level_2[y])):
        character = level_2[y][x]
        screen_x = -338 + (x * 26)
        screen_y = 338 - (y * 26)
        if character == "X":
            wall_2.append((screen_x, screen_y))