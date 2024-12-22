import sys
sys.path.append("..")
from helpers import *  # noqa

# Parse input
data = map(int, parse_input("./input.txt", Parse.lines))


def mix_and_prune(prev, new):
    return (new ^ prev) & ((1 << 24) - 1)


def calc_secret(prev):
    secret = mix_and_prune(prev, prev * (2**6))
    secret = mix_and_prune(secret, secret // 32)
    secret = mix_and_prune(secret, secret * (2**11))

    return secret


total = 0
seqs_to_bananas = defaultdict(int)
max_bananas = 0
for num in data:
    sec = num
    changes = deque()
    seqs_seen = set()
    for i in range(2000):
        if len(changes) == 4:
            changes.popleft()
        nsec = calc_secret(sec)
        changes.append(nsec % 10 - sec % 10)

        tup = tuple(changes)
        if len(changes) == 4 and tup not in seqs_seen:
            seqs_seen.add(tup)
            seqs_to_bananas[tup] += nsec % 10
            if seqs_to_bananas[tup] > max_bananas:
                max_bananas = seqs_to_bananas[tup]
        sec = nsec
    total += sec

print(total)
print(max_bananas)
