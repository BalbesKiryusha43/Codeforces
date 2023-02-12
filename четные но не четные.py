for i in range(int(input())):
    input();odd=[x for x in input() if int(x)%2]
    if len(odd)<2:print(-1)
    else:print('%c%c'%(odd[0],odd[1]))

