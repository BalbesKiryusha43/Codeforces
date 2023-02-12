num = int(input())
nlist = []
mlist = []
t = True
for i in range(num):
    list1 = list(map(int, input().split()))
    k = list1[0]
    n = 0
    while t == True:
        n = n + 1
        if (k % list1[n]) == 0:
            o = 0
            mlist.append(o)
        elif (k - list1[n]) > 0:
            i = 1
            r = k // list1[n]
            i = list1[n] * (r + 1)
            h = k - i
            o = h
            o = int(o)
            o = abs(o)
            mlist.append(o)
        if (k - list1[n]) < 0:
            o = k - list1[n]
            o = abs(o)
            mlist.append(o)
        if n == 3:
            break
    m = min(mlist)
    nlist.append(m)
    mlist = []
print(*nlist, sep='\n')
