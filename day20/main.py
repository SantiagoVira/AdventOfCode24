import sys
sys.path.append("..")
from helpers import *  # noqa

# Parse input
data = parse_input("./input.txt", Parse.chars2d)
y0 = [i for i in range(len(data)) if "S" in data[i]][0]
x0 = data[y0].index("S")


def get_min_path(data, x0, y0):
    positions = deque([(x0, y0, 0)])
    min_path = -1
    seen = set()

    while positions:
        x, y, num_moves = positions.popleft()

        if (x, y) in seen:
            continue

        if data[y][x] == "E":
            min_path = num_moves
            break

        seen.add((x, y))

        for (nx, ny) in cardinal_moves_indicies(len(data[0]), len(data), x, y):
            if data[ny][nx] != "#":
                positions.append((nx, ny, num_moves + 1))

    return min_path


moves = []
positions = deque([(x0, y0)])
move_indices = {}
num_moves = 0

while positions:
    x, y = positions.popleft()

    if (x, y) in move_indices:
        continue

    moves.append((x, y))
    move_indices[(x, y)] = num_moves

    if data[y][x] == "E":
        break

    num_moves += 1

    for (nx, ny) in cardinal_moves_indicies(len(data[0]), len(data), x, y):
        if data[ny][nx] != "#":
            positions.append((nx, ny))


# path_length = sum(line.count(".") for line in data) + 1
differences = defaultdict(int)

# for (x, y) in moves:
#     two_away = cardinal_moves_indicies(
#         len(data[0]), len(data), x, y, include_all=True, factor=2)
#     one_away = cardinal_moves_indicies(
#         len(data[0]), len(data), x, y, include_all=True)

#     for (x1, y1), (x2, y2) in zip(one_away, two_away):
#         if not (x2 in range(len(data[0])) and y2 in range(len(data))):
#             continue
#         if data[y1][x1] != "#" or data[y2][x2] == "#" or ((x1, y1), (x2, y2)) in cheats_seen:
#             continue

#         cheats_seen.add(((x1, y1), (x2, y2)))

#         i, i2 = move_indices[(x, y)], move_indices[(x2, y2)]

#         if i < i2:
#             differences[i2 - i - 2] += 1

for (x1, y1) in moves:
    cheats_seen = set()
    cheat_positions = deque([(x1, y1, 0)])
    while cheat_positions:
        x, y, num_moves = cheat_positions.popleft()

        if num_moves > 20 or (x, y) in cheats_seen:
            continue
        cheats_seen.add((x, y))
        if data[y][x] != "#":
            # Out of wall, valid cheat
            di = move_indices[(x, y)] - move_indices[(x1, y1)]
            if di - num_moves >= 100:
                differences[di - num_moves] += 1

        for (nx, ny) in cardinal_moves_indicies(len(data[0]), len(data), x, y):
            cheat_positions.append((nx, ny, num_moves + 1))


count = 0

for d, c in differences.items():
    count += c

# for d in sorted(differences.keys()):
#     print(f"There are {differences[d]} cheats that save {d} picoseconds")

# print(differences)
print(count)
