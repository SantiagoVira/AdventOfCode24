with open("./input.txt") as f:
    data = list(map(list, f.readlines()))

y = [i for i in range(len(data)) if "^" in data[i]][0]
x = data[y].index("^")
dx, dy = 0, -1

mat = [[False for i in range(len(data[0]))] for j in range(len(data))]
mat[y][x] = True
count = 1


while y + dy in range(len(data)) and x + dx in range(len(data[0])):
    if data[y + dy][x + dx] == "#":
        if not dx:
            dx = -dy
            dy = 0
        else:
            dy = dx
            dx = 0

    x += dx
    y += dy

    if not mat[y][x]:
        count += 1
        mat[y][x] = True

print(count)
