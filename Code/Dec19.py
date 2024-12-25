lines = open('Input/Dec19.txt').readlines()
patterns = lines[0].strip().split(', ')
designs = [d.strip() for d in lines[2:]]
maxLen = max(map(len, patterns))
seen = {}


def completable(d):
    if d == '':
        return True
    if d in seen:
        return seen[d]
    for i in range(min(len(d), maxLen)+1):
        if d[:i] in patterns and completable(d[i:]):
            seen[d] = True
            return True
    seen[d] = False
    return False


print(sum(completable(d) for d in designs))
