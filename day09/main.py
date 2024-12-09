with open("./input.txt") as f:
    data = f.read().strip()

files = []
id = 0

for i in range(len(data)):
    n = int(data[i])
    if i % 2 == 0:
        files.append((id, n))
        id += 1
    else:
        files.append((None, n))

i = len(files) - 1
while i > 0:
    if files[i][0] != None:
        idx = -1
        for j, f in enumerate(files):
            if f[0] == None and f[1] >= files[i][1] and j < i:
                idx = j
                break

        if idx != -1:
            files.insert(idx, files[i])
            files.insert(i+1, (None, files[i+1][1]))
            files.pop(i+2)
            files[idx + 1] = (None, files[idx + 1][1] - files[idx][1])

    i -= 1


total = 0
k = 0
for i in range(len(files)):
    if files[i][0] == None:
        k += files[i][1]
        continue
    for _ in range(files[i][1]):
        total += k * files[i][0]
        k += 1

print(total)
