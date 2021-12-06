xs = [int(x) for x in open("input.txt").read().split(',')]

def iter(n):
	ls = [xs.count(i) for i in range(10)]
	for _ in range(n):
		ls[9]=ls[0]
		ls[7]+=ls[0]
		for i in range(9):
			ls[i] = ls[i+1]
	return sum(ls[:-1])

print("Star 1:",iter(80))
print("Star 2:",iter(256))
