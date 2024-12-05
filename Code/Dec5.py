from collections import defaultdict
from functools import cmp_to_key

with open('AdventOfCode2024/Input/Dec5.txt') as f:
    lines = f.readlines()

divider = lines.index('\n')
rules = [line.strip() for line in lines[:divider]]
updates = [line.strip() for line in lines[divider + 1:]]
ruleset = defaultdict(set)  # num: preceeds num
for r in rules:
    x, y = r.split('|')
    ruleset[x].add(y)


def pt1(updates):
    global ruleset
    soln, unsafe = 0, []
    for s in updates:
        safe = True
        seen = set()
        s = s.split(',')
        for c in s:
            if ruleset[c] & seen:
                safe = False
            seen.add(c)
        if safe:
            soln += int(s[(len(s)//2)])
        else:
            unsafe.append(s)
    return soln, unsafe


def pt2(updates):
    soln = 0
    for s in updates:
        s.sort(key=cmp_to_key(cmp))
        soln += int(s[(len(s)//2)])
    return soln


def cmp(x, y):
    global ruleset
    if y in ruleset[x]:
        return -1
    elif x in ruleset[y]:
        return 1
    return 0


soln1, unsafe_updates = pt1(updates)
print(soln1)
print(pt2(unsafe_updates))
