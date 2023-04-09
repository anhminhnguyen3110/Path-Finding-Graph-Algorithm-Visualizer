from common import check_found_goals, check_valid_move, print_path
from maze import Maze
from robot import Robot


def bfs(robot: Robot, maze: Maze, instructions: dict):
	rows = len(maze.grid)
	cols = len(maze.grid[0])
	visited = [[False for j in range(cols)] for i in range(rows)]
	path = [["$" for j in range(cols)] for i in range(rows)]
	queue = []
	queue.append((robot.row, robot.col))
	visited[robot.row][robot.col] = True
	while(queue):
		row, col = queue.pop(0)
		if(check_found_goals(maze.goals, row, col)):
			ans = print_path(row, col, path, instructions, (robot.row, robot.col))
			return ans
		for instruction in instructions:
			new_row = row + instructions[instruction][0]
			new_col = col + instructions[instruction][1]
			if(check_valid_move(maze, visited, new_row, new_col)):
				queue.append((new_row, new_col))
				path[new_row][new_col] = instruction
				visited[new_row][new_col] = True
	return "No solution found."
