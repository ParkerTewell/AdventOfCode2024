from collections import defaultdict
lines = open('Input/Dec19.txt').readlines()
patterns = lines[0].strip().split(', ')
designs = [d.strip() for d in lines[2:]]
maxLen = max(map(len, patterns))
seen = defaultdict(int)


def completable(d):
    if d == '':
        return 1
    if d in seen:
        return seen[d]
    for i in range(min(len(d), maxLen)+1):
        if d[:i] in patterns and completable(d[i:]):
            seen[d] += completable(d[i:])
    return seen[d]


soln = [completable(d) for d in designs]
print(sum(True if s else False for s in soln))
print(sum(soln))
