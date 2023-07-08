import csv
import numpy as np
import LSM
import matplotlib.pyplot as plt

file = open('data1.csv', newline='')
try:
	reader = csv.reader(file)
	data = np.empty(0)
	for row in reader:
		data = np.append(data, row) # пишем все в пустой массив, получим один массив из всех данных

	data = data.reshape(np.size(data) // 4, 4) # превращаем массив в двумерный для упрощения работы

	x = data[1:, 0].astype('f') # пишем куски массива в x и y и в их погрешности
	dx = data[1:, 1].astype('f')
	y = data[1:, 2].astype('f')
	dy = data[1:, 3].astype('f')

	fig, ax = plt.subplots()

	k, b, dk, db = LSM.lsqm(x, y) # считаем МНК

	linx = np.array([np.min(x), np.max(x)])
	ax.plot(linx, k * linx + b) # строим МНК по 2 точкам
	ax.errorbar(x, y, dy, dx, fmt = '.r') # строим точки в виде '.r', т.е. в виде точек красного цвета
	plt.show()

finally:
	file.close()