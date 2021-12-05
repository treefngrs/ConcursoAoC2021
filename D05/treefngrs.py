from re import findall
import numpy as np

def iter(xs, star2=False):
	a = np.zeros((1000,1000))
	for x1,y1,x2,y2 in xs:
		if x2<x1:
			x1,y1,x2,y2=x2,y2,x1,y1
		if x1==x2:
			a[x1,min(y1,y2):max(y1,y2)+1]+=1
		elif y1==y2:
			a[x1:x2+1,y1]+=1	
		elif y1<y2 and star2:
			a[range(x1,x2+1), range(y1,y2+1)]+=1
		elif star2:
			a[range(x1,x2+1), range(y1,y2-1,-1)]+=1
	return a[a>1].size

xs = [list(map(int,ls)) for ls in findall(r"(\d+),(\d+) -> (\d+),(\d+)", open("input.txt").read())]
print("Star 1:",iter(xs))
print("Star 2:",iter(xs,True))
