import matplotlib.pyplot as plt

from modules import environment as env
from modules import robot as robo

print ('\nMOTION PLANNING FOR MULTIMODAL OBJECT RETRIEVAL\n')

# ----------------
#  SELECT CHOICES
# ----------------

# Select mode
print ('\nSelect a mode:')
print ('1. Test (test on a benchmark environment)')
print ('2. Play (test on a randomly generated environment)\n')
mode = ''
while True:
	mode = input('Enter your selection: ')
	if mode not in ['1', '2']:
		print ('Incorrect Choice. Please enter from the following options: (1, 2, 3)\n')
	else:
		break

# Select environment		
print ('\nSelect an environment to test:')
print ('1. Small')
print ('2. Medium')
print ('3. Large\n')
environment = ''
while True:
	environment = input('Enter your selection: ')
	if environment not in ['1', '2', '3']:
		print ('Incorrect Choice. Please enter from the following options: (1, 2, 3)\n')
	else:
		break

# Select robot
print ('\nSelect the type of robot:')
print ('1. No sensors')
print ('2. Touch and tell color\n')
robot_type = ''
while True:
	robot_type = input('Enter your selection: ')
	if robot_type not in ['1', '2']:
		print ('Incorrect Choice. Please enter from the following options: (1, 2)\n')
	else:
		break

# Select desired object for touch and tell robot
if robot_type == '2':
	print ('\nSelect the object that you want to be fetched:')
	print ('1. Red Object')
	print ('2. Green Object')
	print ('3. Blue Object')
	print ('4. Circle Object')
	print ('5. Square Object')
	print ('6. Red Circle')
	print ('7. Red Square')
	print ('8. Green Circle')
	print ('9. Green Square')
	print ('10. Blue Circle')
	print ('11. Blue Square\n')
	desired_object = ''
	while True:
		desired_object = input('Enter your selection: ')
		if desired_object not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
			print ('Incorrect Choice. Please enter from the following options: (1, 2, 3)\n')
		else:
			break

# Select robot actions
print ('\nAre diagonal actions allowed for the robot?\n1. Yes\n2. No\n')
action_type = ''
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


# ----------------
#  SETUP AND PLAN
# ----------------

print ('\nDrawing environment...')
dimension = env.draw_env(environment)

print ('\nInitializing obstacles...')
if mode == '1':
	obst_pos = env.draw_obst(environment, test=True)
else:
	obst_pos = env.draw_obst(environment)

print ('\nInitializing objects...')
if mode == '1':
	obj_pos, obj_map = env.draw_objs(environment, obst_pos, test=True)
else:
	obj_pos, obj_map = env.draw_objs(environment, obst_pos)

print ('\nPlanning robot motion...')
if robot_type == '1':
	#robo.get_path_no_sensor(dimension, obst_pos, obj_pos, actions)
	robo.get_path_lidar(dimension, obst_pos, obj_pos, actions)
elif robot_type == '2':
	robo.get_path_touch_tell(dimension, obst_pos, obj_pos, obj_map, desired_object, actions)