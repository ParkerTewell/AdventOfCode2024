import re


def pt1(regex, lines):
    soln = 0
    for line in lines:
        matches = re.findall(regex, line)
        for x, y in matches:
            soln += int(x)*int(y)
    return soln


def pt2(regex, lines):
    soln, enabled = 0, True
    for line in lines:
        matches = re.findall(regex, line)
        for x, y, dont, do in matches:
            if dont:
                enabled = False
            elif do:
                enabled = True
            elif enabled:
                soln += int(x)*int(y)
    return soln


with open('AdventOfCode2024/Input/Dec3.txt') as f:
    lines = f.readlines()

regex1 = r"mul\((\d{1,3}),(\d{1,3})\)"
print("pt1", pt1(regex1, lines))
regex2 = r"mul\((\d{1,3}),(\d{1,3})\)|(don't)|(do)"
print("pt2", pt2(regex2, lines))
