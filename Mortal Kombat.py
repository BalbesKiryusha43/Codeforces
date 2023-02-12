for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    x = [0] * n
    x[0] = a[0]
    y = 0
    for i in range(1, n):
        if a[i] and y == 2:
            y = 0
            x[i] = x[i - 1] + 1
        elif a[i]:
            y += 1
            x[i] = x[i - 1]
        else:
            y = 0
            x[i] = x[i - 1]
    print(x[-1])
