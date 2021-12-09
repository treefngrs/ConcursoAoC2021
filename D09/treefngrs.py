xs = [[int(c) for c in line.strip()] for line in open("input.txt")]
n,m = len(xs),len(xs[0])

def adj(i,j):
	return [(i+x2,j+y2) for (x2,y2) in [(1,0),(-1,0),(0,1),(0,-1)]]

def checkadj(num,x,y):
	return not 0<=x<n or not 0<=y<m or xs[x][y]>num

def checkbas(x,y,ls):
	return 0<=x<n and 0<=y<m and xs[x][y]!=9 and (x,y) not in ls

basins=[[(i,j)] for i in range(n) for j in range(m) if all([checkadj(xs[i][j],x,y) for x,y in adj(i,j)])]
for basin in basins:
	for (i,j) in basin:
		basin.extend([(x,y) for x,y in adj(i,j) if checkbas(x,y,basin)])
lens = sorted(list(map(len,basins)), reverse=True)

print("Star 1:", sum([1+xs[i][j] for i,j in x][0] for x in basins))
print("Star 2:", lens[0]*lens[1]*lens[2])
