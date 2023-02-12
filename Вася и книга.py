import math

t = int(input())
for i in range(t):
    a = 10 ** 90
    b = 10 ** 90
    n, x, y, d = [int(x) for x in input().split()]
    if abs(y - x) % d == 0:
        print(abs(x - y) // d)
    else:
        if (y - 1) % d == 0:
            a = math.ceil((x - 1) / d) + math.ceil((y - 1) // d)
        if (n - y) % d == 0:
            b = math.ceil((n - y) / d) + math.ceil((n - x) / d)
        if a != 10 ** 90 or b != 10 ** 90:
            print(min(a, b))
        else:
            print(-1)
