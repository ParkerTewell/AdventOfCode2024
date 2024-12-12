from collections import deque, Counter
with open('Input/Dec11.txt') as f:
    rocks = list(map(int, f.readline().split()))


def solve(rounds, rocks):
    rocks = Counter(rocks)

    for _ in range(rounds):
        new_rocks = Counter()
        for r in rocks.keys():
            if r == 0:
                new_rocks[r+1] += rocks[r]
            elif len(str(r)) % 2 == 0:
                s = str(r)
                r1, r2 = int(s[len(s)//2:]), int(s[:(len(s)//2)])
                new_rocks[r1] += rocks[r]
                new_rocks[r2] += rocks[r]
            else:
                new_rocks[r*2024] += rocks[r]
        rocks = new_rocks

    return rocks.values()


print(sum(solve(75, rocks)))
