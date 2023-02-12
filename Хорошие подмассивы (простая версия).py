for t in range(int(input())):
    n = int(input())
    z = list(map(int, input().split()))
    x = 0
    y = 0
    for i, v in enumerate(z):
        if i + 1 > v:
            y = max(y, i + 1 - v)
        x += i + 1 - y
    print(x)

