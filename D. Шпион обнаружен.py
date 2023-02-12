a = int(input())
for a in range(a):
    n = int(input())
    b = dict(sorted(zip([x + 1 for x in range(n)], [int(x) for x in input().split()]), key=lambda item: item[1]))

    if list(b.values())[0] == list(b.values())[1]:
        print(list(b.keys())[-1])
    else:
        print(list(b.keys())[0])


