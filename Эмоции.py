n, m, g = map(int, input().split())
a = 0
b = 0
c = list(map(int, input().split()))
for i in range(0, n):
    if c[i] >= a:
        b = a
        a = c[i]
    if c[i] > b and c[i] < a:
        b = c[i]
print(((m // (g + 1)) * b) + (m - (m // (g + 1))) * a)

