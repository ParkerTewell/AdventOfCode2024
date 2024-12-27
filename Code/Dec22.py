from collections import defaultdict, deque
nums = list(map(int, open('Input/Dec22.txt').readlines()))
mod = 16777216


def step(num):
    num = (num ^ num*64) % mod
    num = (num ^ num//32) % mod
    num = (num ^ num*2048) % mod
    return num


def solve(nums):
    soln = 0
    for num in nums:
        for _ in range(2000):
            num = step(num)
        soln += num
    return soln


def genPrices(nums):
    prices = []
    for num in nums:
        price = []
        for _ in range(2000):
            num = step(num)
            price.append(num % 10)
        prices.append(price)
    return prices


def findMaxWindow(nums):
    prices = genPrices(nums)
    seqProfits = defaultdict(int)
    for p in prices:
        seen, seq = set(), deque([p[0]-p[1], p[1]-p[2], p[2]-p[3]], maxlen=4)

        for i in range(3, len(p)-1):
            seq.append(p[i]-p[i+1])
            tup = tuple(seq)
            if tup not in seen:
                seqProfits[tup] += p[i+1]
                seen.add(tup)

    return max(seqProfits.values())


print(solve(nums))
print(findMaxWindow(nums))
