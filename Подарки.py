import sys

x = int(sys.stdin.readline().split()[0])

friends_to = []

for line in sys.stdin:
    for word in line.split():
        friends_to.append(int(word))

friends_from = [0 for y in range(x)]

a = 0

while a < x:
    friends_from[friends_to[a] - 1] = a + 1
    a += 1

print(*friends_from)
