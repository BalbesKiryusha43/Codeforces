n = int(input())
for t in range(n):
    s=input()
    s+='R'
    c=1
    a=0
    for i in s:
        if i=='R':
            a=max(a,c)
            c=1
        else:
            c+=1
    print(a)