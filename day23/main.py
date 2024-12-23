import sys
sys.path.append("..")
from helpers import *  # noqa

# Parse input
data = parse_input("./input.txt", Parse.lines)

connections = defaultdict(set)
for line in data:
    source, target = line.split("-")
    connections[source].add(target)
    connections[target].add(source)

for i in range(3, 14):
    party = set()

    for k, v in connections.items():
        for combo in itertools.combinations(v, i):
            works = True
            for c1 in range(len(combo)):
                for c2 in range(c1+1, len(combo)):
                    if combo[c1] not in connections[combo[c2]]:
                        works = False
                        break

                if not works:
                    break

            if works:
                party.add(tuple(sorted((k, *combo))))

    if len(party) == 1:
        print(",".join(party.pop()))
        break

    print(i, len(party))
