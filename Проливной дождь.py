from math import pi

d, h, u, e = map(int, input().split(' '))
u = 4 * u / (pi * d * d)
if e >= u:
    print('NO')
else:
    print('YES')
    print(h / (u - e))
