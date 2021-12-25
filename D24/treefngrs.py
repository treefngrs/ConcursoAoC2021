#by observing my input, its made of the same instructions repeated 14 times with changing a,b,c int values
#inp w
#mul x 0
#add x z
#mod x 26
#div z a
#add x b
#eql x w
#eql x 0
#mul y 0
#add y 25
#mul y x
#add y 1
#mul z y
#mul y 0
#add y w
#add y c
#mul y x
#add z y
#where a is 1 or 26 and if a==26 -> b<0. x and y reset every iteration. Simplifying, the expression is 
#z = (w+c)*x + z*(25*x+1) / a
#with x=0 when z%26+a == w, else 1
#so z multiplies itself by 26 and gets added to w+c when x==1 (a==1) and gets divided by 26 when x==0 (a==26), where w must be z%26+b

from re import findall
numbers = [(ls[2],ls[3],ls[-1]) for ls in [tuple(map(int, findall(r"-?\d+", block))) for block in open("input.txt").read().split("inp")[1:]]]

def find(n, total, z, s2):
	if n>=14:
		return total

	if numbers[n][0] == 1:
		for w in range((9,1)[s2], (0,10)[s2], (-1,1)[s2]):
			ret = find(n+1, total*10+w, z*26+w+numbers[n][2], s2)
			if ret:
				return ret

	w = z%26+numbers[n][1]
	if 1<=w<=9:
		return find(n+1, total*10+w, z//26, s2)
	return 0

print("Star 1:", find(0, 0, 0, 0))
print("Star 2:", find(0, 0, 0, 1))
