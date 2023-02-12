t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [[*map(int, input().split())] for _ in range(n)]

    u = [0] * (n + m - 1)
    v = [0] * (n + m - 1)
    for i in range(n):
        for j in range(m):
            u[i + j] += a[i][j]
            v[i - j] += a[i][j]
    for i in range(n):
        for j in range(m):
            a[i][j] = u[i + j] + v[i - j] - a[i][j]
    print(max(map(max, a)))
