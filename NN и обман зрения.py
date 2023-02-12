from math import pi, sin

a, b = map(int, input().split())
c = (b / (1 / sin(pi / a) - 1))
print(c)
