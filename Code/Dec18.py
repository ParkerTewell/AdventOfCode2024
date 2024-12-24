from collections import deque
n, m = 70, 1024
grid = [['.'] * (n+1) for _ in range(n+1)]

coords = [tuple(map(int,line.split(','))) for line in open('Code/Dec18.txt').readlines()]
for c, r in coords[:m]:
    grid[r][c] = '#'

def bfs():
    queue = deque([(0,0,0)]) # r, c, dist
    seen = set([(0,0)])
    while queue:
        r,c,d = queue.popleft()
        for rd, cd in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+rd, c+cd
            if (r,c) == (n,n):
                return d
            elif 0 <= nr <= n and 0 <= nc <= n and grid[nr][nc] != '#' and (nr, nc) not in seen:
                queue.append((nr,nc,d+1))
                seen.add((nr,nc))
    return -1


def simulate(s=0,e=m):
    for c, r in coords[s:e]:
        grid[r][c] = '#'
def find_unsolveable():
    for i in range(m, len(coords)-1):
        simulate(i, i+1)
        if bfs() == -1:
            return coords[i]
    return (-1,-1)
simulate()
print(bfs())
print(find_unsolveable())