l = list(map(int, input().split()))

x = l[0]
y = l[1]
a = l[2]
b = l[3]

if x == a or y == b:
    print("1", end=" ")
else:
    print("2", end=" ")

if (x + y) % 2 != (a + b) % 2:
    print("0", end=" ")
elif abs(x - a) == abs(y - b):
    print("1", end=" ")
else:
    print("2", end=" ")

z = (max(abs(x - a), abs(y - b)))
print(z)
