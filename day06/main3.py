with open("./input.txt") as f:
    data = list(map(lambda l: list(l.strip()), f.readlines()))

y0 = [i for i in range(len(data)) if "^" in data[i]][0]
x0 = data[y0].index("^")

count2 = 0

print(x0, y0)

for y_lvl in range(len(data)):
    for x_lvl in range(len(data[0])):
        # print(y_lvl, x_lvl)
        if data[y_lvl][x_lvl] != ".":
            continue

        data[y_lvl][x_lvl] = "#"
        x, y = x0, y0
        dx, dy = 0, -1

        visited = set()
        visited.add((x, y, dx, dy))

        while x+dx in range(len(data[0])) and y+dy in range(len(data)):
            if data[y+dy][x+dx] == "#":
                # Hit a wall, turn
                if dx == 0:
                    dx = -dy
                    dy = 0
                else:
                    dy = dx
                    dx = 0
            else:
                # Advance
                x += dx
                y += dy

            if (x, y, dx, dy) in visited:
                count2 += 1
                break

            visited.add((x, y, dx, dy))

        data[y_lvl][x_lvl] = "."


print(count2)
