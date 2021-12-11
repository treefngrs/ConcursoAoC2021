a = [[int(c) for c in line[:-1]] for line in open("input.txt")]
n,m=len(a),len(a[0])

def adj(i,j):
	return [(i+x2,j+y2) for (x2,y2) in [(i,j) for i in range(-1,2) for j in range(-1,2)] if -1<i+x2<n and -1<j+y2<m]

def flash(i,j):
	if a[i][j] or (i,j) not in visited:
		visited.add((i,j))
		a[i][j] = (a[i][j]+1)%10
		if not a[i][j]:
			return 1+sum(flash(x,y) for x,y in adj(i,j))
	return 0

total,step=0,0
while(1):
	step+=1
	visited=set()
	s=sum(flash(i,j) for i in range(n) for j in range(m))
	if step<=100:
		total+=s
	if s==100:
		print("Star 1:",total)
		print("Star 2:",step)
		break
