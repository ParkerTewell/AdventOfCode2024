import re

with open('Input/Dec17.txt') as f:
    lines = f.readlines()
    A = int(re.search(r'\d+', lines[0]).group())
    B = int(re.search(r'\d+', lines[1]).group())
    C = int(re.search(r'\d+', lines[2]).group())
    instructions = list(map(int, re.findall(r'\d', lines[-1])))
    target = ','.join(re.findall(r'\d', lines[-1]))
    ptr, eof, output = 0, len(instructions), ''


def divA(A, num):
    return A // 2**num
    # print(f'A {A}')


def xor(B, num):
    return B ^ num
    # print(f"B {B}")


def convert(A, B, C, num):
    if num == 4:
        num = A
    elif num == 5:
        num = B
    elif num == 6:
        num = C
    return num


def combo(num):
    return num % 8


def out(num):
    return str((num) % 8)+','


def jump(A, num, ptr):
    return num if A != 0 else ptr
    # print(f"jump {ptr}")


def BxorC(B, C):
    return B ^ C


def divB(A, num):
    return A // 2**num


def divC(A, num):
    return A // 2**num


ops = {0: divA, 1: xor, 2: combo, 3: jump,
       4: BxorC, 5: out, 6: divB, 7: divC}


def pt1(A, B, C, instructions):
    ptr, eof, output = 0, len(instructions), ''

    while ptr < eof:
        opcode = instructions[ptr]
        literal = instructions[ptr + 1]
        ptr += 2

        # Match the opcode with the corresponding function directly
        match opcode:
            case 0:
                A = divA(A, literal)
            case 1:
                B = xor(B, literal)
            case 2:
                literal = convert(A, B, C, literal)
                B = combo(literal)
            case 3:
                ptr = jump(A, literal, ptr)
            case 4:
                B = BxorC(B, C)
            case 5:
                literal = convert(A, B, C, literal)
                output += out(literal)
            case 6:
                B = divB(A, literal)
            case 7:
                literal = convert(A, B, C, literal)
                C = divC(A, literal)

    return output[:-1]


def pt2(B, C, instructions, target):
    output = ''
    newA = 100000000000000

    while output != target:
        newA += 1
        output = pt1(newA, B, C, instructions)
        if newA % 100000000 == 0:
            print(newA)

    return newA


output = pt1(A, B, C, instructions)
print(output)
print(pt2(B, C, instructions, target))
