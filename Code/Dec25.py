locks, keys = [], []
for grid in open('Input/Dec25.txt').read().split("\n\n"):
    pins = [p.count('#')-1 for p in zip(*grid.split('\n'))]
    if '#' in grid[0]:
        locks.append(pins)
    else:
        keys.append(pins)


def solve():
    total = 0

    for lock in locks:
        for key in keys:
            if all(l + k <= 5 for l, k in zip(lock, key)):
                total += 1
    return total


print(solve())
