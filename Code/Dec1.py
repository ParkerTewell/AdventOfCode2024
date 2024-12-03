from heapq import heappush, heappop
from collections import Counter

with open('AdventOfCode2024/Input/Dec1.txt') as f:
    lines = f.readlines()
left, right = [], []

# parse input
for line in lines:
    x, y = map(int, line.split())
    heappush(left, x)   # min heap
    heappush(right, y)  # min heap

# part 2
counts = Counter(right)
soln2 = 0
for i in set(left):
    soln2 += i*counts[i]

# part 1
soln1 = 0
while left and right:
    soln1 += abs(heappop(left)-heappop(right))

print("pt1", soln1)
print("pt2", soln2)
