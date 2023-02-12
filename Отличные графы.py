for n in range(int(input())):
    n = int(input())
    l = sorted(list(map(int, input().split())))
    f = 0
    k = 0
    for i in range(2, n):
        k += l[i - 2]
        f -= (l[i] * (i - 1))
        f += k
    print(f)
