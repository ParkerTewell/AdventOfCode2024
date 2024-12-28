from collections import defaultdict, deque
graph = defaultdict(set)
for conn in open('Input/Dec23.txt').readlines():
    x, y = conn.strip().split('-')
    graph[x].add(y)
    graph[y].add(x)


def bfs(src):
    q = deque([(src, 1, {src})])
    groups = set()
    while q:
        node, dist, path = q.popleft()
        if dist > 4:
            break
        elif dist == 4 and node == src:
            groups.add(tuple(sorted(path)))
        else:
            for nei in graph[node]:
                q.append((nei, dist+1, path | {nei}))
    return groups


def pt1():
    t_comps = [node for node in graph if node[0] == 't']
    groups = set()
    for node in graph:
        groups |= bfs(node)
    return len([group for group in groups if any(g in t_comps for g in group)])


def dfs(node, path, seen):
    tup = tuple(sorted(path))
    if tup in seen:
        return seen
    seen.add(tup)
    for nei in graph[node]:
        if nei not in path and path <= graph[nei]:
            seen |= dfs(nei, path | {nei}, seen)
    return seen


def pt2():
    groups = set()
    for node in graph:
        groups |= dfs(node, {node}, groups)
    return ','.join(sorted(max(groups, key=len)))


# print(pt1())
print(pt2())
