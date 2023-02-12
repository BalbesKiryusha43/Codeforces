t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    l=len(set(a))
    l=n-l
    if l%2!=0:
        l+=1
    print(n-l)