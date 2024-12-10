from collections import defaultdict, deque
with open('Input/Dec9.txt') as f:
    line = f.readline()

blocks, ID, free_space = [], 0, False
file_length, stack, file_start = defaultdict(
    int), deque(), {}  # needed for pt2

i = 0
for c in line:
    for _ in range(int(c)):
        if not free_space:
            file_length[ID] += 1
            stack.append(ID)
            # the starting position of the file, add length to get end bound
            if ID not in file_start:
                file_start[ID] = i
        blocks += ['.'] if free_space else [f'{ID}']
        i += 1
    free_space = not free_space
    ID += free_space
# print(''.join(blocks))
# print(file_start)


def pt1():
    lptr, rptr = blocks.index('.'), len(blocks)-1
    while lptr < rptr:
        blocks[lptr] = blocks[rptr]
        blocks[rptr] = '.'
        while lptr < rptr and blocks[lptr] != '.':
            lptr += 1
        while lptr < rptr and blocks[rptr] == '.':
            rptr -= 1
    return sum([int(blocks[i]) * i for i in range(lptr)])


def calc_dist(lptr):
    rptr = lptr+1
    while rptr < len(blocks) and blocks[rptr] == '.':
        rptr += 1
    return rptr-lptr


def fill_space(lptr, dist):
    global stack
    queue = deque()
    while stack and file_length[stack[-1]] > dist:
        queue.appendleft(stack.pop())
    if stack:
        f = stack.pop()
        stack += queue
        move_file(f, lptr)
        free_space(f)


def move_file(file, ptr):
    for i in range(file_length[file]):
        blocks[ptr+i] = str(file)


def free_space(file):
    for i in range(file_length[file]):
        blocks[file_start[file]+i] = '.'


def pt2():
    global blocks
    lptr = blocks.index('.')
    while lptr < len(blocks):
        dist = calc_dist(lptr)
        # print(f"free space: {dist}")
        fill_space(lptr, dist)
        # print(''.join(blocks))
        lptr += 1  # skip space if no file is small enough
        while lptr < len(blocks) and blocks[lptr] != '.':
            lptr += 1
    return sum2()


def sum2():
    ret = 0
    for i in range(len(blocks)):
        if blocks[i] != ".":
            ret += int(blocks[i]) * i
    return ret


# print(pt1())
print(pt2())
# print(''.join(blocks))
# print(file_length)
