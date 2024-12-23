import heapq
with open('Input/Dec16.txt') as f:
    grid = [list(line.strip()) for line in f.readlines()]
n, m = len(grid), len(grid[0])
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def find_start_end():
    global grid, m, n
    start, end = None, None
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 'S':
                start = (r, c)
            if grid[r][c] == 'E':
                end = (r, c)
    return start, end


def dijkstra(start, end):
    global directions
    pq = [(0, start[0], start[1], 0)]  # score, r, c, d
    seen, min_score = set(), float('inf')

    while pq:
        score, r, c, d = heapq.heappop(pq)

        if (r, c) == end:
            min_score = min(min_score, score)
        elif (r, c, d) not in seen:
            seen.add((r, c, d))
            nr, nc = r+directions[d][0], c+directions[d][1]
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != '#':
                heapq.heappush(pq, (score+1, nr, nc, d))

            # rotate clockwise
            new_d = (d+1) % 4
            heapq.heappush(pq, (score + 1000, r, c, new_d))

            # rotate counterclockwise
            new_d = (d-1) % 4
            heapq.heappush(pq, (score + 1000, r, c, new_d))

    return min_score


start, end = find_start_end()
print(dijkstra(start, end))
