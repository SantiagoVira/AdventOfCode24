with open("./input.txt") as f:
    data = f.readlines()

freqs = [i for line in data for i in line if i !=
         "\n" and i != "."]
locs1, locs2 = set(), set()

SIZE = len(data)


def get_anti1(x1, y1, x2, y2):
    dy = y2 - y1
    dx = x2 - x1

    nodes = []
    if x1-dx in range(SIZE) and y1-dy in range(SIZE):
        nodes.append((x1 - dx, y1 - dy))
    if x2+dx in range(SIZE) and y2+dy in range(SIZE):
        nodes.append((x2 + dx, y2 + dy))

    return nodes


def get_anti2(x1, y1, x2, y2):
    dy = y2 - y1
    dx = x2 - x1

    nodes = []
    p = [x1, y1]
    while p[0] >= 0 and p[1] >= 0 and p[0] < SIZE and p[1] < SIZE:
        nodes.append((p[0], p[1]))
        p[0] -= dx
        p[1] -= dy
    p = [x2, y2]
    while p[0] >= 0 and p[1] >= 0 and p[0] < SIZE and p[1] < SIZE:
        nodes.append((p[0], p[1]))
        p[0] += dx
        p[1] += dy

    return nodes


for f in freqs:
    positions = []
    for row in range(SIZE):
        for col in range(SIZE):
            if data[row][col] == f:
                positions.append((col, row))

    for a1 in range(len(positions)):
        for a2 in range(a1 + 1, len(positions)):
            locs1.update(get_anti1(*positions[a1], *positions[a2]))
            locs2.update(get_anti2(*positions[a1], *positions[a2]))


print(len(locs1), len(locs2))
