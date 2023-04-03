from common import check_found_goals, check_valid_move, print_path
from maze import Maze
from robot import Robot


def dfs(robot: Robot, maze: Maze, instructions: dict):
	rows = len(maze.grid)
	cols = len(maze.grid[0])
	visited = [[False for j in range(cols)] for i in range(rows)]
	path = [["$" for j in range(cols)] for i in range(rows)]
	stack = []
	stack.append((robot.row, robot.col))
	while(stack):
		row, col = stack.pop()
		visited[row][col] = True
		if(check_found_goals(maze.goals, row, col)):
			ans = print_path(row, col, path, instructions, robot)
			return ans
		for instruction in instructions:
			add_row = instructions[instruction][0]
			add_col = instructions[instruction][1]
			if(check_valid_move(maze, visited, row + add_row, col + add_col)):
				stack.append((row + add_row, col + add_col))
				path[row+add_row][col+add_col] = instruction
	return path