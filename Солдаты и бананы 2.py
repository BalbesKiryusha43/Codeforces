import sys

numbers = [int(i)
           for i in sys.stdin.readline().split()]

k = numbers[0]
n = numbers[1]
w = numbers[2]
x = 0                                                    # Полная стоимость

i = 1

while i <= w:
    x += i * k
    i += 1
if n >= x:
    print('0')
else:
    print(x - n)

