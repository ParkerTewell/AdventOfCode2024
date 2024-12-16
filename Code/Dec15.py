from copy import deepcopy
from itertools import chain
with open('Input/Dec15.txt') as f:
    lines = f.readlines()
    grid = [list(line.strip())
            for line in lines if line.strip()][:lines.index('\n')]
    moves = ''.join(line.strip() for line in lines[len(grid):])

directions = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
n, m = len(grid), len(grid[0])


def find_start(grid):
    n, m = len(grid), len(grid[0])
    for r in range(n):
        for c in range(m):
            if grid[r][c] == "@":
                return (r, c)


def push_boxes(pos, dir, grid):
    start, ret = pos, False
    while grid[pos[0]][pos[1]] == "O":
        pos = (pos[0]+directions[dir][0], pos[1]+directions[dir][1])
    if grid[pos[0]][pos[1]] == ".":
        grid[pos[0]][pos[1]] = "O"
        grid[start[0]][start[1]] = "@"
        ret = True
    return ret


def sum_boxes(grid):
    n, m = len(grid), len(grid[0])
    sum = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] in "O[":
                sum += 100*r+c
    return sum


def pt1(grid):
    n, m = len(grid), len(grid[0])
    pos = find_start(grid)
    for dir in moves:
        new_pos = (pos[0]+directions[dir][0], pos[1]+directions[dir][1])
        if (0, 0) <= new_pos <= (n, m):
            if grid[new_pos[0]][new_pos[1]] == "O" and push_boxes(new_pos, dir, grid):
                grid[pos[0]][pos[1]] = "."
                pos = new_pos
            elif grid[new_pos[0]][new_pos[1]] == ".":
                grid[pos[0]][pos[1]] = '.'
                pos = new_pos
                grid[pos[0]][pos[1]] = '@'

    return sum_boxes(grid)


def fatten_grid(grid):
    fat_grid = []
    for r in grid:
        fat_row = []
        for c in r:
            if c == "@":
                c += "."
            elif c == "O":
                c = "[]"
            else:
                c *= 2
            fat_row.append(c[0])
            fat_row.append(c[1])
        fat_grid.append(fat_row)
    return fat_grid


def pt2():
    global grid
    pos = find_start(grid)
    with open("mysoln.txt", "w") as file:
        for dir in moves:
            new_pos = (pos[0]+directions[dir][0], pos[1]+directions[dir][1])
            if (0, 0) <= new_pos <= (n, m):
                if grid[new_pos[0]][new_pos[1]] in "[]" and push_fat_boxes(new_pos, dir):
                    grid[pos[0]][pos[1]] = "."
                    pos = new_pos
                    grid[pos[0]][pos[1]] = '@'
                elif grid[new_pos[0]][new_pos[1]] == ".":
                    grid[pos[0]][pos[1]] = '.'
                    pos = new_pos
                    grid[pos[0]][pos[1]] = '@'
                file.write(f"move {dir}\n")
                for r in grid:
                    r = ''.join(r)
                    file.write(f"{r}\n")
    return sum_boxes(grid)


def push_fat_boxes(pos, dir):
    return lateral_push(pos, dir) if dir in "<>" else vertical_push(pos, dir)


def vertical_push(pos, dir):
    global grid
    boxes = detect_region(pos, dir, set())
    boxes = sorted(boxes) if dir == '^' else sorted(boxes, reverse=True)
    # print(boxes)
    no_walls = not has_wall(boxes, dir)

    if no_walls:
        sim_vert_push(boxes, dir)

    return no_walls


def sim_vert_push(region, dir):
    for r, c in region:
        grid[r+directions[dir][0]][c] = grid[r][c]
        grid[r][c] = '.'


def detect_region(pos, dir, region):
    if pos in region:
        return region

    if grid[pos[0]][pos[1]] == '[':
        region.add(pos)
        region |= detect_region((pos[0], pos[1]+1), dir, region)
        region |= detect_region(
            (pos[0]+directions[dir][0], pos[1]), dir, region)
    if grid[pos[0]][pos[1]] == ']':
        region.add(pos)
        region |= detect_region((pos[0], pos[1]-1), dir, region)
        region |= detect_region(
            (pos[0]+directions[dir][0], pos[1]), dir, region)
    return region


def has_wall(region, dir):
    for box in region:
        if grid[box[0]+directions[dir][0]][box[1]] == "#":
            return True
    return False


def lateral_push(pos, dir):
    global grid
    # print("lateral push")
    start, ret = pos, False
    # print(grid[pos[0]][pos[1]])
    while grid[pos[0]][pos[1]] in "[]":
        pos = (pos[0]+directions[dir][0], pos[1]+directions[dir][1])
        # print(pos, grid[pos[0]][pos[1]])
        end = pos
        if grid[pos[0]][pos[1]] == ".":
            # print("run lat push")
            end = pos
            box_start = (start[0]+directions[dir][0],
                         start[1]+directions[dir][1])
            sim_lat_push(box_start, end, dir)
            grid[start[0]][start[1]] = "@"
            ret = True
            break
    return ret


def sim_lat_push(start, end, dir):
    global grid
    pos, alt = start, False if dir == ">" else True
    # print("end", end)
    while pos != end:
        # print(pos)
        grid[pos[0]][pos[1]] = "]" if alt else "["
        alt = not alt
        pos = (pos[0]+directions[dir][0], pos[1]+directions[dir][1])
    grid[end[0]][end[1]] = "]" if alt else "["


grid = fatten_grid(grid)
n, m = len(grid), len(grid[0])
print(pt2())
# for r in grid:
#     print(r)
