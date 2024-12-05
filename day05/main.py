with open("./input.txt") as f:
    rules, updates = f.read().split("\n\n")

# Each key must occur before every number in the value array
befores = {}

for r in rules.split():
    b, a = map(lambda x: int(x.strip()), r.split("|"))
    if b not in befores:
        befores[b] = set()

    befores[b].add(a)

total1, total2 = 0, 0


def check_valid(nums):
    is_valid = True
    already = {}
    problem = (-1, -1)

    for i in range(len(nums)):
        n = nums[i]
        already[n] = i
        if n in befores:
            for a in already.keys():
                if a in befores[n]:
                    is_valid = False
                    problem = (already[a], i)
                    break
            if not is_valid:
                break

    return is_valid, problem


for u in updates.split():
    nums = list(map(lambda x: int(x.strip()), [
                n for n in u.split(",") if n.isnumeric()]))

    is_valid, problem = check_valid(nums)
    if is_valid:
        total1 += nums[len(nums)//2]
    else:
        while not is_valid:
            nums[problem[0]], nums[problem[1]
                                   ] = nums[problem[1]], nums[problem[0]]
            is_valid, problem = check_valid(nums)
        total2 += nums[len(nums)//2]

print(total1, total2)
