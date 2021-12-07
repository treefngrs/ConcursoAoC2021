xs = sorted([int(x) for x in open("input.txt").read().split(',')])

def f(x,m):
	return abs(x-m)

def f2(x,m):
	return (abs(x-m)*(abs(x-m)+1))//2

print("Star 1:",sum(f(x,xs[len(xs)//2]) for x in xs))
print("Star 2:",min(sum(f2(x,m) for x in xs) for m in range(xs[0],xs[-1]+1)))
