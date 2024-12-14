import sys
sys.path.append("..")
from helpers import *  # noqa

data = []
W, H = 101, 103
for line in parse_input("./input.txt", Parse.lines):
    p, v = line.split()
    p_nums = [int(n) for n in p[2:].split(",")]
    v_nums = [int(n) for n in v[2:].split(",")]
    data.append([p_nums, v_nums])

data2 = deepcopy(data)

for i in range(100):
    for j in range(len(data)):
        data[j][0][0] = (data[j][0][0] + data[j][1][0] + W) % W
        data[j][0][1] = (data[j][0][1] + data[j][1][1] + H) % H


grid = [[0 for _i in range(W)] for _j in range(H)]
for p, v in data:
    grid[p[1]][p[0]] += 1

prod = 1
prod *= sum(sum(line[:W//2]) for line in grid[:H//2])
prod *= sum(sum(line[W//2 + 1:]) for line in grid[:H//2])
prod *= sum(sum(line[:W//2]) for line in grid[H//2 + 1:])
prod *= sum(sum(line[W//2 + 1:]) for line in grid[H//2 + 1:])

print(prod)

for i in range(999999):
    for j in range(len(data2)):
        data2[j][0][0] = (data2[j][0][0] + data2[j][1][0] + W) % W
        data2[j][0][1] = (data2[j][0][1] + data2[j][1][1] + H) % H

    grid = [[0 for _i in range(W)] for _j in range(H)]
    for p, v in data2:
        grid[p[1]][p[0]] += 1

    for line in grid:
        if "1111111111" in "".join(str(n) for n in line):
            break
    else:
        continue

    print(i + 1)
    for i in range(len(grid)):
        print("".join(str(n) if n > 0 else "." for n in grid[i]))
    break
