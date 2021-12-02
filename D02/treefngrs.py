xs = [(cad, int(d)) for cad,d in map(lambda x: x.split(), open("input.txt").readlines())]

hor,dep,dep2=(0,)*3
for cad, d in xs:
	if cad == "down":
		dep+=d
	elif cad == "up":
		dep-=d
	elif cad == "forward":
		hor+=d
		dep2+=dep*d

print("Star 1:", hor*dep)
print("Star 2:", hor*dep2)
