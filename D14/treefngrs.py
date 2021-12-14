from re import findall
from collections import defaultdict

temp,rules = open("input.txt").read().split('\n\n')
start,temp = temp[0],{p : temp.count(p) for p in [temp[i:i+2] for i in range(len(temp)-1)]}
rules = {a : (a[0]+b,b+a[1]) for a,b in findall(r"(\w+) -> (\w)", rules)}

def star(n,temp,rules):
	for _ in range(n):
		next=defaultdict(lambda: 0)
		for p in temp:
			for p2 in rules[p]:
				next[p2]+=temp[p]			
		temp=next

	count=defaultdict(lambda: 0)
	for p in next:
		count[p[1]]+=next[p]
	count[start]+=1
	return max(count.values())-min(count.values())

print("Star 1:", star(10,temp,rules))
print("Star 2:", star(40,temp,rules))
