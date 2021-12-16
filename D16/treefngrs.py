code = bin(int(open("input.txt").read(), 16))[2:]
if len(code)%4:
	code='0'*(4-len(code)%4)+code

ops={0 : (int.__add__,0), 1 : (int.__mul__,1), 2 : (min,-1), 3 : (max,-1), 5 : (int.__gt__,-1), 6  : (int.__lt__,-1), 7 : (int.__eq__,-1)}

def literal(bits,n):
	if bits[0]=='1':
		lit,l = literal(bits[5:], n+5)
		return (bits[1:5]+lit, l)
	return (bits[1:5], n+5)

def packet(bits):
	v,pid,l = int(bits[:3],2), int(bits[3:6], 2), 0
	if pid==4:
		lit,l=literal(bits[6:], 0)
		return (v, int(lit,2), l+6)
	elif bits[6]=='0':
		op,acc=ops[pid]
		subs=int(bits[7:22],2)
		while l<subs:
			v2,x,l2=packet(bits[22+l:])
			v,l = v+v2, l+l2
			if acc==-1:
				acc=x
			else:
				acc=(op(acc,x))
		return (v,acc,l+22)
	else:
		subs=int(bits[7:18],2)
		op,acc=ops[pid]
		for _ in range(subs):
			v2,x,l2=packet(bits[18+l:])
			v,l = v+v2, l+l2
			if acc==-1:
				acc=x
			else:
				acc=(op(acc,x))
		return (v,acc,l+18)

s1,s2,_=packet(code)
print("Star 1:",s1)
print("Star 2:",s2)
