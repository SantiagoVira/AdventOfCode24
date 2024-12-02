with open("./input.txt") as f:
    data = f.readlines()

count = 0


def is_safe(nums):
    mult = 1 if nums[1] > nums[0] else -1
    for i in range(1, len(nums)):
        diff = mult * (nums[i] - nums[i-1])
        if not (1 <= diff <= 3):
            return False

    return True


for line in data:
    nums = list(map(int, line.split(" ")))

    if is_safe(nums):
        count += 1
    else:
        for i in range(len(nums)):
            new_nums = nums.copy()
            new_nums.pop(i)
            if is_safe(new_nums):
                count += 1
                break


print(count)
