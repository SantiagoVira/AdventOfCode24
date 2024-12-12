with open("./input.txt") as f:
    data = list(map(lambda x: list(x.strip()), f.readlines()))

visited = set()


def is_border(x, y, target):
    return y not in range(len(data)) or x not in range(len(data[0])) or data[y][x] != target


def is_region(x, y, target):
    return y in range(len(data)) and x in range(len(data[0])) and data[y][x] == target


def traverse(x, y, area=0, perimeter=0, sides=0):
    if y not in range(len(data)) or x not in range(len(data[0])) or (x, y) in visited:
        return area, perimeter, sides

    visited.add((x, y))
    area += 1
    borders = [is_border(x, y-1, data[y][x]), is_border(x+1, y, data[y][x]),
               is_border(x, y+1, data[y][x]), is_border(x-1, y, data[y][x])]
    regions = [is_region(x, y-1, data[y][x]), is_region(x+1, y, data[y][x]),
               is_region(x, y+1, data[y][x]), is_region(x-1, y, data[y][x])]
    perimeter += borders.count(True)

    # Convex corners
    if borders[0] and borders[1]:
        sides += 1
    if borders[1] and borders[2]:
        sides += 1
    if borders[2] and borders[3]:
        sides += 1
    if borders[3] and borders[0]:
        sides += 1

    # Concave corners
    if regions[0] and regions[1] and not is_region(x+1, y-1, data[y][x]):
        sides += 1
    if regions[1] and regions[2] and not is_region(x+1, y+1, data[y][x]):
        sides += 1
    if regions[2] and regions[3] and not is_region(x-1, y+1, data[y][x]):
        sides += 1
    if regions[3] and regions[0] and not is_region(x-1, y-1, data[y][x]):
        sides += 1

    # Explore the rest of the region
    if regions[0]:
        area, perimeter, sides = traverse(x, y-1, area, perimeter, sides)
    if regions[1]:
        area, perimeter, sides = traverse(x+1, y, area, perimeter, sides)
    if regions[2]:
        area, perimeter, sides = traverse(x, y+1, area, perimeter, sides)
    if regions[3]:
        area, perimeter, sides = traverse(x-1, y, area, perimeter, sides)

    return area, perimeter, sides


total1, total2 = 0, 0

for y in range(len(data)):
    for x in range(len(data[0])):
        if (x, y) not in visited:
            a, p, s = traverse(x, y)
            total1 += a * p
            total2 += a * s


print(total1, total2)
