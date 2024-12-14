import re
with open('Input/Dec13.txt') as f:
    lines = f.readlines()
    A, B, prizes = [], [], []
    for i in range(0, len(lines), 4):
        A.append(tuple(map(int, re.findall(r'\d+', lines[i]))))
        B.append(tuple(map(int, re.findall(r'\d+', lines[i+1]))))
        prizes.append(tuple(map(int, re.findall(r'\d+', lines[i+2]))))
# Example:                   General:
# Button A: X+94, Y+34       Button A: X+x_a, Y+y_a
# Button B: X+22, Y+67       Button B: X+x_b, Y+y_b
# Prize: X=8400, Y=5400      Prize: X=x_p, Y=y_p
# 94a + 22b = 8400           (x_a)a + (x_b)b = x_p
# 34a + 67b = 5400           (y_a)a + (y_b)b = y_p
# 60a - 45b = 3000
# 60a = 45b + 3000           (y_b)(x_a)a + (y_b)(x_b)b = (y_b)x_p                     (y_a)(x_a)a + (y_a)(x_b)b = (y_a)x_p
# a = .75b + 50              (x_b)(y_a)a + (x_b)(y_b)b = (x_b)y_p                     (x_a)(y_a)a + (x_a)(y_b)b = (x_a)y_p
#
#                            (y_b)(x_a)a - (x_b)(y_a)a = (y_b)x_p - (x_b)y_p          (y_a)(x_b)b - (x_a)(y_b)b = (y_a)x_p - (x_a)y_p
#                            a((y_b)(x_a) - (x_b)(y_a)) = (y_b)x_p - (x_b)y_p         b((y_a)(x_b) - (x_a)(y_b)) = (y_a)x_p - (x_a)y_p
#                            a = ((y_b)x_p - (x_b)y_p)/((y_b)(x_a) - (x_b)(y_a))      b = ((y_a)x_p - (x_a)y_p)/((y_a)(x_b) - (x_a)(y_b))


def solve(constant):
    soln = 0
    for a, b, p in zip(A, B, prizes):
        x_a, y_a = a[0], a[1]
        x_b, y_b = b[0], b[1]
        x_p, y_p = p[0]+constant, p[1]+constant
        a = (y_b*x_p - x_b*y_p)//(y_b*x_a - x_b*y_a)
        r = (y_b*x_p - x_b*y_p) % (y_b*x_a - x_b*y_a)
        if not r:
            b = (y_a*x_p - x_a*y_p)//(y_a*x_b - x_a*y_b)
            r = (y_a*x_p - x_a*y_p) % (y_a*x_b - x_a*y_b)
        if not r:
            soln += 3*a+b
    return soln


print(solve(0), solve(10000000000000))
