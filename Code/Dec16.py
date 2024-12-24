from heapq import heappop, heappush
with open('Input/Dec16.txt') as f:
    grid = [list(line.strip()) for line in f.readlines()]
n, m = len(grid), len(grid[0])
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def find_start_end():
    start, end = None, None
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 'S':
                start = (r, c)
            if grid[r][c] == 'E':
                end = (r, c)
    return start, end


def dijkstra(start, end):
    # score, r, c, d
    pq = [(0, start[0], start[1], 0, {(start[0], start[1], 0)})]
    seen, min_score, min_path = set(), float('inf'), None

    while pq:
        score, r, c, d, path = heappop(pq)

        if (r, c) == end:
            min_score = min(min_score, score)
            min_path = path
        elif (r, c, d) not in seen:
            seen.add((r, c, d))
            nr, nc = r+directions[d][0], c+directions[d][1]
            if grid[nr][nc] != '#':
                heappush(pq, (score+1, nr, nc, d, path | {(nr, nc, score+1)}))

            # rotate clockwise
            new_d = (d+1) % 4
            heappush(pq, (score + 1000, r, c, new_d,
                     path | {(nr, nc, score+1000)}))

            # rotate counterclockwise
            new_d = (d-1) % 4
            heappush(pq, (score + 1000, r, c, new_d,
                     path | {(nr, nc, score+1000)}))

    return min_score, min_path


def shortest_paths(start, end, shortest_path):
    # score, r, c, d, path
    pq = [(0, start[0], start[1], 0, {(start[0], start[1], 0)})]

    while pq:
        score, r, c, d, path = heappop(pq)
        if (r, c) == end:
            continue
        if (r, c, score) in shortest_path:
            shortest_path |= path
            continue

        for i, (dr, dc) in enumerate(directions):
            nr, nc = r+dr, c+dc
            if grid[nr][nc] != '#':
                new_score = score+1 if i == d else score+1000
                heappush(pq, (new_score, nr, nc, i,
                         path | {(nr, nc, new_score)}))
    return shortest_path


start, end = find_start_end()
min_score, min_path = dijkstra(start, end)
print(min_score, len(min_path))
print(len(shortest_paths(start, end, min_path)))
# print(len({node for path in shortest_paths(start, end) for node in path}))
