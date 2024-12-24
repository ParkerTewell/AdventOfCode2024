import heapq
from collections import defaultdict, deque
with open('Code/Dec16.txt') as f:
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
    # prev needed for pt2, backtracking to find multiple optimal paths
    pq = [(0, start[0], start[1], 0, None, None, None)]  # score, r, c, d, prev_r, prev_c, prev_d
    lowest_cost, min_score = defaultdict(lambda: float('inf')), float('inf')
    backtrack = defaultdict(set)
    end_state = None # needed to trace back optimal paths
    while pq:
        score, r, c, d, pr, pc, pd = heapq.heappop(pq)
        if score > lowest_cost[(r, c, d)]:
            continue
        lowest_cost[(r, c, d)] = score  # if we're processing this is the min cost for the node
        backtrack[(r,c,d)].add((pr,pc,pd))
        if (r, c) == end:
            if score > min_score:
                break
            end_state = (r,c,d)
            min_score = min(min_score, score)
        else:
            nr, nc = r+directions[d][0], c+directions[d][1]
            next_moves = {(score+1, nr, nc, d), (score + 1000, r, c, (d+1) % 4), (score + 1000, r, c, (d-1) % 4)}
            for new_score, nr, nc, nd in next_moves:
                if grid[nr][nc] != '#' and score <= lowest_cost[(nr,nc,nd)]:
                    heapq.heappush(pq, (new_score, nr, nc, nd, r, c, d))
    
    optimal_paths, seen = deque([end_state]), set()
    while optimal_paths:
        state = optimal_paths.popleft()
        seen.add(state)
        for prev in backtrack[state]:
            if prev not in seen:
                seen.add(prev)
                optimal_paths.append(prev)
    seen = set((r,c) for r,c,_ in seen)

    return min_score, len(seen)-1


start, end = find_start_end()
min_score, seats = dijkstra(start, end)
print(min_score, seats)
#print(len({node for path in shortest_paths(start, end) for node in path}))
