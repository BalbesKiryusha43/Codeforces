n, h = map(int, input().split())
for i in range(1, n):
    a= (h * (i / n) ** .5)
    print(a)
