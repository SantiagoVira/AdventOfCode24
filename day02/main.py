with open("./input.txt") as f:
    data = f.readlines()

count = 0


def is_safe(nums, skip=-1):
    if skip < 2:
        mult = 1 if nums[2] > nums[not skip] else -1
    else:
        mult = 1 if nums[1] > nums[0] else -1

    for i in range(1, len(nums)):
        if i != skip and (skip != 0 or i != 1):
            prev = nums[i-2] if i == skip + 1 else nums[i-1]
            diff = mult * (nums[i] - prev)

            if not (1 <= diff <= 3):
                return False

    return True


for line in data:
    nums = list(map(int, line.split(" ")))

    if is_safe(nums):
        count += 1
    else:
        for i in range(len(nums)):
            if is_safe(nums, skip=i):
                count += 1
                break


print(count)
