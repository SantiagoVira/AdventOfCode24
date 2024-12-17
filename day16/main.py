import time
import sys
sys.path.append("..")
from helpers import *  # noqa


start = time.time()

# PARSE DATA
data = parse_input("./input.txt", Parse.chars2d)
y0 = [i for i in range(len(data)) if "S" in data[i]][0]
x0 = data[y0].index("S")

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# PART 1
positions = deque([(x0, y0, 1, 0, 0)])
min_score = float("inf")
all_positions = {}

# PART 2
paths = defaultdict(list)
winning_paths = deque()
path_to_parent = {}
next_path_id = 1

while positions:
    x, y, d, score, path_id = positions.popleft()

    if data[y][x] == "E":
        if score < min_score:
            min_score, winning_paths = score, deque([path_id])
        elif score == min_score:
            winning_paths.append(path_id)

        paths[path_id].append((x, y))
        continue

    all_positions[(x, y, d)] = score
    paths[path_id].append((x, y))

    for dir_num in [(d+3) % 4, d, (d+1) % 4]:
        new_x, new_y = x + dirs[dir_num][0], y + dirs[dir_num][1]
        new_score = score + (1 if dir_num == d else 1001)
        if ((new_x, new_y, dir_num) not in all_positions or all_positions[(new_x, new_y, dir_num)] >= new_score) and data[new_y][new_x] != "#" and new_score <= min_score:
            path_to_parent[next_path_id] = path_id
            positions.append((new_x, new_y, dir_num, new_score, next_path_id))
            next_path_id += 1

print(min_score)

good_seats = set()

while winning_paths:
    wp = winning_paths.popleft()
    good_seats.update(paths[wp])
    if wp in path_to_parent:
        winning_paths.append(path_to_parent[wp])

print(len(good_seats))

print(time.time()-start)
