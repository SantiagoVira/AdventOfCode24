import sys
sys.path.append("..")
from helpers import *  # noqa

data = parse_input("./input.txt", Parse.chars2d)
visited = set()


def traverse(x, y, area=0, perimeter=0, sides=0):
    if y not in range(len(data)) or x not in range(len(data[0])) or (x, y) in visited:
        return area, perimeter, sides

    visited.add((x, y))
    area += 1

    adjacents = cardinal_moves_indicies(len(data[0]), len(data), x, y, True)
    diagonals = diagonal_moves_indices(len(data[0]), len(data), x, y, True)

    for i in range(4):
        # Convex corners
        if not check_list2d(data, *adjacents[i], data[y][x]) and not check_list2d(data, *adjacents[(i+1) % 4], data[y][x]):
            sides += 1
        # Concave corners
        if check_list2d(data, *adjacents[i], data[y][x]) and check_list2d(data, *adjacents[(i+1) % 4], data[y][x]) and not check_list2d(data, *diagonals[i], data[y][x]):
            sides += 1

    # Explore the rest of the region
    for c in adjacents:
        if check_list2d(data, c[0], c[1], data[y][x]):
            area, perimeter, sides = traverse(*c, area, perimeter, sides)
        else:
            perimeter += 1

    return area, perimeter, sides


total1, total2 = 0, 0

for y in range(len(data)):
    for x in range(len(data[0])):
        if (x, y) not in visited:
            a, p, s = traverse(x, y)
            total1 += a * p
            total2 += a * s


print(total1, total2)
