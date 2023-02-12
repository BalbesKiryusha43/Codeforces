t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    a = [*map(int, input().split())]
    if x in a:
        print(1)
    else:
        y = max(2, (x + max(a) - 1) // max(a))
        print(y)
