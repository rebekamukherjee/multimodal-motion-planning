import matplotlib.pyplot as plt

from modules import environment as env
from modules import robot as robo

print ('\nMOTION PLANNING FOR MULTIMODAL OBJECT RETRIEVAL\n')

# Select environment
print ('\nSelect an environment to test:\n1. Small\n2. Medium\n3. Large\n')
while True:
	env_type = input('Enter your selection: ')
	if env_type not in ['1', '2', '3']:
		print ('Incorrect Choice. Please enter from the following options: (1, 2, 3)\n')
	else:
		break
if env_type == '1':
	environment = 'Small'
elif env_type == '2':
	environment = 'Medium'
elif env_type == '3':
	environment = 'Large'

# Select robot
print ('\nSelect the type of robot:\n1. No sensors\n2. Touch and tell sensors\n')
while True:
	robot_type = input('Enter your selection: ')
	if robot_type not in ['1', '2']:
		print ('Incorrect Choice. Please enter from the following options: (1, 2)\n')
	else:
		break
if robot_type == '1':
	robot = 'No sensors'
elif robot_type == '2':
	robot = 'Touch and tell sensors'

# Select desired object for touch and tell robot
if robot_type == '2':
	print ('\nSelect the object that you want to be fetched:\n1. Red\n2. Green\n3. Blue\n')
	while True:
		obj_type = input('Enter your selection: ')
		if obj_type not in ['1', '2', '3']:
			print ('Incorrect Choice. Please enter from the following options: (1, 2, 3)\n')
		else:
			break
	if obj_type == '1':
		dobject = 'red'
	elif obj_type == '2':
		dobject = 'green'
	elif obj_type == '3':
		dobject = 'blue'

# Select robot actions
print ('\nAre diagonal actions allowed for the robot?\n1. Yes\n2. No\n')
while True:
	action_type = input('Enter your selection: ')
	if action_type not in ['1', '2']:
		print ('Incorrect Choice. Please enter from the following options: (1, 2, 3)\n')
	else:
		break
if action_type == '1':
	actions = {'u': 1, 'd': 1, 'l': 1, 'r': 1, 'ne': 1.5, 'nw': 1.5, 'se': 1.5, 'sw': 1.5}
elif action_type == '2':
	actions = {'u': 1, 'd': 1, 'l': 1, 'r': 1}

print ('\nDrawing environment...')
dimension = env.draw_env(environment)

print ('\nInitializing obstacles...')
obst_pos = env.draw_obst(environment)

print ('\nInitializing objects...')
obj_pos, obj_map = env.draw_objs(environment, obst_pos)

print ('\nPlanning robot motion...')
if robot_type == '1':
	#robo.get_path_no_sensor(dimension, obst_pos, obj_pos, actions)
	robo.get_path_no_sensor_closest_goal(dimension, obst_pos, obj_pos, actions)
elif robot_type == '2':
	robo.get_path_touch_tell(dimension, obst_pos, obj_pos, obj_map, dobject, actions)