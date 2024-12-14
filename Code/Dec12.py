from collections import deque
with open('Input/Dec12.txt') as f:
    grid = [list(line.strip()) for line in f.readlines()]
n, m = len(grid), len(grid[0])

# for r in grid:
#     rint(r)


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


def solve():
    seen, soln1, soln2 = set(), 0, 0
    for r in range(n):
        for c in range(m):
            if (r, c) not in seen:
                seen.add((r, c))
                a, p, s = bfs(r, c)
                soln1 += a * p
                soln2 += a * countSides(s)
                seen |= s
    return soln1, soln2

# first check that a plot is on the perimeter of the region
# once we find an unmarked plot, mark it and all its neighbors in the
# to mark these neighbors, multiply the delta by a positive or negative scalar to go in both directions


def countSides(region):
    sides = 0
    for rd, cd in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        seen = set()
        for plot in region:
            r, c = plot
            # only want exterior plots that haven't been seen
            if (r, c) not in seen and (r + rd, c + cd) not in region:
                sides += 1
                # mark this side as seen
                for scalar in [-1, 1]:
                    r, c = plot
                    while (r, c) in region and (r + rd, c + cd) not in region:
                        seen.add((r, c))
                        r += cd * scalar
                        c += rd * scalar

    return sides


print(solve())
