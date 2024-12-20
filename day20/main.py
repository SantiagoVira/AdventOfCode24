import sys
sys.path.append("..")
from helpers import *  # noqa

# Parse input
data = parse_input("./input.txt", Parse.chars2d)
y0 = [i for i in range(len(data)) if "S" in data[i]][0]
x0 = data[y0].index("S")


positions = deque([(x0, y0)])
move_indices = {}
differences = defaultdict(int)
num_moves = 0
MAX_CHEAT_LENGTH = 2  # 20

while positions:
    x, y = positions.popleft()
    move_indices[(x, y)] = num_moves
    num_moves += 1

    if data[y][x] == "E":
        break

    for (nx, ny) in cardinal_moves_indicies(len(data[0]), len(data), x, y):
        if data[ny][nx] != "#" and (nx, ny) not in move_indices:
            positions.append((nx, ny))

for (x1, y1) in move_indices.keys():
    cheats_seen = set()
    cheat_positions = deque([(x1, y1, 0)])

    while cheat_positions:
        x, y, num_moves = cheat_positions.popleft()

        if num_moves > MAX_CHEAT_LENGTH or (x, y) in cheats_seen:
            continue
        cheats_seen.add((x, y))
        if data[y][x] != "#":
            # Out of wall, valid cheat
            di = move_indices[(x, y)] - move_indices[(x1, y1)]
            if di - num_moves >= 100:
                differences[di - num_moves] += 1

        for (nx, ny) in cardinal_moves_indicies(len(data[0]), len(data), x, y):
            cheat_positions.append((nx, ny, num_moves + 1))


count = sum(differences.values())
print(count)
