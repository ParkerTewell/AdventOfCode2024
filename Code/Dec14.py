from re import findall
import numpy as np
import re
import math
import matplotlib.pyplot as plt
from seaborn import heatmap
with open('Input/Dec14.txt') as f:
    robots = [list(map(int, re.findall(r'-?\d+', line)))
              for line in f.readlines()]

w, h = 101, 103


def simulate(seconds):
    return [((robots[i][0]+robots[i][2]*seconds) % w, (robots[i][1]+robots[i][3]*seconds) % h) for i in range(len(robots))]


def countQuadrants(robots):
    # (row bounds, col bounds)
    Q1 = (0, w//2-1, 0, h//2-1)
    Q2 = (0, w//2-1, h//2+1, h-1)
    Q3 = (w//2+1, w-1, 0, h//2-1)
    Q4 = (w//2+1, w-1, h//2+1, h-1)
    sums = [0] * 4

    for r in robots:
        for q, bounds in enumerate([Q1, Q2, Q3, Q4]):
            if bounds[0] <= r[0] <= bounds[1] and bounds[2] <= r[1] <= bounds[3]:
                sums[q] += 1
    return math.prod(sums)


def findTree(start, end):
    vars = []
    for i in range(start, end+1):
        grid = np.array([[0] * w for _ in range(h)])
        res = simulate(i)
        for x, y in res:
            grid[y][x] += 1
        vars.append((i, np.var(grid)))
    i, _ = min(vars, key=lambda x: x[1])
    plot_grid(i)
    return i


def plot_grid(i):
    grid = np.array([[0] * w for _ in range(h)])
    res = simulate(i)
    for x, y in res:
        grid[y][x] += 1
    plt.figure(figsize=(10, 10))
    heatmap(grid)
    plt.show()


print(countQuadrants(simulate(100)))  # pt1
print(findTree(1, 10000))  # pt2
