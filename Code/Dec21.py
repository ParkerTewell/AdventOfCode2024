import re
from collections import deque, defaultdict

# input -> rob1 soln -> rob1 input -> rob2 soln -> ...
# save the key coords to reduce duplicate work for finding starts and ends
from collections import deque, defaultdict
from itertools import product

codes = [line.strip() for line in open('Input/Dec21.txt').readlines()]
cache = defaultdict(set)  # (origin, dest) : list of paths
num_keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"]
]
num_coords = {num_keypad[r][c]: (r, c) for r in range(
    len(num_keypad)) for c in range(len(num_keypad[r]))}
dir_keypad = [
    [None, "^", "A"],
    ["<", "v", ">"]
]
dir_coords = {dir_keypad[r][c]: (r, c) for r in range(
    len(dir_keypad)) for c in range(len(dir_keypad[r]))}


def bfs(src, dest, coords, keypad):
    if cache[(src, dest)]:
        return cache[(src, dest)]
    elif src == dest:
        cache[(src, dest)] = {"A"}
        return cache[(src, dest)]
    else:
        q = deque([(coords[src][0], coords[src][1], "")])
        min_dist = float('inf')
        while q:
            r, c, path = q.popleft()
            for nr, nc, mv in [(r-1, c, "^"), (r+1, c, "v"), (r, c-1, "<"), (r, c+1, ">")]:
                if (nr, nc) == coords[dest] and len(path)+1 <= min_dist:
                    cache[(src, dest)].add(path+mv+'A')
                    min_dist = min(min_dist, len(path)+1)
                elif len(path)+1 > min_dist:
                    return cache[(src, dest)]
                elif 0 <= nr < len(keypad) and 0 <= nc < len(keypad[nr]) and keypad[nr][nc]:
                    q.append((nr, nc, path+mv))
        return cache[(src, dest)]


def solve(seq):
    options = [cache[(src, dest)] for src, dest in zip("A" + seq, seq)]
    return ["".join(x) for x in product(*options)]


def generate_paths(coords, keypad):
    flat = [key for row in keypad for key in row if key]
    for src in flat:
        for dest in flat:
            r1, c1 = coords[src]
            r2, c2 = coords[dest]
            if keypad[r1][c1] is not None and keypad[r2][c2] is not None:
                bfs(src, dest, coords, keypad)


def identical_neighbors(s):
    return sum(s[i] == s[i + 1] for i in range(len(s) - 1))


def calc_complexity(codes):
    total = 0
    for code in codes:
        robot1 = solve(code)
        next = robot1
        for _ in range(25):
            paths = []
            for seq in next:
                paths += solve(seq)
            # some optimal paths for one soln result in a sub optimal path for a next step
            minlen = min(map(len, paths))
            next = [seq for seq in paths if len(seq) == minlen]
            next = sorted(next, key=identical_neighbors, reverse=True)
            # print(next[0])
        total += len(next[0]) * int(code[:-1])
    return total


generate_paths(num_coords, num_keypad)
generate_paths(dir_coords, dir_keypad)
print(calc_complexity(codes))
