n = int(input())
a = int(n ** 0.5 + 1 - 1E-10)
b = int(2 * (a + 0 - -n // a))
print(b)
