xs = [eval(line) for line in open("input.txt")]

def seek(x, n, pos):
	if isinstance(x, int):
		return x+n
	l,r=x
	if pos==0:
		return [seek(l,n, pos), r]
	else:
		return [l, seek(r,n,pos)]

def explode(x, dep):
	if isinstance(x, list):
		l,r = x
		if dep==4:
			return 0,l,r,True
		l,l2,r2,found = explode(l,dep+1)
		if found:
			return [l, seek(r,r2,0)],l2,0,True
		r,l2,r2,found = explode(r,dep+1)
		if found:
			return [seek(l,l2,1), r],0,r2,True
	return x,0,0,False

def split(x):	
	if isinstance(x, list):
		l,r = x
		l,found = split(l)
		if not found:
			r,found = split(r)
		return [l,r],found
	if x>9:
		return [x//2, (x+1)//2], True
	return x, False

def magnitude(x):
	if isinstance(x, int):
		return x
	l,r=x
	return 3*magnitude(l)+2*magnitude(r)

def add(a, b):
	x = [a, b]
	found = True
	while found:
		x, _, _, found = explode(x, 0)
		if not found:
			x, found = split(x)
	return x

acc=xs[0]
for x in xs[1:]:
	acc = add(acc,x)

print("Star 1:", magnitude(acc))
print("Star 2:", max(magnitude(add(a,b)) for a in xs for b in xs if a!=b))
