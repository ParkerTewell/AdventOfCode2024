from operator import add, mul
with open('AdventOfCode2024/Input/Dec7.txt') as f:
    lines = f.readlines()

targets, numbers = [], []
for line in lines:
    line = line.strip().split(":")
    targets.append(int(line[0]))
    numbers.append(list(map(int, line[1].split())))


def cat(x, y):
    return int(str(x)+str(y))


def pt1(target, curr, nums, ops):
    if target == curr and len(nums) == 0:
        return target
    elif target < curr or len(nums) == 0:
        return 0
    else:
        x = nums[0]
        for op in ops:
            if pt1(target, op(curr, x), nums[1:], ops):
                return target
    return 0


print(sum(pt1(t, 0, nums, [add, mul])
      for t, nums in zip(targets, numbers)))
print(sum(pt1(t, 0, nums, [add, mul, cat])
      for t, nums in zip(targets, numbers)))
