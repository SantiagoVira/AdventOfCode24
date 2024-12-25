import sys
sys.path.append("..")
from helpers import *  # noqa

# Parse input
data = parse_input("./input.txt", Parse.two_lines)
locks, keys = [], []

for item in data:
    if item[0] == "#":
        # Lock
        lock = [0, 0, 0, 0, 0]
        lines = item.splitlines()[1:]
        for line in lines:
            for x in range(len(line)):
                if line[x] == "#":
                    lock[x] += 1
        locks.append(tuple(lock))
    else:
        # Key
        key = [0, 0, 0, 0, 0]
        lines = item.splitlines()[:-1]
        for line in lines:
            for x in range(len(line)):
                if line[x] == "#":
                    key[x] += 1
        keys.append(tuple(key))

combos = 0

for key in keys:
    for lock in locks:
        if max([a + b for (a, b) in zip(key, lock)]) <= 5:
            combos += 1

print(combos)
