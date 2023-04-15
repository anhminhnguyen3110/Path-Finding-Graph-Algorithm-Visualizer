from astar import astar
from bfs import bfs
from multidirection_search import multidirection_search
from multidirection_astar import multidirection_astar
from dfs import dfs
from gbfs import gbfs
from maze import Maze
from robot import Robot

def execute_search(robot: Robot, maze: Maze, type_of_function: str, draw_package = None):
	# for i in range(len(maze.grid)):
	# 	for j in range(len(maze.grid[0])):
	# 		if(i == robot.row and j == robot.col):
	# 			print("R", end = " ")
	# 		else:
	# 			print(maze.grid[i][j], end = " ")
	# 	print()
	type_of_function = type_of_function.lower()
	instructions_bfs = { "up" : (-1, 0), "left" : (0, -1), "down" : (1, 0), "right" : (0, 1) }
	instructions_dfs = { "right" : (0, 1), "down" : (1, 0), "left" : (0, -1), "up" : (-1, 0) }
	instructions_gbfs = { "up" : (-1, 0), "left" : (0, -1), "down" : (1, 0), "right" : (0, 1) }
	instructions_astar = { "up" : (-1, 0), "left" : (0, -1), "down" : (1, 0), "right" : (0, 1) }
	instructions_multidirection = { "down" : (-1, 0), "right" : (0, -1), "up" : (1, 0), "left" : (0, 1) }
	instructions_multidirection_astar = { "up" : (1, 0), "left" : (0, 1), "down" : (-1, 0), "right" : (0, -1) }
 
	match type_of_function:
		case 'dfs':
			return dfs(robot, maze, instructions_dfs, draw_package)
		case 'bfs':
			return bfs(robot, maze, instructions_bfs, draw_package)
		case 'gbfs':
			return gbfs(robot, maze, instructions_gbfs, draw_package)
		case 'astar':
			return astar(robot, maze, instructions_astar, draw_package)
		case 'as':
			return astar(robot, maze, instructions_astar, draw_package)
		case 'a*':
			return astar(robot, maze, instructions_astar, draw_package)
		case 'cus1':
			return multidirection_search(robot, maze, instructions_bfs, instructions_multidirection, draw_package)
		case 'multidirectional search':
			return multidirection_search(robot, maze, instructions_bfs, instructions_multidirection, draw_package)
		case 'cus2':
			return multidirection_astar(robot, maze, instructions_astar, instructions_multidirection, draw_package)
		case 'multidirectional a*':
			return multidirection_astar(robot, maze, instructions_astar, instructions_multidirection_astar, draw_package)
		case default:
			return bfs(robot, maze, instructions_bfs, draw_package)