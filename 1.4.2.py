import numpy as np
import random

def randprod(n):
	R = 1
	for i in range(n):
		R = R * random.randint(0, 12)
	return R

def randarray(Len, n):
	ret = []
	for i in range(Len):
		ret.append(randprod(n))
	return ret

print(randarray(60, 4))