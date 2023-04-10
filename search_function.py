from astar import astar
from bfs import bfs
from bidirection import bidirection
from bidirection_astar import bidirection_astar
from dfs import dfs
from gbfs import gbfs
from maze import Maze
from robot import Robot

def execute_search(robot: Robot, maze: Maze, type_of_function: str):
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
	instructions_bidirection = { "down" : (-1, 0), "right" : (0, -1), "up" : (1, 0), "left" : (0, 1) }
	match type_of_function:
		case 'dfs':
			return dfs(robot, maze, instructions_dfs)
		case 'bfs':
			return bfs(robot, maze, instructions_bfs)
		case 'gbfs':
			return gbfs(robot, maze, instructions_gbfs)
		case 'astar':
			return astar(robot, maze, instructions_astar)
		case 'as':
			return astar(robot, maze, instructions_astar)
		case 'a*':
			return astar(robot, maze, instructions_astar)
		case 'cus1':
			return bidirection(robot, maze, instructions_bfs, instructions_bidirection)
		case 'cus2':
			return bidirection_astar(robot, maze, instructions_astar, instructions_bidirection)
		case default:
			return bfs(robot, maze, instructions_bfs)