import sys
sys.path.append("..")
from helpers import *  # noqa

avail, desired = parse_input("./input.txt", Parse.two_lines)
avail = avail.split(", ")
desired = Parse.lines(desired)

count = 0
count2 = 0

for d in desired:
    paths = [""]
    seen = set()

    counts = defaultdict(int)
    counts[""] = 1
    winners = set()

    while paths:
        paths.sort(key=len)
        p = paths.pop(0)

        if p not in seen and len(p) <= len(d):
            goal = d[len(p):]

            for a in avail:
                if goal.startswith(a):
                    if p + a == d:
                        winners.add(p)
                    paths.append(p + a)
                    counts[p+a] += counts[p]
                    seen.add(p)

    for w in winners:
        count2 += counts[w]
    if winners:
        count += 1


print(count, count2)
