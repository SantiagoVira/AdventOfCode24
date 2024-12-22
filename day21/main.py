import sys
sys.path.append("..")
from helpers import *  # noqa

# Parse input
codes = parse_input("./input.txt", Parse.chars2d)

map1 = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["", "0", "A"]
]
map2 = [
    ["", "^", "A"],
    ["<", "v", ">"]
]


def from_to(map):
    from_to_paths = {}
    dead_y = [i for i in range(len(map)) if "" in map[i]][0]
    dead_x = map[dead_y].index("")

    for y0 in range(len(map)):
        for x0 in range(len(map[0])):
            for yf in range(len(map)):
                for xf in range(len(map[0])):
                    if map[yf][xf] != "" and map[y0][x0] != "":
                        dx, dy = (xf - x0), (yf - y0)
                        xmove, ymove = ">" if dx > 0 else "<" if dx < 0 else "", "v" if dy > 0 else "^" if dy < 0 else ""

                        if dx == 0 and dy == 0:
                            path = "A"
                        elif dx == 0:
                            path = ymove * abs(dy) + "A"
                        elif dy == 0:
                            path = xmove * abs(dx) + "A"
                        elif y0 == dead_y and xf == dead_x:
                            path = ymove * abs(dy) + xmove * abs(dx) + "A"
                        elif x0 == dead_x and yf == dead_y:
                            path = xmove * abs(dx) + ymove * abs(dy) + "A"
                        else:
                            path = ymove * abs(dy) + xmove * abs(dx) + "A"
                        from_to_paths[(map[y0][x0], map[yf][xf])] = path

    return from_to_paths


def get_seqs(map, code):
    y = [i for i in range(len(map)) if "A" in map[i]][0]
    x = map[y].index("A")

    dead_y = [i for i in range(len(map)) if "" in map[i]][0]
    dead_x = map[dead_y].index("")

    seq = ""
    moves = deque([(x, y, "", 0, set())])

    for char in code:
        yf = [i for i in range(len(map)) if char in map[i]][0]
        xf = map[yf].index(char)
        # dx > 0: right, dy > 0: down
        dx, dy = (xf - x), (yf - y)
        xmove, ymove = ">" if dx > 0 else "<" if dx < 0 else "", "v" if dy > 0 else "^" if dy < 0 else ""

        if dx == 0 and dy == 0:
            path = "A"
        elif dx == 0:
            path = ymove * abs(dy) + "A"
        elif dy == 0:
            path = xmove * abs(dx) + "A"
        elif y == dead_y and xf == dead_x:
            path = ymove * abs(dy) + xmove * abs(dx) + "A"
        else:
            path = xmove * abs(dx) + ymove * abs(dy) + "A"
            # moves = xmove * abs(dx) + ymove * abs(dy)
            # perm_paths = [
            #     "".join(p) + "A" for p in set(itertools.permutations(moves))]
            # new_seqs = []
            # # print(perm_paths)
            # for np in perm_paths:
            #     if x == dead_x and yf == dead_y and np.startswith(abs(dy) * ymove):
            #         continue
            #     if y == dead_y and xf == dead_x and np.startswith(abs(dx) * xmove):
            #         continue
            #     if not seqs:
            #         new_seqs.append(np)
            #     else:
            #         for s in seqs:
            #             new_seqs.append(s + np)
            # seqs = new_seqs

        x, y = xf, yf
        # if dx == 0 or dy == 0:
        #     # print(path)
        #     if not seqs:
        #         seqs.append(path)
        #     else:
        #         for i in range(len(seqs)):
        #             seqs[i] += path
        # print(seqs)

        seq += path

    return seq


def assemble_seq(map, code):
    from_to_paths = from_to(map)
    # if ("A", "<") in map:
    #     map[("A", "<")] = "<v<"
    sym = "A"
    seq = ""
    for c in code:
        seq += from_to_paths[(sym, c)]
        sym = c
    return seq


total = 0

# print(get_seqs(map2, '<A^A>^^AvvvA'))

for code in codes:
    NUM_ROBOTS = 2  # 25
    seq = assemble_seq(map1, code)
    if code == ['8', '6', '9', 'A']:
        print("869A")
        print(seq)

    for i in range(NUM_ROBOTS):
        seq = assemble_seq(map2, seq)
        if code == ['8', '6', '9', 'A']:
            print(seq)

    total += len(seq) * int("".join(c for c in code if c.isnumeric()))

print(total)

'''
Code: 379A
^A<<^^A>>AvvvA
<A>Av<<AA>^AA>AvAA^A<vAAA>^A
<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
'''


# x, y = 2, 0
# seq = "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"
# for i in range(2):
#     new_seq = ""
#     for c in seq:
#         if c == "^":
#             y -= 1
#         elif c == ">":
#             x += 1
#         elif c == "v":
#             y += 1
#         elif c == "<":
#             x -= 1
#         else:
#             new_seq += map2[y][x]
#     print(new_seq)
#     seq = new_seq
