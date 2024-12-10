with open("./input.txt") as f:
    data = list(map(lambda x: [int(c)
                for c in list(x.strip())], f.readlines()))

paths = []

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == 0:
            paths.append((x, y, x, y))


def check(data, x, y, target):
    return y in range(len(data)) and x in range(len(data[0])) and data[y][x] == target


peaks = {}
peaks2 = {}

while paths:
    (x, y, x0, y0) = paths.pop(0)
    value = data[y][x]
    if value == 9:
        if (x0, y0) not in peaks:
            peaks[(x0, y0)] = set()

        peaks[(x0, y0)].add((x, y))

        if (x, y, x0, y0) in peaks2:
            peaks2[(x, y, x0, y0)] += 1
        else:
            peaks2[(x, y, x0, y0)] = 1
        continue
    if check(data, x, y-1, value + 1):
        paths.append((x, y-1, x0, y0))
    if check(data, x, y+1, value + 1):
        paths.append((x, y+1, x0, y0))
    if check(data, x-1, y, value + 1):
        paths.append((x-1, y, x0, y0))
    if check(data, x+1, y, value + 1):
        paths.append((x+1, y, x0, y0))


total = 0
for start, ends in peaks.items():
    total += len(ends)

print(total)

total2 = 0
for displacement, count in peaks2.items():
    total2 += count

print(total2)
