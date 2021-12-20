import numpy as np
import scipy.signal

alg,img = open("input.txt").read().split("\n\n")
alg = [(0,1)[c=='#'] for c in alg]
img = np.array([[(0,1)[c=='#'] for c in line] for line in img.splitlines()])
conv = np.array([[1,2,4],[8,16,32],[64,128,256]])

def sol(n, img):
	for i in range(n):
		img = np.pad(img, (2,2), 'constant', constant_values=i%2)
		img = scipy.signal.convolve(img, conv, mode='same')

		for x in np.nditer(img, op_flags=['readwrite']):
			x[...]=alg[x]
		img=img[1:-1,1:-1]
		
	return np.sum(img)

print("Star 1:", sol(2, img))
print("Star 2:", sol(50, img))
