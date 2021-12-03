from functools import reduce
xs = [list(map(int,list(cad))) for cad in open("input.txt").read().splitlines()]

bools = [2*x>len(xs) for x in [sum(a) for a in zip(*xs)]]
s1=reduce(lambda a, b: (a<<1) + b, bools)
s2=reduce(lambda a, b: (a<<1) + b,  [not bool for bool in bools])
print("Star 1:",s1*s2)

ys=xs
i=0
while(len(xs)>1):
	s = 2*sum(x[i] for x in xs)>=len(xs)
	xs = list(filter(lambda a:a[i]==s,xs))
	i+=1

i=0
while(len(ys)>1):
	s = 2*sum(y[i] for y in ys)>=len(ys)
	ys = list(filter(lambda a:a[i]!=s,ys))
	i+=1

s1=reduce(lambda a, b: (a<<1) + b, xs[0])
s2=reduce(lambda a, b: (a<<1) + b, ys[0])
print("Star 2:",s1*s2)
