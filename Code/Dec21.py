from collections import deque, defaultdict
from functools import lru_cache
from itertools import product
# pt1
# input -> rob1 soln -> rob1 input -> rob2 soln -> ...
# save the key coords to reduce duplicate work for finding starts and ends
# some optimal paths for one soln result in a sub optimal path for a next step
# pt2
# instead of solving the problem one level at a time
# solve each pair in the sequence all the way down to n dfs style
# and then reuse those calculations when calculating the other pairs
codes = [line.strip() for line in open('Input/Dec21.txt').readlines()]
seqs = defaultdict(list)  # (origin, dest) : list of paths
num_keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["", "0", "A"]
]
num_coords = {num_keypad[r][c]: (r, c) for r in range(
    len(num_keypad)) for c in range(len(num_keypad[r]))}

dir_keypad = [
    ["", "^", "A"],
    ["<", "v", ">"]
]
dir_coords = {dir_keypad[r][c]: (r, c) for r in range(
    len(dir_keypad)) for c in range(len(dir_keypad[r]))}


def bfs(src, dest, coords, keypad):
    if seqs[(src, dest)]:
        return seqs[(src, dest)]
    elif src == dest:
        seqs[(src, dest)] = ["A"]
        return seqs[(src, dest)]
    else:
        q = deque([(coords[src][0], coords[src][1], "")])
        min_dist = float('inf')
        while q:
            r, c, path = q.popleft()
            for nr, nc, mv in [(r-1, c, "^"), (r+1, c, "v"), (r, c-1, "<"), (r, c+1, ">")]:
                if (nr, nc) == coords[dest] and len(path)+1 <= min_dist:
                    seqs[(src, dest)].append(path+mv+'A')
                    min_dist = min(min_dist, len(path)+1)
                elif len(path)+1 > min_dist:
                    return seqs[(src, dest)]
                elif 0 <= nr < len(keypad) and 0 <= nc < len(keypad[nr]) and keypad[nr][nc]:
                    q.append((nr, nc, path+mv))
        return seqs[(src, dest)]


def solve_seq(seq):
    options = [seqs[(src, dest)] for src, dest in zip("A" + seq, seq)]
    return ["".join(x) for x in product(*options)]


def generate_paths(coords, keypad):
    flat = [key for row in keypad for key in row if key]
    for src in flat:
        for dest in flat:
            r1, c1 = coords[src]
            r2, c2 = coords[dest]
            if keypad[r1][c1] and keypad[r2][c2]:
                bfs(src, dest, coords, keypad)


def identical_neighbors(s):
    return sum(s[i] == s[i + 1] for i in range(len(s) - 1))


@lru_cache
def compute_length(seq, depth=25):
    if depth == 1:
        return sum(dir_lengths[(x, y)] for x, y in zip("A" + seq, seq))
    length = 0
    for x, y in zip("A" + seq, seq):
        length += min(compute_length(subseq, depth - 1)
                      for subseq in seqs[(x, y)])
    return length


def solve(codes):
    total = 0
    for code in codes:
        seqs = solve_seq(code)
        length = min(map(compute_length, seqs))
        total += length * int(code[:-1])
    return total


generate_paths(num_coords, num_keypad)
generate_paths(dir_coords, dir_keypad)
dir_lengths = {key: len(value[0]) for key, value in seqs.items()}
print(solve(codes))
