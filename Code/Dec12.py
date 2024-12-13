from collections import deque
with open('Input/Dec12.txt') as f:
    grid = [list(line.strip()) for line in f.readlines()]
n, m = len(grid), len(grid[0])

# for r in grid:
#     print(r)


def bfs(r, c):
    global n, m, grid
    queue, seen = deque([(r, c)]), set([(r, c)])
    area, perimeter = 0, 0

    while queue:
        for _ in range(len(queue)):
            r, c = queue.pop()
            perimeter += 4
            area += 1
            for rd, cd in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= r+rd < n and 0 <= c+cd < m and grid[r+rd][c+cd] == grid[r][c]:
                    perimeter -= 1
                    if (r+rd, c+cd) not in seen:
                        queue.appendleft((r+rd, c+cd))
                        seen.add((r+rd, c+cd))
    return area, perimeter, seen


def pt1():
    seen, soln = set(), 0
    for r in range(n):
        for c in range(m):
            if (r, c) not in seen:
                seen.add((r, c))
                a, p, s = bfs(r, c)
                seen |= s
                soln += a*p
    return soln


print(pt1())
