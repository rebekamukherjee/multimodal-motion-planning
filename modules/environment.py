from random import randint
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def draw_env (environment):
	if environment == 'Small':
		plt.axis([0, 4, 0, 4])
		dimension = 4
	elif environment == 'Medium':
		plt.axis([0, 8, 0, 8])
		dimension = 8
	elif environment == 'Large':
		plt.axis([0, 16, 0, 16])
		dimension = 16
	plt.grid()
	plt.ion()
	plt.show()

	return dimension

def draw_obst (environment):
	if environment == 'Small':
		min_obst = 1
		max_obst = 3
		max_pos = 4
	elif environment == 'Medium':
		min_obst = 4
		max_obst = 10
		max_pos = 8
	elif environment == 'Large':
		min_obst = 10
		max_obst = 30
		max_pos = 16
	obst_pos = []
	num_obst = randint(min_obst, max_obst)
	for obst in range(num_obst):
		x = randint(0, max_pos)
		y = randint(0, max_pos)
		if (x, y) == (0, 0):
			continue
		obst_pos.append((x, y))
		plt.plot(x, y, 'mo')
	plt.draw()
	plt.pause(2)
	return obst_pos

def draw_objs (environment, obst_pos):
	if environment == 'Small':
		min_num = 1
		max_num = 2
		max_pos = 4
	elif environment == 'Medium':
		min_num = 2
		max_num = 4
		max_pos = 8
	elif environment == 'Large':
		min_num = 2
		max_num = 6
		max_pos = 16
	obj_pos = []
	obj_map = {}
	num_r = randint(min_num, max_num)
	for r in range(num_r):
		x = randint(0, max_pos)
		y = randint(0, max_pos)
		if (x, y) in obst_pos or (x, y) in obj_pos:
			continue
		obj_pos.append((x, y))
		obj_map[str((x, y))] = 'red'
		plt.plot(x, y, 'ro')
	num_g = randint(min_num, max_num)
	for g in range(num_g):
		x = randint(0, max_pos)
		y = randint(0, max_pos)
		if (x, y) in obst_pos or (x, y) in obj_pos:
			continue
		obj_pos.append((x, y))
		obj_map[str((x, y))] = 'green'
		plt.plot(x, y, 'go')
	num_b = randint(min_num, max_num)
	for b in range(num_b):
		x = randint(0, max_pos)
		y = randint(0, max_pos)
		if (x, y) in obst_pos or (x, y) in obj_pos:
			continue
		obj_pos.append((x, y))
		obj_map[str((x, y))] = 'blue'
		plt.plot(x, y, 'bo')
	plt.draw()
	plt.pause(2)
	return obj_pos, obj_map