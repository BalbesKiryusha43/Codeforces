t = int(input())
for z in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x, y = [0] * n, [0] * n
    j = 0
    for i in range(n):
        while b[j] < a[i]:
            j += 1
        x[i] = b[j] - a[i]
    j = n - 1
    for i in reversed(range(n)):
        y[i] = b[j] - a[i]
        if b[i - 1] < a[i]:
            j = i - 1
    print(*x)
    print(*y)
