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


# whenever we turn we want to check if we can make a loop
# assume the node you're at is the top left of the square
# 1 down and m right   <- corner 1
# 1 left and n down    <- corner 2
# n down and m+1 right <- corner 3
#
# check corner 1 & 2 first
# if neither exist there cannot be a loop
# if both exist there can be a loop
# if one exists check corner 3 -> True if corner 3 else False
#   if corner 1 exists go 1 left and m down (from corner 1)
#   if corner 2 exists go 1 down and n right (from corner 2)
def check_square(r, c):
    M, N = len(grid), len(grid[0])
    c1, m = check_direction(r+1, c, 0, 1)
    # print(f"Check corner 1 input: {r+1, c} output: {c1, m}")
    c2, n = check_direction(r, c-1, 1, 0)
    # print(f"Check corner 2 input: {r, c-1} output: {c2, n}")
    if c1 and c2:
        return True
    elif c1:
        print(r, m-1)
        c3, _ = check_direction(r, m-1, 1, 0)
        return c3
    elif c2:
        c3, _ = check_direction(n-1, c, 0, 1)
        return c3
    else:
        return False


def check_direction(r, c, rd, cd):
    n, m = len(grid), len(grid[0])
    while 0 <= r < n and 0 <= c < m:
        # print(r, c, grid[r][c])
        if grid[r][c] == "#":
            # print("Check direction found match")
            return True, r if rd else c
        r, c = r+rd, c+cd
    return False, -1


def pt2(pos):
    soln = 0
    r, c = pos[0], pos[1]
    n, m = len(grid), len(grid[0])
    while 0 <= r < n and 0 <= c < m:
        rd, cd, orientation = directions[grid[r][c]]
        if not (0 <= r+rd < n and 0 <= c+cd < m):
            break
        if grid[r+rd][c+cd] == "#":
            print(f"Checking {r+rd, c+cd} as top left corner")
            soln += check_square(r+rd, c+cd)
            print(f"SOL2: {soln}")
            grid[r][c] = directions[(orientation+1) % 4]
            rd, cd, _ = directions[grid[r][c]]
        else:
            grid[r+rd][c+cd] = directions[orientation]
            r, c = r+rd, c+cd

    return soln


for r in grid:
    print(r)

sol2 = pt2(pos)
print(sol2)
# pt1 = pt1(pos)
# print(f"pt1: {pt1}\npt2: {pt2}")
