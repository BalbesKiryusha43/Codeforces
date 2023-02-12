t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split(' ')))
    c=0
    for i in range(m):
        for j in range(i):
            if a[j]<a[i]:
                c+=1
    print(c)