import random
import matplotlib.pyplot as plt

def draw_path(path):
	if len(path) <= 1:
		print ('No path exists.')
		return
	point_1 = path[0]
	for point_2 in path[1:len(path)]:
		x1 = point_1[0]
		x2 = point_2[0]
		y1 = point_1[1]
		y2 = point_2[1]
		# up
		if x2 == x1 and y2 > y1:
			for i in range(0, 50):
				plt.plot(x1, y1 + i/50, 'y.')
		# down
		elif x2 == x1 and y2 < y1:
			for i in range(0, 50):
				plt.plot(x1, y1 - i/50, 'y.')
		# left
		elif x2 < x1 and y2 == y1:
			for i in range(0, 50):
				plt.plot(x1 - i/50, y1, 'y.')
		#right
		elif x2 > x1 and y2 == y1:
			for i in range(0, 50):
				plt.plot(x1 + i/50, y1, 'y.')
		# north east
		elif x2 > x1 and y2 > y1:
			for i in range(0, 50):
				plt.plot(x1 + i/50, y1 + i/50, 'y.')
		# north west
		elif x2 < x1 and y2 > y1:
			for i in range(0, 50):
				plt.plot(x1 - i/50, y1 + i/50, 'y.')
		# south east
		elif x2 > x1 and y2 < y1:
			for i in range(0, 50):
				plt.plot(x1 + i/50, y1 - i/50, 'y.')
		# south west
		elif x2 < x1 and y2 < y1:
			for i in range(0, 50):
				plt.plot(x1 - i/50, y1 - i/50, 'y.')
		point_1 = point_2
		plt.draw()
		plt.pause(0.001)

def euclidean_distance(point1, point2):
	return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5

class Node():
	def __init__(self, parent=None, position=None):
		self.parent = parent
		self.position = position
		self.g = 0
		self.h = 0
		self.f = 0

	def __eq__(self, other):
		return self.position == other.position

def astar(grid, start, end, actions):
	open_list = []
	closed_list = []

	start_node = Node(None, start)
	start_node.g = start_node.h = start_node.f = 0
	open_list.append(start_node)

	end_node = Node(None, end)
	end_node.g = end_node.h = end_node.f = 0

	while len(open_list) > 0:
		current_node = open_list[0]
		current_index = 0
		for index, item in enumerate(open_list):
			if item.f < current_node.f:
				current_node = item
				current_index = index
		open_list.pop(current_index)
		closed_list.append(current_node)
		if current_node == end_node:
			path = []
			current = current_node
			while current is not None:
				path.append(current.position)
				current = current.parent
			return path[::-1]
		children = []
		for a in actions.keys():
			if a == 'u':
				node_position = (current_node.position[0], current_node.position[1] + 1)
			elif a == 'd':
				node_position = (current_node.position[0], current_node.position[1] - 1)
			elif a == 'l':
				node_position = (current_node.position[0] - 1, current_node.position[1])
			elif a == 'r':
				node_position = (current_node.position[0] + 1, current_node.position[1])
			elif a == 'ne':
				node_position = (current_node.position[0] + 1, current_node.position[1] + 1)
			elif a == 'nw':
				node_position = (current_node.position[0] + 1, current_node.position[1] - 1)
			elif a == 'se':
				node_position = (current_node.position[0] - 1, current_node.position[1] + 1)
			elif a == 'sw':
				node_position = (current_node.position[0] - 1, current_node.position[1] - 1)
			if node_position[0] > (len(grid) - 1) or node_position[0] < 0 or node_position[1] > (len(grid[len(grid)-1]) -1) or node_position[1] < 0:
				continue
			if grid[node_position[0]][node_position[1]] != 0:
				continue
			new_node = Node(current_node, node_position)
			children.append(new_node)
		for child in children:
			for closed_child in closed_list:
				if child == closed_child:
					continue
			child.g = current_node.g + 1
			child.h = euclidean_distance(child.position, end_node.position)
			child.f = child.g + child.h
			for open_node in open_list:
				if child == open_node and child.g > open_node.g:
					continue
			open_list.append(child)

def get_path_random(dimension, obst_pos, obj_pos, actions):	
	start = (0,0)
	goal_found = False
	random.shuffle(obj_pos)
	for end in obj_pos:
		grid = []
		for i in range(dimension+1):
			row = []
			for j in range(dimension+1):
				if (i,j) in obst_pos:
					row.append(1)
				elif (i,j) in obj_pos and (i,j) is not start and (i,j) is not end:
					row.append(1)
				else:
					row.append(0)
			grid.append(row)		
		path = astar(grid, start, end, actions)
		draw_path(path)
		user_input = input('Is this the desired object (y)? ')
		if user_input == 'y' or user_input == 'Y':
			goal_found = True
			print ('Found the desired object!')
			break
		else:
			start = end
	if goal_found == False:
		print ('Could not find the desired object!')

def get_path_nearest_neighbor(dimension, obst_pos, obj_pos, actions):	
	start = (0,0)
	visited = [start]
	goal_found = False
	while len(obj_pos) > 0:
		end = obj_pos[0]
		min_dist = dimension ** 2
		for pos in obj_pos:
			dist = euclidean_distance(pos, start)
			if dist < min_dist:
				end = pos
				min_dist = dist
		grid = []
		for i in range(dimension+1):
			row = []
			for j in range(dimension+1):
				if (i,j) in obst_pos:
					row.append(1)
				else:
					row.append(0)
			grid.append(row)		
		path = astar(grid, start, end, actions)
		draw_path(path)
		user_input = input('Is this the desired object (y)?  ')
		if user_input == 'y' or user_input == 'Y':
			goal_found = True
			print ('Found the desired object!')
			break
		start = end
		visited.append(end)
		obj_pos.remove(end)
	if goal_found == False:
		print ('Could not find the desired object!')

def get_path_nonvisual(dimension, obst_pos, obj_pos, obj_map, desired_object, actions, robot_type):
	if desired_object in ['1', '6', '7']:
		desired_color = 'red'
	elif desired_object in ['2', '8', '9']:
		desired_color = 'green'
	elif desired_object in ['3', '10', '11']:
		desired_color = 'blue'
	else:
		desired_color = 'na'
	if desired_object in ['4', '6', '8', '10']:
		desired_shape = 'circle'
	elif desired_object in ['5', '7', '9', '11']:
		desired_shape = 'square'
	else:
		desired_shape = 'na'
	start = (0,0)
	visited = [start]
	goal_found = False
	while len(obj_pos) > 0:
		end = obj_pos[0]
		min_dist = dimension ** 2
		for pos in obj_pos:
			dist = euclidean_distance(pos, start)
			if dist < min_dist:
				end = pos
				min_dist = dist
		grid = []
		for i in range(dimension+1):
			row = []
			for j in range(dimension+1):
				if (i,j) in obst_pos:
					row.append(1)
				else:
					row.append(0)
			grid.append(row)		
		path = astar(grid, start, end, actions)
		draw_path(path)
		if robot_type == '3': # touch and tell shape
			object_shape = obj_map[str(end)][1]
			if object_shape == desired_shape or desired_shape == 'na':
				user_input = input('Is this the desired object (y)? ')
				if user_input == 'y' or user_input == 'Y':
					goal_found = True
					print ('Found the desired object!')
					break
		elif robot_type == '4': # touch and tell object
			object_color = obj_map[str(end)][0]
			object_shape = obj_map[str(end)][1]
			if  (((desired_object in ['1', '2', '3']) and (object_color == desired_color)) or 
				((desired_object in ['4', '5']) and (object_shape == desired_shape)) or 
				((desired_object in ['6', '7', '8', '9', '10', '11']) and (object_color == desired_color) and (object_shape == desired_shape))):
				user_input = input('Is this the desired object (y)? ')
				if user_input == 'y' or user_input == 'Y':
					goal_found = True
					print ('Found the desired object!')
					break
		start = end
		visited.append(end)
		obj_pos.remove(end)
	if goal_found == False:
		print ('Could not find the desired object!')

def vision_sensor(dimension, start, end, obj_map):
	distance = ((end[0] - start[0]) ** 2) + ((end[1] - start[1]) ** 2)
	if dimension == 4:
		percentage = distance * 50 / 32
	elif dimension == 8:
		percentage = distance * 50 / 128
	elif dimension == 16:
		percentage = distance * 10 / 512
	if obj_map[str(end)][0] == 'red':
		return [(100-percentage), (percentage/2), (percentage/2)]
	elif obj_map[str(end)][0] == 'green':
		return [(percentage/2), (100-percentage), (percentage/2)]
	elif obj_map[str(end)][0] == 'blue':
		return [(percentage/2), (percentage/2), (100-percentage)]

def get_path_visual(dimension, obst_pos, obj_pos, obj_map, desired_object, actions):
	if desired_object in ['1', '6', '7']:
		desired_color = 'red'
	elif desired_object in ['2', '8', '9']:
		desired_color = 'green'
	elif desired_object in ['3', '10', '11']:
		desired_color = 'blue'
	else:
		desired_color = 'na'
	start = (0,0)
	visited = [start]
	goal_found = False	
	while len(obj_pos) > 0:
		color_map = []
		for obj in obj_pos:
			if desired_color == 'red':
				color_map.append(vision_sensor(dimension, start, obj, obj_map)[0])
				max_index = color_map.index(max(color_map))
				end = obj_pos[max_index]
			elif desired_color == 'green':
				color_map.append(vision_sensor(dimension, start, obj, obj_map)[1])
				max_index = color_map.index(max(color_map))
				end = obj_pos[max_index]
			elif desired_color == 'blue':
				color_map.append(vision_sensor(dimension, start, obj, obj_map)[2])
				max_index = color_map.index(max(color_map))
				end = obj_pos[max_index]
			else:
				end = obj_pos[0]
				min_dist = dimension ** 2
				for pos in obj_pos:
					dist = euclidean_distance(pos, start)
					if dist < min_dist:
						end = pos
						min_dist = dist		
		grid = []
		for i in range(dimension+1):
			row = []
			for j in range(dimension+1):
				if (i,j) in obst_pos:
					row.append(1)
				else:
					row.append(0)
			grid.append(row)
		path = astar(grid, start, end, actions)
		draw_path(path)
		user_input = input('Is this the desired object (y)? ')
		if user_input == 'y' or user_input == 'Y':
			goal_found = True
			print ('Found the desired object!')
			break
		start = end
		visited.append(end)
		obj_pos.remove(end)
	if goal_found == False:
		print ('Could not find the desired object!')

def get_path_visual_nonvisual(dimension, obst_pos, obj_pos, obj_map, desired_object, actions, robot_type):
	if desired_object in ['1', '6', '7']:
		desired_color = 'red'
	elif desired_object in ['2', '8', '9']:
		desired_color = 'green'
	elif desired_object in ['3', '10', '11']:
		desired_color = 'blue'
	else:
		desired_color = 'na'
	if desired_object in ['4', '6', '8', '10']:
		desired_shape = 'circle'
	elif desired_object in ['5', '7', '9', '11']:
		desired_shape = 'square'
	else:
		desired_shape = 'na'
	start = (0,0)
	visited = [start]
	goal_found = False
	while len(obj_pos) > 0:
		color_map = []
		for obj in obj_pos:
			if desired_color == 'red':
				color_map.append(vision_sensor(dimension, start, obj, obj_map)[0])
				max_index = color_map.index(max(color_map))
				end = obj_pos[max_index]
			elif desired_color == 'green':
				color_map.append(vision_sensor(dimension, start, obj, obj_map)[1])
				max_index = color_map.index(max(color_map))
				end = obj_pos[max_index]
			elif desired_color == 'blue':
				color_map.append(vision_sensor(dimension, start, obj, obj_map)[2])
				max_index = color_map.index(max(color_map))
				end = obj_pos[max_index]
			else:
				end = obj_pos[0]
				min_dist = dimension ** 2
				for pos in obj_pos:
					dist = euclidean_distance(pos, start)
					if dist < min_dist:
						end = pos
						min_dist = dist		
		grid = []
		for i in range(dimension+1):
			row = []
			for j in range(dimension+1):
				if (i,j) in obst_pos:
					row.append(1)
				else:
					row.append(0)
			grid.append(row)
		path = astar(grid, start, end, actions)
		draw_path(path)
		if robot_type == '6': # touch and tell shape
			object_shape = obj_map[str(end)][1]
			if object_shape == desired_shape or desired_shape == 'na':
				user_input = input('Is this the desired object (y)? ')
				if user_input == 'y' or user_input == 'Y':
					goal_found = True
					print ('Found the desired object!')
					break
		elif robot_type == '7': # touch and tell object
			object_color = obj_map[str(end)][0]
			object_shape = obj_map[str(end)][1]
			if  (((desired_object in ['1', '2', '3']) and (object_color == desired_color)) or 
				((desired_object in ['4', '5']) and (object_shape == desired_shape)) or 
				((desired_object in ['6', '7', '8', '9', '10', '11']) and (object_color == desired_color) and (object_shape == desired_shape))):
				user_input = input('Is this the desired object (y)? ')
				if user_input == 'y' or user_input == 'Y':
					goal_found = True
					print ('Found the desired object!')
					break
		start = end
		visited.append(end)
		obj_pos.remove(end)
	if goal_found == False:
		print ('Could not find the desired object!')