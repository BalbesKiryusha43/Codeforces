for _ in range(int(input())):
    a, b = map(int, input().split())
    x = a - 1
    x = [x, 1, x + 1, 0][x % 4]

    if x == b:
        print(a)

    elif (x ^ a) == b:
        print(a + 2)
    else:
        print(a + 1)
