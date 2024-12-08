from collections import Counter
with open('AdventOfCode2024/Input/Dec6.txt') as f:
    lines = f.readlines()

directions = {"^": (-1, 0, 0), "v": (1, 0, 2), ">": (0, 1, 1),
              "<": (0, -1, 3), 0: "^", 1: ">", 2: "v", 3: "<"}
grid, pos = [], ()
for r in range(len(lines)):
    line = list(lines[r].strip())
    grid.append(line)
    for c in range(len(line)):
        if line[c] in directions.keys():
            pos = (r, c)


def pt1(pos):
    soln = 0
    r, c = pos[0], pos[1]
    n, m = len(grid), len(grid[0])
    while 0 <= r < n and 0 <= c < m:
        rd, cd, orientation = directions[grid[r][c]]
        if not (0 <= r+rd < n and 0 <= c+cd < m):
            soln += 1
            break
        if grid[r+rd][c+cd] == "#":
            grid[r][c] = directions[(orientation+1) % 4]
            rd, cd, _ = directions[grid[r][c]]
        elif grid[r+rd][c+cd] == ".":
            grid[r][c] = "X"
            grid[r+rd][c+cd] = directions[orientation]
            soln += 1
            r, c = r+rd, c+cd
        elif grid[r+rd][c+cd] == "X":
            grid[r][c] = "X"
            grid[r+rd][c+cd] = directions[orientation]
            r, c = r+rd, c+cd

    return soln


def pt2(pos):
    times_visited_wall = Counter()
    r, c = pos[0], pos[1]
    n, m = len(grid), len(grid[0])
    while 0 <= r < n and 0 <= c < m:
        rd, cd, orientation = directions[grid[r][c]]
        if not (0 <= r+rd < n and 0 <= c+cd < m):
            break
        if grid[r+rd][c+cd] == "#":
            grid[r][c] = directions[(orientation+1) % 4]
            rd, cd, _ = directions[grid[r][c]]

            times_visited_wall[(r+rd, c+cd)] += 1
            if 3 in times_visited_wall.values():
                return True
        else:
            grid[r+rd][c+cd] = directions[orientation]
            r, c = r+rd, c+cd

    return False


def brute_force_pt2(pos):
    soln = 0
    n, m = len(grid), len(grid[0])
    for r in range(n):
        for c in range(m):
            if grid[r][c] != "#" and (r, c) != pos:
                grid[pos[0]][pos[1]] = "^"
                grid[r][c] = "#"
                res = pt2(pos)
                if res:
                    soln += res

                grid[r][c] = "."
    return soln


sol1 = pt1(pos)
sol2 = brute_force_pt2(pos)
print(sol2)
