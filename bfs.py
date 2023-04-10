from common import check_found_goals, check_valid_move, print_path
from maze import Maze
from robot import Robot
from square import Square


def bfs(robot: Robot, maze: Maze, instructions: dict):
	row_size = len(maze.grid)
	col_size = len(maze.grid[0])
	visited = [[False for j in range(col_size)] for i in range(row_size)]
	path = [["$" for j in range(col_size)] for i in range(row_size)]
	start = Square(robot.row, robot.col)
 
	queue = []
	queue.append(start)
	visited[start.row][start.col] = True
	while(queue):
		current_square = queue.pop(0)
		if(check_found_goals(maze.goals, current_square)):
			ans = print_path(current_square, path, instructions, start)
			return ans
		for instruction in instructions:
			next_square = Square(current_square.row + instructions[instruction][0], current_square.col + instructions[instruction][1])
			if(check_valid_move(maze, visited, next_square)):
				queue.append(next_square)
				path[next_square.row][next_square.col] = instruction
				visited[next_square.row][next_square.col] = True
	return "No solution found."