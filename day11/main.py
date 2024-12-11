from typing import Optional
import math

with open("./input.txt") as f:
    stones = {k: 1 for k in map(int, f.read().strip().split())}


def blink(stone) -> tuple[int, Optional[int]]:
    if stone == 0:
        return (1, None)
    digits = math.floor(math.log10(stone)+1)
    if digits % 2 == 0:
        sep = 10 ** (digits / 2)
        return (stone // sep, stone % sep)
    return (stone * 2024, None)


for i in range(75):
    new_stones = {}
    for num in stones:
        (a, b) = blink(num)
        if a in new_stones:
            new_stones[a] += stones[num]
        else:
            new_stones[a] = stones[num]
        if b != None:
            if b in new_stones:
                new_stones[b] += stones[num]
            else:
                new_stones[b] = stones[num]

    stones = new_stones
    print(sorted(stones.values(), reverse=True)[:5])

print(sum(stones.values()))
