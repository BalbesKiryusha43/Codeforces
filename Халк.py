a = 'I hate it '
b = 'I love it '
c = int(input())
if c == '1':
    print(a)
elif c % 2 == 1:
    print(((a + b) * (c // 2)).replace('it', 'that') + (a))
else:
    print(((a + b) * (c // 2)).replace('it', 'that')[:-5] + 'it')
