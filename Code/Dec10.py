with open('Input/Dec10.txt') as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]
n, m = len(grid), len(grid[0])
summits = set()


def dfs(r, c, elevation, pt1):
    global n, m, summits
    if 0 <= r < n and 0 <= c < m and grid[r][c] == elevation:
        if elevation == 9 and (r, c) not in summits:
            if pt1:
                summits.add((r, c))
            return 1
        return sum(dfs(r+rd, c+cd, elevation+1, pt1) for rd, cd in [(1, 0), (-1, 0), (0, 1), (0, -1)])
    return 0


def solve(pt1):
    global n, m, summits
    soln = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 0:
                summits = set()
                x = dfs(r, c, grid[r][c], pt1)
                soln += x
    return soln


print(solve(True))
print(solve(False))
