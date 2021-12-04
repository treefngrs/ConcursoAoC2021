def parse(ls):
	ls = [[[int(x),0] for x in line.split()] for line in ls]
	for i in range(0, len(ls), 5):
		yield ls[i:i+5]

def findx(bingo, elem):
	for i,line in enumerate(bingo):
		if [elem,0] in line:
			return (i, line.index([elem, 0]))
	return 0

def checksum(bingo,i,j):
	return sum(y for x,y in bingo[i])==5 or sum(y for x,y in [row[j] for row in bingo])==5

def sumsol(bingo):
	s=0
	for line in bingo:
		s+=sum(x[0] for x in line if x[1]==0)
	return s

def iter1(bs, xs, n):
	for x in xs:
		for i in range(n):
			found = findx(bs[i],x)
			if found:
				bs[i][found[0]][found[1]][1]=1
				if checksum(bs[i],found[0],found[1]):
					return sumsol(bs[i])*x
	return		

def iter2(bs, xs):
	for x in xs:
		r=0
		for i in range(len(bs)):
			found = findx(bs[i-r],x)
			if found:
				bs[i-r][found[0]][found[1]][1]=1
				if checksum(bs[i-r],found[0],found[1]):
					if len(bs)==1:
						return sumsol(bs[i])*x
					bs.remove(bs[i-r])
					r+=1
	return				

with open("input.txt") as file:
	xs = [int(x) for x in file.readline().strip().split(',')]
	lines = [line for line in (l.strip() for l in file) if line]
	bs = list(parse(lines))
	n = len(bs)

print("Star 1:",iter1(bs,xs,n))
print("Star 2:",iter2(bs,xs))
