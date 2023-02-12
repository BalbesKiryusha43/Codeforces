t = int(input())
for j in range(t):
	n = int(input())
	a = [int(i) for i in input().split()]
	e = 0
	o = 0
	for i in a:
		if i % 2 == 0:
			e += 1
		else:
			o += 1
	if e % 2 == 0 and o % 2 == 0:
		print("YES")
	else:
		works = False
		for i in a:
			if i + 1 in a:
				works = True
		if works == True:
			print("YES")
		else:
			print("NO")
