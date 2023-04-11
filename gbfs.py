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
	queue.put((heuristic((robot.row, robot.col), goal), -1,(robot.row, robot.col)))
	visited[robot.row][robot.col] = True
	while(not queue.empty()):
		f, priority, (row, col) = queue.get()
		# print(f, priority, row, col)
		if(check_found_goals([goal], row, col)):
			ans = print_path(row, col, path, instructions, (robot.row, robot.col))
			return ans
		for ind, instruction in enumerate(instructions):
			new_row = row + instructions[instruction][0]
			new_col = col + instructions[instruction][1]
			if(check_valid_move(maze, visited, new_row, new_col)):
				queue.put((heuristic((new_row, new_col), goal), ind,(new_row, new_col)))
				path[new_row][new_col] = instruction
				visited[new_row][new_col] = True
	return "No solution found."
