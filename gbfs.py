from common import check_found_goals, check_valid_move, find_goal_in_multiple_goals, heuristic, print_path
from maze import Maze
from robot import Robot
from queue import PriorityQueue

def gbfs(robot: Robot, maze: Maze, instructions: dict):
	rows = len(maze.grid)
	cols = len(maze.grid[0])
	goal = find_goal_in_multiple_goals(maze, robot)
	visited = [[False for j in range(cols)] for i in range(rows)]
	path = [["$" for j in range(cols)] for i in range(rows)]
	queue = PriorityQueue()
	queue.put((heuristic(robot.row, robot.col, goal) + 0, -1,(robot.row, robot.col)))
	visited[robot.row][robot.col] = True
	while(not queue.empty()):
		f, priority, (row, col) = queue.get()
		# print(f, priority, row, col)
		if(check_found_goals([goal], row, col)):
			ans = print_path(row, col, path, instructions, robot)
			return ans
		for ind, instruction in enumerate(instructions):
			add_row = instructions[instruction][0]
			add_col = instructions[instruction][1]
			if(check_valid_move(maze, visited, row + add_row, col + add_col)):
				queue.put((heuristic(row + add_row, col + add_col, goal) + 1, ind,(row + add_row, col + add_col)))
				path[row+add_row][col+add_col] = instruction
				visited[row + add_row][col + add_col] = True
	return path
