with open("./input.txt") as f:
    data = f.readlines()

lefts = []
rights = []

for line in data:
    l, r = [int(v) for v in line.split(' ') if v]

    lefts.append(l)
    rights.append(r)

lefts.sort()
rights.sort()

total = 0

for i in range(len(lefts)):
    total += abs(lefts[i] - rights[i])

print(total)
