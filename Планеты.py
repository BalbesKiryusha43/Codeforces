t = int(input())
for g in range(t):
    n, c = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    x = [0] * 101
    for i in a:
        x[i] += 1
    l = 0
    for s in x:
        if s > c:
            l += c
        else:
            l += s
    print(l)
