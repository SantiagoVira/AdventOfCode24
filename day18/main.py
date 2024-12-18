import sys
sys.path.append("..")
from helpers import *  # noqa

data = parse_input("./input.txt", Parse.lines)
bits = [tuple(map(int, line.strip().split(","))) for line in data]

SIZE = 71

for numbits in range(1024, 3451):
    grid = [[True for _x in range(SIZE)] for _y in range(SIZE)]

    for i in range(numbits):
        x, y = bits[i]
        grid[y][x] = False

    visited = set()
    spots = deque([(0, 0, 0)])

    while spots:
        x, y, moves = spots.popleft()
        if x == SIZE-1 and y == SIZE-1:
            break

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for nx, ny in cardinal_moves_indicies(SIZE, SIZE, x, y):
            if grid[ny][nx]:
                spots.append((nx, ny, moves + 1))
    else:
        print("Cant do it!")
        print(numbits)
        print
        break
