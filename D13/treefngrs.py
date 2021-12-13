from re import findall

file = open("input.txt").read().split("\n\n")
xs = [tuple(map(int,x.split(','))) for x in file[0].splitlines()]
folds = [(x,int(y)) for x,y in findall(r"(\w)=(\d+)",file[1])]

n = 2*next(filter(lambda x: x[0]=='x', folds), None)[1]+1
m = 2*next(filter(lambda x: x[0]=='y', folds), None)[1]+1
grid=[[0]*n for _ in range(m)]

for x,y in xs:
	grid[y][x]=1

s1=True
for a,b in folds:
	if a=='y':
		grid = [[grid[i][j] | grid[m-i-1][j] for j in range(n)] for i in range(b)]
		m = b
	if a=='x':
		grid = [[grid[i][j] | grid[i][n-j-1] for j in range(b)] for i in range(m)]
		n = b
	if s1:
		print("Star 1:", sum(sum(row) for row in grid))
		s1=False

print("Star 2:",*grid,sep='\n')
