import re
from collections import deque
from operator import xor, and_, or_

lines = open('Input/Dec24.txt').readlines()
divider = lines.index('\n')
wires = {line[:3]: int(line[-2]) for line in lines[:divider]}
ops = deque(re.findall(r'(\w+)', line) for line in lines[divider + 1:])
op_map = {'XOR': xor, 'AND': and_, 'OR': or_}


def pt1(wires, ops, base=2):
    while ops:
        w1, op, w2, w3 = ops.popleft()
        if w1 in wires and w2 in wires:
            wires[w3] = op_map[op](wires[w1], wires[w2])
        else:
            ops.append([w1, op, w2, w3])
    return int(''.join(map(lambda k: str(wires[k]), sorted(
        [w for w in wires if w[0] == 'z'], reverse=True))), base)


print(pt1(wires, ops))
print(pt1(wires, ops, 10))

# pt2
# the result of x+y should equal the output of the program
# printed both, run thru the program and just manually swap the outputs where they mismatch
# something about a full/ half adder i have no idea its easy to just write it out
x = int(''.join(map(lambda k: str(wires[k]), sorted(
    [w for w in wires if w[0] == 'x'], reverse=True))), base=2)
y = int(''.join(map(lambda k: str(wires[k]), sorted(
    [w for w in wires if w[0] == 'y'], reverse=True))), base=2)
print(bin(x+y)[2:])
