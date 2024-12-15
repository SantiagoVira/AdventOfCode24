import sys
sys.path.append("..")
from helpers import *  # noqa

layout, moves = parse_input("./input.txt", Parse.two_lines)

grid = [list(line) for line in layout.split("\n")]
moves = moves.replace("\n", "")

grid2 = []
for y, line in enumerate(grid):
    grid2.append([])
    for c in line:
        match c:
            case "#":
                grid2[-1] += ["#", "#"]
            case "O":
                grid2[-1] += ["[", "]"]
            case ".":
                grid2[-1] += [".", "."]
            case "@":
                grid2[-1] += ["@", "."]

y = [i for i in range(len(grid2)) if "@" in grid2[i]][0]
x = grid2[y].index("@")

for m in moves:
    dx, dy = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}[m]
    newx, newy = x + dx, y + dy
    if grid2[newy][newx] == ".":
        # No boxes
        grid2[newy][newx] = "@"
        grid2[y][x] = "."
        x, y = newx, newy
    elif grid2[newy][newx] == "#":
        # Moving into a wall
        continue
    elif dy == 0:
        # Moving boxes horizontally
        while grid2[newy][newx] != "." and grid2[newy][newx] != "#":
            newx, newy = newx + dx, newy + dy

        if grid2[newy][newx] != "#":
            grid2[y].pop(newx)
            grid2[y].insert(x, ".")
            x, y = x+dx, y+dy
    else:
        # Moving boxes vertically

        # Check if boxes can move
        boxes = []
        can_move = True
        if grid2[newy][newx] == "[":
            boxes.append((newx, newy))
        else:
            boxes.append((newx - 1, newy))
        while boxes:
            b = boxes.pop(0)
            if "#" in grid2[b[1] + dy][b[0]:b[0]+2]:
                can_move = False
                break
            if grid2[b[1]+dy][b[0]-1] == "[":
                boxes.append((b[0]-1, b[1]+dy))
            if grid2[b[1]+dy][b[0]] == "[":
                boxes.append((b[0], b[1]+dy))
            if grid2[b[1]+dy][b[0]+1] == "[":
                boxes.append((b[0]+1, b[1]+dy))
        if not can_move:
            continue

        # Move boxes
        boxes = []
        if grid2[newy][newx] == "[":
            boxes.append((newx, newy))
            grid2[newy][newx] = "@"
            grid2[newy][newx + 1] = "."
            grid2[y][x] = "."
        else:
            boxes.append((newx - 1, newy))
            grid2[newy][newx] = "@"
            grid2[newy][newx - 1] = "."
            grid2[y][x] = "."

        x, y = x + dx, y + dy

        while boxes:
            b = boxes.pop(0)

            if grid2[b[1]+dy][b[0]-1] == "[":
                boxes.append((b[0]-1, b[1]+dy))
                grid2[b[1] + dy][b[0]-1] = "."
            if grid2[b[1]+dy][b[0]] == "[":
                boxes.append((b[0], b[1]+dy))
            if grid2[b[1]+dy][b[0]+1] == "[":
                boxes.append((b[0]+1, b[1]+dy))
                grid2[b[1] + dy][b[0]+2] = "."

            grid2[b[1] + dy][b[0]] = "["
            grid2[b[1] + dy][b[0]+1] = "]"
    # print(m)
    # print(newx, newy)
    # print("\n".join("".join(line) for line in grid2))
    # print("\n-----\n")


total2 = 0
for y in range(1, len(grid2)):
    for x in range(1, len(grid2[0])):
        if grid2[y][x] == "[":
            total2 += 100 * y + x

print(total2)

# y = [i for i in range(len(grid)) if "@" in grid[i]][0]
# x = grid[y].index("@")

# for m in moves:
#     dx, dy = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}[m]
#     newx, newy = x + dx, y + dy
#     while newx in range(len(grid[0])) and newy in range(len(grid)) and grid[newy][newx] != "." and grid[newy][newx] != "#":
#         newx, newy = newx + dx, newy + dy

#     if newx in range(len(grid[0])) and newy in range(len(grid)) and grid[newy][newx] != "#":
#         grid[y][x] = "."
#         x, y = x + dx, y + dy
#         grid[y][x] = "@"
#         if newy != y or newx != x:
#             grid[newy][newx] = "O"
#     # print(m)
#     # print(newx, newy)
#     # print("\n".join("".join(line) for line in grid))
#     # print("\n-----\n")

# total1 = 0
# for y in range(1, len(grid)):
#     for x in range(1, len(grid[0])):
#         if grid[y][x] == "O":
#             total1 += 100 * y + x

# print(total1)
