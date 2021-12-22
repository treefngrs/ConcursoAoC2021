from functools import cache

x,y = (int(line.split(": ")[1]) for line in open("input.txt"))

def gen(x, y):
	i=1
	px,py=0,0
	while True:
		a = (i-1)%100+i%100+(i+1)%100+3
		b = (i+2)%100+(i+3)%100+(i+4)%100+3
		x,y = (x+a-1)%10+1, (y+b-1)%10+1
		px+=x
		i+=3
		if px<1000:
			py+=y
			i+=3
		yield i-1,px,py

@cache
def roll(x,y,px,py):
	if px>=21:
		return 1,0
	if py>=21:
		return 0,1

	u1,u2=0,0
	for d,c in ((3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1)):
		x2=(x+d-1)%10+1
		px2=px+x2
		v1,v2=roll(y,x2,py,px2)
		u1,u2=u1+c*v2,u2+c*v1
	return u1,u2

s1 = next(filter(lambda x:x[1]>=1000 or x[2]>=1000, gen(x,y)), None)
print("Star 1:", s1[0]*min(s1[1:]))
print("Star 2:", max(roll(x,y,0,0)))
