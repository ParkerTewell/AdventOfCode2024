# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.

with open('AdventOfCode2024/Input/Dec2.txt') as f:
    lines = f.readlines()


def checkLine(ls, tolerance=0):
    asc = ls[0] < ls[-1]
    isSafe = True
    mistakes = 0
    for i in range(1, len(ls)):
        if asc and ls[i-1] < ls[i] and 1 <= abs(ls[i-1]-ls[i]) <= 3:
            pass
        elif not asc and ls[i-1] > ls[i] and 1 <= abs(ls[i-1]-ls[i]) <= 3:
            pass
        else:
            isSafe = False if mistakes >= tolerance else isSafe
            mistakes += 1
    return isSafe


def pt1(lines):
    badLines = []  # needed for pt2
    soln1 = 0
    for line in lines:
        ls = list(map(int, line.split()))
        isSafe = checkLine(ls)
        if not isSafe:
            badLines.append(ls)
        soln1 += isSafe
    return soln1, badLines


def pt2(badLines):
    soln2 = 0
    for line in badLines:
        for i in range(len(line)):
            isSafe = checkLine(line[:i] + line[i+1:])
            if isSafe:
                break
        soln2 += isSafe
    return soln2


soln1, badLines = pt1(lines)
soln2 = pt2(badLines)+soln1

print("pt1", soln1)
print("pt2", soln2)
