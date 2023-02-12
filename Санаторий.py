c = list(map(int, input().split()))
k = 0
c.sort()
for i in range(2):
    if (c[2] - 1) > c[i]:
         k += ((c[2] - 1) - c[i])
print(k)