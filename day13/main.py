with open("./input.txt") as f:
    machines = f.read().split("\n\n")
    data = []
    for m in machines:
        lines = m.split("\n")
        a = tuple(map(int, lines[0][12:].split(", Y+")))
        b = tuple(map(int, lines[1][12:].split(", Y+")))
        prize = tuple(map(lambda x: int(x) + 10000000000000,
                      lines[2][9:].split(", Y=")))
        data.append([a, b, prize])


def mostly_int(a):
    return abs(a - round(a)) < 0.001


total = 0
for a, b, p in data:
    x = (b[0] * p[1] - b[1] * p[0]) / (b[0] * a[1] - b[1] * a[0])
    y1 = (p[0] - a[0] * x) / b[0]
    y2 = (p[1] - a[1] * x) / b[1]
    if y1 == y2 and mostly_int(x) and mostly_int(y1):
        total += 3 * x + y1

print(total)
