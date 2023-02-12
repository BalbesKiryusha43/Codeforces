for i in range(int(input())):
    p, h = sorted(input()), input()
    f = 1
    for j in range(len(h) - len(p) + 1):
        if p == sorted(h[j:j + len(p)]):
            f = 0
            break
    print('YNEOS'[f::2])
