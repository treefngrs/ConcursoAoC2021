from re import findall

instructions = [*reversed([[onoff=="on",*map(int, findall("-?\d+", ins))] for onoff,ins in [line.split() for line in open("input.txt")]])]
cuboids, volume = [], 0

def light(x1, x2, y1, y2, z1, z2):
	ret = 0
	for a1,a2,b1,b2,c1,c2 in cuboids:
		if x1>a1 and x2<a2 and y1>b1 and y2<b2 and z1>c1 and z2<c2:
			return 0
		if x1<=a2 and x2>=a1 and y1<=b2 and y2>=b1 and z1<=c2 and z2>=c1:
			if x1 < a1:
				ret += light(x1, a1-1, y1, y2, z1, z2)
			x1 = max(x1,a1)
			if x2 > a2:
				ret += light(a2+1, x2, y1, y2, z1, z2)
			x2 = min(x2,a2)
			if y1 < b1:
				ret += light(x1, x2, y1, b1-1, z1, z2)
			y1 = max(y1,b1)
			if y2 > b2:
				ret += light(x1, x2, b2+1, y2, z1, z2)
			y2 = min(y2,b2)
			if z1 < c1:
				ret += light(x1, x2, y1, y2, z1, c1-1)
			if z2 > c2:
				ret += light(x1, x2, y1, y2, c2+1, z2)
			return ret     

	return (x2-x1+1)*(y2-y1+1)*(z2-z1+1)

for on,*bounds in instructions:
	if any(abs(x)>50 for x in bounds):
		continue
	if on:
		volume += light(*bounds)
	cuboids.append(bounds)
print("Star 1:", volume)

cuboids, volume = [], 0
for on,*bounds in instructions:
	if on:
		volume += light(*bounds)
	cuboids.append(bounds)
print("Star 2:", volume)
