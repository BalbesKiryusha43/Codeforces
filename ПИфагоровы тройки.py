import math

for i in range(int(input())):
    n = int(input())
    x = (int(math.sqrt(2 * n - 1)) + 1) // 2 - 1
    print(x)
