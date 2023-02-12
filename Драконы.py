s, n = (int(i) for i in input().split())
a = []
w = []
z = True

for i in range(n):
    x, y = (int(i) for i in input().split())
    a.append([x, y])

while len(a) > 0:
    k = a[0]
    for dragon in a:
        if dragon[0] < k[0]:
            k = dragon
    w.append(k)
    del a[a.index(k)]

for i in range(n):
    if s > w[i][0]:
        s += w[i][1]
    else:
        z = False
        break

if z:
    print("YES")
else:
    print("NO")
