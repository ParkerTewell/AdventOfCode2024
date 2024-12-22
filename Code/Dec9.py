from collections import defaultdict
with open('Input/Dec9.txt') as f:
    line = f.readline()

blocks, ID, free_space = [], 0, False
file_length, file_start = defaultdict(int), {}  # needed for pt2

i = 0
for c in line:
    for _ in range(int(c)):
        if not free_space:
            file_length[ID] += 1
            # the starting position of the file, add length to get end bound
            if ID not in file_start:
                file_start[ID] = i
        blocks += ['.'] if free_space else [f'{ID}']
        i += 1
    free_space = not free_space
    ID += free_space
stack = [i for i in range(ID)]


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
    pass


def move_file(file, ptr):
    for i in range(file_length[file]):
        blocks[ptr+i] = str(file)


def free_space(file):
    for i in range(file_length[file]):
        blocks[file_start[file]+i] = '.'


def pt2():
    while stack:
        f = stack.pop()
        lptr = blocks.index('.')

        while lptr < len(blocks) and lptr < file_start[f]:
            dist = calc_dist(lptr)
            if dist >= file_length[f]:
                move_file(f, lptr)
                free_space(f)
                break

            lptr += 1  # skip space if no file is small enough
            while lptr < len(blocks) and blocks[lptr] != '.':
                lptr += 1
    return sum([int(blocks[i]) * i if blocks[i] != "." else 0 for i in range(len(blocks))])


# print(pt1())
print(pt2())
