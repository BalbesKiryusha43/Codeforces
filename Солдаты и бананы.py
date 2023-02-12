k, n, w = map(int, input().split())
x = 0
i = 1
while i <= w:
    x += i * k
    i += 1
if n >= x:
    print('0')
else:
    print(x - n)
