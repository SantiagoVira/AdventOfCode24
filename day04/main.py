with open("./input.txt") as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

l = len(data[0])
cols = ["".join([r[i] for r in data]) for i in range(l)]

total = sum(line.count("XMAS") + line.count("SAMX") for line in data) + \
    sum(line.count("XMAS") + line.count("SAMX") for line in cols)
total2 = 0

h = 0
v = 0

for y, line in enumerate(data):
    ti = total
    for x, c in enumerate(line):
        if c == "X":
            if y > 2 and x > 2 and data[y-1][x-1]+data[y-2][x-2]+data[y-3][x-3] == "MAS":
                total += 1
            if y > 2 and x < l-3 and data[y-1][x+1]+data[y-2][x+2]+data[y-3][x+3] == "MAS":
                total += 1
            if y < len(data)-3 and x > 2 and data[y+1][x-1]+data[y+2][x-2]+data[y+3][x-3] == "MAS":
                total += 1
            if y < len(data)-3 and x < l-3 and data[y+1][x+1]+data[y+2][x+2]+data[y+3][x+3] == "MAS":
                total += 1

        if c == "M" and x < l-2 and y < len(data)-2 and line[x+2] == "S" and data[y+1][x+1] == "A" and data[y+2][x] == "M" and data[y+2][x+2] == "S":
            total2 += 1
        elif c == "M" and x < l-2 and y < len(data)-2 and line[x+2] == "M" and data[y+1][x+1] == "A" and data[y+2][x] == "S" and data[y+2][x+2] == "S":
            total2 += 1
        elif c == "S" and x < l-2 and y < len(data)-2 and line[x+2] == "S" and data[y+1][x+1] == "A" and data[y+2][x] == "M" and data[y+2][x+2] == "M":
            total2 += 1
        elif c == "S" and x < l-2 and y < len(data)-2 and line[x+2] == "M" and data[y+1][x+1] == "A" and data[y+2][x] == "S" and data[y+2][x+2] == "M":
            total2 += 1


print(total)
