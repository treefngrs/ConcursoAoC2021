from re import findall
from math import sqrt,ceil

x1,x2,y1,y2 = map(int,findall(r"(-?\d+)", open("input.txt").read()))
#find the min x velocity to reach the area
#this is the min n that safisfies:
# n*(n+1)/2>=x1
# n^2+n >= 2x1
# (n+1)^2 >= 2x1-1/4
# n >= sqrt(2x1-1/4)-1/2 
xbound = ceil(sqrt(2*x1-0.25)-0.5)

def xsteps(x):
	p = x-1
	while x<=x2:
		yield x
		x,p = x+(0,p)[p>0],p-1

def ysteps(y):
	p = y-1
	while y>=y1:
		yield y
		y,p = y+p,p-1

def land(pos):
	return x1<=pos[0]<=x2 and y1<=pos[1]<=y2

print("Star 1:", (-y1*(-y1-1))//2) #assuming y1<0 and knowing that the prone falls with the same velocity it goes up
print("Star 2:", sum(any(map(land, zip(xsteps(x), ysteps(y)))) for x in range(xbound, x2+1) for y in range(y1, -y1)))
