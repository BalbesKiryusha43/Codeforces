x = int(input())

for _ in range(x):
    n = int(input())

    y = 0
    for i in range(n - 3):
        print(i, end=" ")
        y ^= i

    num1 = 1 << 30
    if n >= 1:
        print(num1, end=" ")
    num2 = 1 << 29
    if n >= 2:
        print(num2, end=" ")
    y ^= num1
    y ^= num2
    if n >= 3:
        print(y, end=" ")
    print()
