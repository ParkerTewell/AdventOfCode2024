from collections import Counter
with open('AdventOfCode2024/Input/Dec4.txt') as f:
    lines = f.readlines()

grid = [line.strip() for line in lines]


directions = {"N": (1, 0), "S": (-1, 0), "E": (0, 1), "W": (0, -1),
              "NE": (1, 1), "NW": (1, -1), "SE": (-1, 1), "SW": (-1, -1)}


def dfs(row, col, dir, word):
    n, m = len(grid), len(grid[0])
    if not word:
        return True
    elif 0 <= row < n and 0 <= col < m and grid[row][col] == word[0]:
        row += directions[dir][0]
        col += directions[dir][1]
        return dfs(row, col, dir, word[1:])
    else:
        return False


def pt1():
    soln = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "X":
                for dir in directions.keys():
                    soln += dfs(row, col, dir, "XMAS")
    return soln


def X(row, col):
    NE = (row+directions["NE"][0], col+directions["NE"][1])
    NW = (row+directions["NW"][0], col+directions["NW"][1])
    SE = (row+directions["SE"][0], col+directions["SE"][1])
    SW = (row+directions["SW"][0], col+directions["SW"][1])

    # in bounds
    for dir in [NE, NW, SE, SW]:
        n, m = len(grid), len(grid[0])
        if not (0 <= dir[0] < n and 0 <= dir[1] < m):
            return False

    # cannot have same letter diagonal from each other
    if grid[NE[0]][NE[1]] == grid[SW[0]][SW[1]] or grid[NW[0]][NW[1]] == grid[SE[0]][SE[1]]:
        return False
    # contains 2M & 2S
    letters = Counter([grid[NE[0]][NE[1]], grid[NW[0]][NW[1]],
                      grid[SE[0]][SE[1]], grid[SW[0]][SW[1]]])
    if letters['M'] != 2 or letters['S'] != 2:
        return False
    return True


def pt2():
    soln = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "A":
                soln += X(row, col)
    return soln


print(f"pt1, {pt1()}")
print(f"pt2, {pt2()}")
