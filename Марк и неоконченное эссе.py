t = int(input())

for _ in range(t):
    n, c, q = map(int, input().split())
    s = input().strip()

    d = []
    f = [n]

    for i in range(c):
        l, r = map(int, input().split())
        d.append(l)
        f.append(f[-1] + r - l + 1)

    for i in range(q):
        k = int(input())

        for j in range(c):
            g = f[-j - 2]

            if k > g:
                k = (k - g) + d[-j - 1] - 1
        z = s[k - 1]
        print(z)
