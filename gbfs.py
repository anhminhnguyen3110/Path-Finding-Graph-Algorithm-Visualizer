from common import check_found_goals, check_valid_move, find_goal_in_multiple_goals, heuristic, print_path
from maze import Maze
from robot import Robot
from queue import PriorityQueue
from square import Square

def gbfs(robot: Robot, maze: Maze, instructions: dict):
	row_size = len(maze.grid)
	col_size = len(maze.grid[0])
	visited = [[False for j in range(col_size)] for i in range(row_size)]
	path = [["$" for j in range(col_size)] for i in range(row_size)]
	start = Square(robot.row, robot.col)
	goal = find_goal_in_multiple_goals(maze, start)
 
	queue = PriorityQueue()
	queue.put((heuristic(start, goal), -1,(start.row, start.col)))
	visited[start.row][start.col] = True
	while(not queue.empty()):
		f, priority, (row, col) = queue.get()
		current_square = Square(row, col)
		# print(f, priority, row, col)
		if(check_found_goals([goal], current_square)):
			ans = print_path(current_square, path, instructions, start)
			return ans
		for ind, instruction in enumerate(instructions):
			next_square = Square(current_square.row + instructions[instruction][0], current_square.col + instructions[instruction][1])
			if(check_valid_move(maze, visited, next_square)):
				queue.put((heuristic((next_square), goal), ind,(next_square.row, next_square.col)))
				path[next_square.row][next_square.col] = instruction
				visited[next_square.row][next_square.col] = True
	return "No solution found."