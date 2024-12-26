import re
from collections import deque, defaultdict

# input -> rob1 soln -> rob1 input -> rob2 soln -> ...
# save the key coords to reduce duplicate work for finding starts and ends
codes = [line.strip() for line in open('Input/Dec21.txt').readlines()]
num_keypad = [["7", "8", "9"],
              ["6", "5", "4"],
              ["3", "2", "1"],
              ["", "0", "A"]]
num_coords = {num_keypad[r][c]: (r, c) for r in range(
    len(num_keypad)) for c in range(len(num_keypad[r]))}

dir_keypad = [["", "^", "A"],
              ["<", "v", ">"]]
dir_coords = {dir_keypad[r][c]: (r, c) for r in range(
    len(dir_keypad)) for c in range(len(dir_keypad[r]))}

# saves optimal paths from one key to another
cache = defaultdict(set)  # (origin, dest) : list of paths


def bfs(src, dest, coords, keypad):
    q, min_dist = deque(
        [(coords[src][0], coords[src][1], "")]), float('inf')
    if cache[(src, dest)]:
        return cache[(src, dest)]
    elif src == dest:
        cache[(src, dest)] = "A"
        return cache[(src, dest)]
    else:
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


def solve(codes, coords, keypad):
    for code in codes:
        code = "A"+code
        result = []
        for i in range(len(code)-1):
            # print(f"Find shortest path between {code[i], code[i+1]}")
            bfs(code[i], code[i+1], coords, keypad)
            # print(cache[code[i], code[i+1]])
            result = [
                path + p for path in result or [''] for p in cache[code[i], code[i+1]]]
            # print(f"result {result}")
    return result


def identical_neighbors(s):
    return sum(s[i] == s[i + 1] for i in range(len(s) - 1))


def pt1(codes):
    soln = 0
    for code in codes:
        num = int(re.search(r'\d+', code).group())
        rob1 = solve([code], num_coords, num_keypad)
        # some optimal paths for one soln result in a sub optimal path for a next step
        rob1 = sorted(rob1, key=lambda x: identical_neighbors(x), reverse=True)

        rob2 = solve([rob1[0]], dir_coords, dir_keypad)
        rob2 = sorted(rob2, key=lambda x: identical_neighbors(x), reverse=True)
        # print(min(map(len, rob2)), max(map(len, rob2)))

        rob3 = solve([rob2[0]], dir_coords, dir_keypad)
        rob3 = sorted(rob3, key=lambda x: identical_neighbors(x), reverse=True)
        # print(min(map(len, rob3)), max(map(len, rob3)))
        print(f"{len(rob3[0])} * {num}")
        soln += len(rob3[0]) * num
    return soln


print(pt1(codes))
