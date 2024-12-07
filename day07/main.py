import math

with open("./input.txt") as f:
    data = [[int(line.split(": ")[0]), list(map(int, line.split(
        ": ")[1].strip().split(" ")))] for line in f.readlines()]

total = 0


def ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))


for test, nums in data:
    done = False
    for i in range(3**(len(nums) - 1)):

        ops = ternary(i).zfill(len(nums)-1)
        value = nums[0]

        for j in range(1, len(nums)):
            if value > test:
                break

            if ops[j-1] == "0":
                value += nums[j]
            elif ops[j-1] == "1":
                value *= nums[j]
            else:
                value *= (10 ** (math.floor(math.log10(nums[j])) + 1))
                value += nums[j]

        if value == test:
            done = True
            break

        if done:
            break

    if done:
        total += test

print(total)
