import re

with open('Input/Dec17.txt') as f:
    lines = f.readlines()
    A = int(re.search(r'\d+', lines[0]).group())
    B = int(re.search(r'\d+', lines[1]).group())
    C = int(re.search(r'\d+', lines[2]).group())
    instructions = list(map(int, re.findall(r'\d', lines[-1])))


def adv(A, num):
    return A // 2**num
    # print(f'A {A}')


def bxl(B, num):
    return B ^ num
    # print(f"B {B}")


def combo(A, B, C, num):
    if num == 4:
        num = A
    elif num == 5:
        num = B
    elif num == 6:
        num = C
    return num


def bst(num):
    return num % 8


def out(num):
    return str((num) % 8)


def jnz(A, num, ptr):
    return num if A != 0 else ptr
    # print(f"jnz {ptr}")


def bxc(B, C):
    return B ^ C


def bdv(A, num):
    return A // 2**num


def cdv(A, num):
    return A // 2**num


def pt1(A, B, C, instructions):
    ptr, eof, output = 0, len(instructions), []

    while ptr < eof:
        opcode = instructions[ptr]
        literal = instructions[ptr + 1]
        ptr += 2

        match opcode:
            case 0:
                A = adv(A, literal)
            case 1:
                B = bxl(B, literal)
            case 2:
                literal = combo(A, B, C, literal)
                B = bst(literal)
            case 3:
                ptr = jnz(A, literal, ptr)
            case 4:
                B = bxc(B, C)
            case 5:
                literal = combo(A, B, C, literal)
                output.append(out(literal))
            case 6:
                B = bdv(A, literal)
            case 7:
                literal = combo(A, B, C, literal)
                C = cdv(A, literal)

    return output


# The last three bits of A determine the output; so we find the right-hand digit
# of the program then shift A three bits and try another value 0-7
# we continue this until we've found all values in program.
def pt2(A, B, C, instructions, compare_index):
    result = set()
    for n in range(8):
        A2 = (A << 3) | n
        output = list(map(int, pt1(A2, B, C, instructions)))
        # print(output)
        # print(instructions[-compare_index:])
        if output == instructions[-compare_index:]:
            if output == instructions:
                result.add(A2)
            else:
                possible = pt2(A2, B, C, instructions, compare_index+1)
                if possible:
                    result.add(possible)

    if len(result) > 0:
        return min(result)
    else:
        return 0


print(','.join(pt1(A, B, C, instructions)))
print(pt2(0, 0, 0, instructions, 1))
