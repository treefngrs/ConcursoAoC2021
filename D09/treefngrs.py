xs = [[[int(c),True] for c in line.strip()] for line in open("input.txt")]

basins,lens=[],[]
s=0

for i in range(100):
	for j in range(100):
		for x,y in [(i+x2,j+y2) for (x2,y2) in [(1,0),(-1,0),(0,1),(0,-1)]]:
			if x>=0 and x<100 and y>=0 and y<100 and xs[x][y][0]<=xs[i][j][0]:
				xs[i][j][1] = False
				break
		if xs[i][j][1]:
			s+=xs[i][j][0]+1
			basins.append([(i,j)])

for basin in basins:
	for (i,j) in basin:
		for x,y in [(i+x2,j+y2) for (x2,y2) in [(1,0),(-1,0),(0,1),(0,-1)]]:
			if x>=0 and x<100 and y>=0 and y<100 and (x,y) not in basin and xs[x][y][0] != 9:
				basin.append((x,y))
	lens.append(len(basin))

lens = sorted(lens, reverse=True)

print("Star 1:", s)
print("Star 2:", lens[0]*lens[1]*lens[2])
