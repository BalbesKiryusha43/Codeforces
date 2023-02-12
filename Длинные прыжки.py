t = int(input())
for x in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n - 1, -1, -1):
        if (i + a[i] < n):
            a[i] += a[i + a[i]]
    print(max(a))
