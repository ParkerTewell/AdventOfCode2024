grid = [list(line.strip()) for line in open('Input/Dec20.txt').readlines()]
n, m = len(grid), len(grid[0])
costs = [[-1] * n for _ in range(m)]


def find_start():
    start, end = None, None
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 'S':
                start = (r, c)
    return start


def dfs(r, c):
    costs[r][c] = 0
    while grid[r][c] != 'E':
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != '#' and costs[nr][nc] == -1:
                costs[nr][nc] = costs[r][c]+1
                r, c = nr, nc


def good_cheats(cheat_dist=20):
    count = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] != '#':
                for dist in range(2, cheat_dist+1):
                    for rd in range(dist+1):
                        cd = dist - rd
                        # have to use a set to ignore duplicate case when one coord is zero
                        for nr, nc in {(r+rd, c+cd), (r-rd, c+cd), (r+rd, c-cd), (r-rd, c-cd)}:
                            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != '#' and costs[r][c]-costs[nr][nc] >= 100+dist:
                                count += 1
    return count


r, c = find_start()
dfs(r, c)
print(good_cheats(2), good_cheats())
