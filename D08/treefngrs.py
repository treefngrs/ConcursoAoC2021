xs = [[y.split() for y in x.split(' | ')] for x in open("input.txt").readlines()]
dic1 = {42:0,17:1,34:2,39:3,30:4,37:5,41:6,25:7,49:8,45:9}

s=0
for x in xs:
	dic2 = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0}
	for cad in x[0]:
		for c in cad:
			dic2[c]+=1
	s+=sum((10**(3-i))*(dic1[sum(dic2[c] for c in x[1][i])]) for i in range(4))

print("Star 1:",sum([sum([list(map(len,x[1])).count(i) for i in [2,3,4,7]]) for x in xs]))
print("Star 2:",s)
