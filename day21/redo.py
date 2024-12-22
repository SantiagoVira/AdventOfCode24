import sys
sys.path.append("..")
from helpers import *  # noqa

# Parse input
codes = parse_input("./input.txt", Parse.lines)

numpad = {
    "char_to_pos": {
        "9": (2, 0),
        "8": (1, 0),
        "7": (0, 0),
        "6": (2, 1),
        "5": (1, 1),
        "4": (0, 1),
        "3": (2, 2),
        "2": (1, 2),
        "1": (0, 2),
        "0": (1, 3),
        "A": (2, 3)
    },
}
numpad["pos_to_char"] = {v: k for k, v in numpad["char_to_pos"].items()}

robopad = {
    "char_to_pos": {
        "^": (1, 0),
        "A": (2, 0),
        "<": (0, 1),
        "v": (1, 1),
        ">": (2, 1)
    }
}
robopad["pos_to_char"] = {v: k for k, v in robopad["char_to_pos"].items()}

data = [numpad, robopad]


# @cache
# def path_from_to(fr, to, pad):
#     pad = data[pad]
#     if fr == to:
#         return "A"
#     from_pos, to_pos = pad["char_to_pos"][fr], pad["char_to_pos"][to]
#     dx, dy = to_pos[0] - from_pos[0], to_pos[1] - from_pos[1]
#     horizontal = "<"*abs(dx) if dx < 0 else ">"*abs(dx) if dx > 0 else ""
#     vertical = "^"*abs(dy) if dy < 0 else "v"*abs(dy) if dy > 0 else ""

#     if dx == 0:
#         return vertical + "A"
#     if dy == 0:
#         return horizontal + "A"

#     if dx > 0 and (from_pos[0], to_pos[1]) in pad["pos_to_char"]:
#         return vertical + horizontal + "A"
#     elif (to_pos[0], from_pos[1]) in pad["pos_to_char"]:
#         return horizontal + vertical + "A"

#     return vertical + horizontal + "A"


# @cache
# def get_path(code, pad):
#     path = ""
#     sym = "A"
#     for c in code:
#         path += path_from_to(sym, c, pad)
#         sym = c
#     return path


# total = 0

# for code in codes:
#     path = get_path(code, 0)
#     print("".join(code))
#     for i in range(25):
#         print(i)
#         path = get_path(path, 1)
#     numeric_code = int("".join(c for c in code if c.isnumeric()))
#     print(len(path), numeric_code)
#     total += len(path) * numeric_code

# print(total)


def path_from_to(fr, to, pad):
    pad = data[pad]
    if fr == to:
        return "A"
    from_pos, to_pos = pad["char_to_pos"][fr], pad["char_to_pos"][to]
    dx, dy = to_pos[0] - from_pos[0], to_pos[1] - from_pos[1]
    horizontal = "<"*abs(dx) if dx < 0 else ">"*abs(dx) if dx > 0 else ""
    vertical = "^"*abs(dy) if dy < 0 else "v"*abs(dy) if dy > 0 else ""

    if dx == 0:
        return vertical + "A"
    if dy == 0:
        return horizontal + "A"

    if dx > 0 and (from_pos[0], to_pos[1]) in pad["pos_to_char"]:
        return vertical + horizontal + "A"
    elif (to_pos[0], from_pos[1]) in pad["pos_to_char"]:
        return horizontal + vertical + "A"

    return vertical + horizontal + "A"


def get_path(code, pad):
    path = []
    sym = "A"
    for c in code:
        path += path_from_to(sym, c, pad)
        sym = c
    return Counter(path)


total = 0

for code in codes:
    path = get_path(code, 0)
    print("".join(code))
    for i in range(25):
        print(i)
        path = get_path(path, 1)
    numeric_code = int("".join(c for c in code if c.isnumeric()))
    print(len(path), numeric_code)
    total += len(path) * numeric_code

print(total)
