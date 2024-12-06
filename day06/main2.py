import numpy as np
with open("./input.txt") as f:
    data = list(map(lambda l: list(l.strip()), f.readlines()))


def get_dir(dx, dy):
    return [[0, -1], [1, 0], [0, 1], [-1, 0]].index([dx, dy])


def get_range(p, l):
    l = list(l)
    print(l, "#" in l[p+1:])
    if "#" in l[:p]:
        l_idx = p - (l[:p][::-1].index("#"))
    else:
        l_idx = 0
    if "#" in l[p+1:]:
        r_idx = p + l[p+1:].index("#") + 1
    else:
        r_idx = len(l)

    return range(l_idx, r_idx)


y = [i for i in range(len(data)) if "^" in data[i]][0]
x = data[y].index("^")
dx, dy = 0, -1

cols = np.transpose(data)

# List of dictionaries for each direction (URDL)
# Keys are col/row indices
# Vals are lists of ranges
lines = [
    {x: [get_range(y, cols[x])]},
    {},
    {},
    {},


]
mat = [[False for i in range(len(data[0]))] for j in range(len(data))]
mat[y][x] = True

count1 = 1
count2 = 0

while x + dx in range(len(data[0])) and y + dy in range(len(data)):
    # Guard has not wandered off
    if data[y+dy][x+dx] == "#":
        # Hit a wall, turn
        if dx == 0:
            dx = -dy
            dy = 0
        else:
            dy = dx
            dx = 0

        # New line, add it to records
        dir = get_dir(dx, dy)
        if dir % 2 == 0:
            # Up & down column motion
            if x in lines[dir]:
                lines[dir][x].append(get_range(y, cols[x]))
            else:
                lines[dir][x] = [get_range(y, cols[x])]
        else:
            # Left & right row motion
            if y in lines[dir]:
                lines[dir][y].append(get_range(x, data[y]))
            else:
                lines[dir][y] = [get_range(x, data[y])]
    else:
        # Advance
        x += dx
        y += dy

    if not mat[y][x]:
        count1 += 1

    mat[y][x] = True

    # Check the lines in the direction they can turn in the current row/col
    dir = get_dir(dx, dy)
    if dir % 2 == 1:
        # Currently left and right moving, search for up & down column motion
        if x in lines[(dir + 1) % 4]:
            possible_lines = lines[(dir + 1) % 4][x]

            for pl in possible_lines:
                if y in pl:
                    count2 += 1
                    break
    else:
        # Currently up and down moving, search for left & right row motion
        if y in lines[(dir + 1) % 4]:
            possible_lines = lines[(dir + 1) % 4][y]

            for pl in possible_lines:
                if x in pl:
                    count2 += 1
                    break

    print(x, y)
    for i, d in enumerate(lines):
        print(["Up", "Right", "Down", "Left"][i])
        for k, v in d.items():
            print(k, v)
        print()

    print("----")

print(count1, count2)
