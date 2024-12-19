import sys
sys.path.append("..")
from helpers import *  # noqa

avail, desired = parse_input("./input.txt", Parse.two_lines)
avail = avail.split(", ")
desired = Parse.lines(desired)

count = 0
count2 = 0

for d in desired:
    paths = [0]
    seen = set()

    counts = defaultdict(int)
    counts[0] = 1
    winners = set()

    while paths:
        paths.sort()
        p = paths.pop(0)

        if p not in seen and p <= len(d):
            goal = d[p:]

            for a in avail:
                if goal.startswith(a):
                    if goal == a:
                        winners.add(p)
                    paths.append(p + len(a))
                    counts[p+len(a)] += counts[p]
                    seen.add(p)

    for w in winners:
        count2 += counts[w]
    if winners:
        count += 1


print(count, count2)
