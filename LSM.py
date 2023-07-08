import numpy as np
import matplotlib.pyplot as plt
import random
import math

def lsqm(x, y):
	if(np.size(x) != np.size(y)):
		raise ValueError('x and y of different size')
	x2 = np.array([n**2 for n in x])
	y2 = np.array([n**2 for n in y])
	xy = np.array([x[i] * y[i] for i in range(np.size(x))])
	xavg = np.average(x)
	yavg = np.average(y)
	x2avg = np.average(x2)
	y2avg = np.average(y2)
	xyavg = np.average(xy)
	k = (xyavg - xavg * yavg) / (x2avg - xavg ** 2)
	b = yavg - k * xavg
	Sk = math.sqrt(((y2avg - yavg ** 2) / (x2avg - xavg**2) - k**2) / np.size(x))
	Sb = Sk * math.sqrt(x2avg - xavg**2)
	return [k, b, Sk, Sb]

# k0 = 1
# b0 = 1.5

# x = np.arange(1, 50)
# y = np.array([k0 * n + b0 + (random.random() - 0.5) * 3 for n in x])

# ytheor = np.array([k0 * n + b0 for n in x])

# coeffs = lsqm(x, y)
# print(coeffs)
# ypred = np.array([(coeffs[0]) * n + (coeffs[1]) for n in x])

# fig, ax = plt.subplots()
# ax.plot(x, ytheor, color = 'green')
# ax.plot(x, ypred, color = 'red')
# ax.errorbar(x, y, 0.5, 0.3, fmt = '.')
# plt.show()