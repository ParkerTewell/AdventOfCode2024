from collections import defaultdict
from operator import add, sub
with open('AdventOfCode2024/Input/Dec8.txt') as f:
    grid = [line.strip() for line in f.readlines()]


nodes = defaultdict(set)
n, m = len(grid), len(grid[0])
for r in range(n):
    for c in range(m):
        if grid[r][c] != '.':
            nodes[grid[r][c]].add((r, c))

# for every pair of nodes
#   count the distance between them (x)
#   check if points exist x distance away from either of them


def pt1(nodes):
    antinodes = set()
    for node in nodes:
        for pos1 in nodes[node]:
            for pos2 in nodes[node]:
                if pos2 != pos1:
                    distance = (pos1[0]-pos2[0], pos1[1]-pos2[1])
                    if 0 <= pos1[0]+distance[0] < n and 0 <= pos1[1]+distance[1] < m:
                        antinodes.add(
                            (pos1[0]+distance[0], pos1[1]+distance[1]))
                    if 0 <= pos2[0]-distance[0] < n and 0 <= pos2[1]-distance[1] < m:
                        antinodes.add(
                            (pos2[0]-distance[0], pos2[1]-distance[1]))

    return len(antinodes)


def resonant_harmonics(pos, delta, op):
    antinodes = set()
    while 0 <= op(pos[0], delta[0]) < n and 0 <= op(pos[1], delta[1]) < m:
        antinodes.add((op(pos[0], delta[0]), op(pos[1], delta[1])))
        pos = (op(pos[0], delta[0]), op(pos[1], delta[1]))
    return antinodes


def pt2(nodes):
    antinodes = set()
    for node in nodes:
        for pos1 in nodes[node]:
            for pos2 in nodes[node]:
                if pos2 != pos1:
                    distance = (pos1[0]-pos2[0], pos1[1]-pos2[1])
                    antinodes |= resonant_harmonics(pos1, distance, add)
                    antinodes |= resonant_harmonics(pos1, distance, sub)

    return len(antinodes)


print(pt1(nodes))
print(pt2(nodes))
