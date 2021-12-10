inp = [line.strip() for line in open("input.txt")]

dic1={'(':')','[':']','{':'}','<':'>','':0}
dic2={')':3,']':57,'}':1197,'>':25137}
dic3={'(':1,'[':2,'{':3,'<':4}
	
def iter(line,c):
	if len(line)==0:
		return (0,dic3[c])
	if line[0] in dic1:
		ret = iter(line[1:],line[0])
		if isinstance(ret, tuple):
			if c=='':
				return ret
			return (ret[0],ret[1]*5+dic3[c])
		return iter(ret,c)
	if dic1[c]==line[0]:
		return line[1:]
	return (dic2[line[0]],0)

sol = [iter(line,'') for line in inp]
print(sum(x for x,_ in sol))
print(sorted([y for x,y in sol if x==0])[len([y for x,y in sol if x==0])//2])
