import heapq

cave = [[int(c) for c in line.strip()] for line in open("input.txt")]
n,m = len(cave),len(cave[0])

def adj(node, t):
	return [(node[0]+x,node[1]+y) for (x,y) in [(1,0),(-1,0),(0,1),(0,-1)] if 0<=node[0]+x<t*n and 0<=node[1]+y<t*m]

def val(x,y):
	val = cave[x%n][y%m]+x//n+y//m
	if val>9:
		return (val%9)
	return val

def sol(t):
	q = []
	heapq.heapify(q)
	node = (0,0)
	dic = {node : 0}

	while node != (t*n-1,t*m-1):
		for x,y in adj(node, t):
			if (x,y) not in dic:
				heapq.heappush(q, (dic[node]+val(x,y), (x,y)))

		while node in dic:
			g,node = heapq.heappop(q)
		dic[node] = g

	return dic[(t*n-1,t*m-1)]

print("Star 1:",sol(1))
print("Star 2:",sol(5))
