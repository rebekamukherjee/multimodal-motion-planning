from random import randint
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def draw_env (environment):
	if environment == '1':
		plt.axis([0, 4, 0, 4])
		dimension = 4
	elif environment == '2':
		plt.axis([0, 8, 0, 8])
		dimension = 8
	elif environment == '3':
		plt.axis([0, 16, 0, 16])
		dimension = 16
	plt.grid()
	plt.ion()
	plt.show()
	plt.pause(2)
	return dimension

def draw_obst (environment, test=False):
	if test:
		if environment == '1':
			obst_pos = [(1, 1), (2, 3)]
		elif environment == '2':
			obst_pos = [(1, 1), (2, 3), (5, 7), (7, 7)]
		elif environment == '3':
			obst_pos = [(1, 1), (2, 3), (5, 7), (7, 7), (8, 6), (10, 5), (12, 13), (15, 14), (15, 3)]
	else:
		if environment == '1':
			min_obst = 1
			max_obst = 4
			max_pos = 4
		elif environment == '2':
			min_obst = 4
			max_obst = 8
			max_pos = 8
		elif environment == '3':
			min_obst = 8
			max_obst = 12
			max_pos = 16
		num_obst = randint(min_obst, max_obst)
		obst_pos = []
		for obst in range(num_obst):
			x = randint(0, max_pos)
			y = randint(0, max_pos)
			if (x, y) == (0, 0) or (x, y) in obst_pos:
				continue
			obst_pos.append((x, y))
	for obst in obst_pos:
		plt.plot(obst[0], obst[1], 'mo')
	plt.draw()
	plt.pause(2)
	return obst_pos

def draw_objs (environment, obst_pos, test=False):
	obj_pos = []
	obj_map = {}
	if test:
		if environment == '1':
			red_circles =[(1, 2)]
			red_squares = [(3, 2)]
			green_circles = [(4, 4)]
			green_squares = [(1, 3)]
			blue_circles = [(2, 4), (3, 3)]
			blue_squares = []
		elif environment == '2':
			red_circles =[(1, 2), (7, 3)]
			red_squares = [(3, 2)]
			green_circles = [(4, 4), (6, 3)]
			green_squares = [(1, 3)]
			blue_circles = [(2, 4), (3, 3), (5, 5)]
			blue_squares = []
		elif environment == '3':
			red_circles =[(1, 2), (7, 3)]
			red_squares = [(3, 2), (15, 9), (12, 4)]
			green_circles = [(4, 4), (6, 3)]
			green_squares = [(1, 3), (3, 15)]
			blue_circles = [(2, 4), (3, 3), (5, 5), (12, 12)]
			blue_squares = []
		obj_pos = red_circles + red_squares + green_circles + green_squares + blue_circles + blue_squares
	else:
		if environment == '1':
			min_num = 1
			max_num = 2
			max_pos = 4
		elif environment == '2':
			min_num = 1
			max_num = 3
			max_pos = 8
		elif environment == '3':
			min_num = 1
			max_num = 4
			max_pos = 16
		red_circles =[]
		num_r_c = randint(min_num, max_num)
		for i in range(num_r_c):
			x = randint(0, max_pos)
			y = randint(0, max_pos)
			if (x, y) in obst_pos or (x, y) in obj_pos:
				continue
			red_circles.append((x, y))
			obj_pos.append((x, y))
		red_squares = []
		num_r_s = randint(min_num, max_num)
		for i in range(num_r_s):
			x = randint(0, max_pos)
			y = randint(0, max_pos)
			if (x, y) in obst_pos or (x, y) in obj_pos:
				continue
			red_squares.append((x, y))
			obj_pos.append((x, y))
		green_circles = []
		num_g_c = randint(min_num, max_num)
		for i in range(num_g_c):
			x = randint(0, max_pos)
			y = randint(0, max_pos)
			if (x, y) in obst_pos or (x, y) in obj_pos:
				continue
			green_circles.append((x, y))
			obj_pos.append((x, y))
		green_squares = []
		num_g_s = randint(min_num, max_num)
		for i in range(num_g_s):
			x = randint(0, max_pos)
			y = randint(0, max_pos)
			if (x, y) in obst_pos or (x, y) in obj_pos:
				continue
			green_squares.append((x, y))
			obj_pos.append((x, y))
		blue_circles = []
		num_b_c = randint(min_num, max_num)
		for i in range(num_b_c):
			x = randint(0, max_pos)
			y = randint(0, max_pos)
			if (x, y) in obst_pos or (x, y) in obj_pos:
				continue
			blue_circles.append((x, y))
			obj_pos.append((x, y))
		blue_squares = []
		num_b_s = randint(min_num, max_num)
		for i in range(num_b_s):
			x = randint(0, max_pos)
			y = randint(0, max_pos)
			if (x, y) in obst_pos or (x, y) in obj_pos:
				continue
			blue_squares.append((x, y))
			obj_pos.append((x, y))
	for obj in red_circles:
		obj_map[str(obj)] = ['red', 'circle']
		plt.plot(obj[0], obj[1], 'ro')
	for obj in red_squares:
		obj_map[str(obj)] = ['red', 'square']
		plt.plot(obj[0], obj[1], 'rs')
	for obj in green_circles:
		obj_map[str(obj)] = ['green', 'circle']
		plt.plot(obj[0], obj[1], 'go')
	for obj in green_squares:
		obj_map[str(obj)] = ['green', 'square']
		plt.plot(obj[0], obj[1], 'gs')
	for obj in blue_circles:
		obj_map[str(obj)] = ['blue', 'circle']
		plt.plot(obj[0], obj[1], 'bo')
	for obj in blue_squares:
		obj_map[str(obj)] = ['blue', 'square']
		plt.plot(obj[0], obj[1], 'bs')
	plt.draw()
	plt.pause(2)
	return obj_pos, obj_map