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
 
	for(goal_row, goal_col) in maze.goals:
		if(robot.row == goal_row and robot.col == goal_col):
			return ("", 0)

	while(stack):
		row, col = stack.pop()
		visited[row][col] = True
		if(check_found_goals(maze.goals, row, col)):
			ans = print_path(row, col, path, instructions, (robot.row, robot.col))
			return ans
		for instruction in instructions:
			new_row = row + instructions[instruction][0]
			new_col = col + instructions[instruction][1]
			if(check_valid_move(maze, visited, new_row, new_col)):
				stack.append((new_row, new_col))
				path[new_row][new_col] = instruction
	return ("No solution found.", 0)