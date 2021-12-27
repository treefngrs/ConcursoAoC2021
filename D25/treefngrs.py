cum = [list(line) for line in open("input.txt").read().splitlines()]
n,m=len(cum),len(cum[0])
moved,step=True,0

while moved:
	moved=0
	for i in range(n):
		rm = [*range(m)]
		first=True
		for j in rm:
			if cum[i][j]=='>' and cum[i][(j+1)%m]=='.' and (first or j!=m-1):
				if j==0:
					first=False
				cum[i][j]='.'
				cum[i][(j+1)%m]='>'
				if j+1<m:
					rm.remove(j+1)
				moved+=1
	for j in range(m):
		rn = [*range(n)]
		first=True
		for i in rn:
			if cum[i][j]=='v' and cum[(i+1)%n][j]=='.' and (first or i!=n-1):
				if i==0:
					first=False
				cum[i][j]='.'
				cum[(i+1)%n][j]='v'
				if i+1<n:
					rn.remove(i+1)
				moved+=1
	step+=1

print("Star 1:", step)
