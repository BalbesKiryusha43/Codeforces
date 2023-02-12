E=int(input())
for ii in range(E):
    s=input()
    s1=input()
    x,y,z=len(s),len(s1),0
    for i in range(x):
        for j in range(i,x):
            if s[i:j+1] in s1 and j-i+1>z:
                z=j-i+1
    print(x+y-(2*z))