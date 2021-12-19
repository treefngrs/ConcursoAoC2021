scanners = [[tuple(map(int, line.split(','))) for line in scanner] for scanner in [scanner.splitlines()[1:] for scanner in open("input.txt").read().split("\n\n")]]

def rotate(v,i,j,k,a,b,c):
	return a*v[i],b*v[j],c*v[k]

def manhattan(a,b,c,d,e,f):
	return abs(a-d)+abs(b-e)+abs(c-f)


orientations = [(0,1,2,1,1,1),  (1,2,0,1,1,1),  (2,0,1,1,1,1),  (2,1,0,-1,1,1),  (1,0,2,-1,1,1),  (0,2,1,-1,1,1),
                (2,1,0,1,-1,1), (1,0,2,1,-1,1), (0,2,1,1,-1,1), (2,1,0,1,1,-1),  (1,0,2,1,1,-1),  (0,2,1,1,1,-1),
                (0,1,2,-1,1,-1),(1,2,0,-1,1,-1),(2,0,1,-1,1,-1),(0,1,2,1,-1,-1), (1,2,0,1,-1,-1), (2,0,1,1,-1,-1),
                (0,1,2,-1,-1,1),(1,2,0,-1,-1,1),(2,0,1,-1,-1,1),(2,1,0,-1,-1,-1),(1,0,2,-1,-1,-1),(0,2,1,-1,-1,-1)]

final = {*scanners[0]}
def search(s):
	for o in orientations:
		s2 = [rotate(v,*o) for v in s]
		for pos in final:
			for pos2 in s2:
				offset = tuple(x-y for x,y in zip(pos,pos2))
				s3 = {tuple(x+y for x,y in zip(pos3,offset)) for pos3 in s2}
				if len(final & s3) >= 12:
					return final|s3,True,offset
	return final,False,None

index = [*range(1,5)]
coords = [(0,0,0)]
for i in index:
	final,found,offset = search(scanners[i])
	if not found:
		index.append(i)
	else:
		coords.append(offset)


print("Star 1", len(final))
print("Star 2:", max(manhattan(*a,*b) for a in coords for b in coords))
