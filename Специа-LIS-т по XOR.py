t = int(input())
for _ in range(t):
    n,b,p=int(input()),1,0
    for i in map(int,input().split()):
        if not i>p:
            b=0
        p=i
    print('YES' if n%2==0 or not b else 'NO')
