from re import findall 
from functools import cache

a1,a2,a3,a4,a5,a6,a7,a8 = findall(r"\w", open("input.txt").read())
cost = {'A':1, 'B':10, 'C':100, 'D':1000}
rs = {'A':2,'B':4,'C':6,'D':8}

def solve(s2=False):
	if not s2:
		rooms = a1,a5,'A',a2,a6,'B',a3,a7,'C',a4,a8,'D'
	else:
		rooms = a1,'D','D',a5,'A',a2,'C','B',a6,'B',a3,'B','A',a7,'C',a4,'A','C',a8,'D'

	dep = (3,5)[s2]
	hall = ('.',)*11 

	@cache
	def cangoout(hall, i, j): 
		return all(hall[k]=='.' for k in range(j,i,(-1,1)[j<i]))

	def candidates(rooms):
		for c,i,j in [('A',0,dep-1),('B',dep,dep*2-1),('C',dep*2,dep*3-1),('D',dep*3,dep*4-1)]:
			for k in range(i,j):
				if rooms[k] != '.':
					if not cangoin(rooms, c):
						yield (rs[c],k)
					break
	@cache
	def cangoin(rooms, amp):
		return all(k==amp or k=='.' for k in rooms[dep*rs[amp]//2-dep:dep*rs[amp]//2])

	@cache
	def search(rooms, hall):
		if (s2 and rooms == ('A','A','A','A','A','B','B','B','B','B','C','C','C','C','C','D','D','D','D','D')) or rooms == ('A','A','A','B','B','B','C','C','C','D','D','D'): 
			return 0
		for i in range(11):
			amp = hall[i]
			if amp == '.': 
				continue
			j = rs[amp]
			if j and cangoout(hall, i, j) and cangoin(rooms, amp):
				idx = dep*rs[amp]//2-dep + rooms[dep*rs[amp]//2-dep:dep*rs[amp]//2].index(amp)-1
				return cost[amp]*(abs(j-i)+(idx%dep)+1) + search(rooms[:idx]+tuple(hall[i])+rooms[idx+1:], hall[:i]+tuple('.')+hall[i+1:])
		ans = float("inf")
		moves = 0
		for c,i in candidates(rooms):
			for j in range(len(hall)):
				if (not j%2 and 2<=j<=8) or hall[j] != '.' or not cangoout(hall, c, j): 
					continue
				moves += 1
				ans = min(ans, cost[rooms[i]]*(i%dep+1+abs(c-j)) + search(rooms[:i]+tuple('.')+rooms[i+1:], hall[:j]+tuple(rooms[i])+hall[j+1:]))
		return ans
	return search(rooms,hall)

print("Star 1:", solve(s2=False))
print("Star 2:", solve(s2=True))
