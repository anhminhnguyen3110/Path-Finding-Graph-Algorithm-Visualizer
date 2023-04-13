from common import check_valid_move_for_bidirectional_search, find_goal_in_multiple_goals, print_path_bidirection
from maze import Maze
from robot import Robot
   
def process_child_nodes(row: int, col: int, is_begin: bool, visited: list, queue: list, path: list, maze: Maze, instructions: dict, draw_package = None):
	if(draw_package):
		draw, grid, wait, check_forbid_event = draw_package
	for instruction in instructions:
		new_row = row + instructions[instruction][0]
		new_col = col + instructions[instruction][1]
		if(check_valid_move_for_bidirectional_search(maze, new_row, new_col)):
			if(not visited[new_row][new_col][0]):
				queue.append((new_row, new_col, is_begin))
				path[new_row][new_col] = (instruction, is_begin)
				visited[new_row][new_col] = (1, is_begin)
				if(draw_package and not(grid[new_col][new_row].is_end() or grid[new_col][new_row].is_start())):
					grid[new_col][new_row].assign_push_inside_queue()
			elif(visited[new_row][new_col][0] and visited[new_row][new_col][1] != is_begin):
				return ((row, col), (new_row, new_col))
	return -1

def bidirection(robot: Robot, maze: Maze, instructions_start: dict, instructions_end: dict, draw_package):
	if(draw_package):
		draw, grid, wait, check_forbid_event = draw_package
	intersacting_point = -1
	rows = len(maze.grid)
	cols = len(maze.grid[0])
	goal = find_goal_in_multiple_goals(maze, robot)
	visited = [[(0, True) for j in range(cols)] for i in range(rows)]
	path = [["$" for j in range(cols)] for i in range(rows)]
	queue = []
 
	queue.append((robot.row, robot.col, True))
	queue.append((goal[0], goal[1], False))
 
	visited[robot.row][robot.col] = (1, True)
	visited[goal[0]][goal[1]] = (1, False)
 
	path[robot.row][robot.col] = ("start", True)
	path[goal[0]][goal[1]] = ("end", False)
 
	if(goal[0] == robot.row and goal[1] == robot.col):
		return ("", 0)
	while(queue):
		row,col,is_begin = queue.pop(0)
		if(is_begin):
			intersacting_point = process_child_nodes(row, col, is_begin, visited, queue, path, maze, instructions_start, draw_package)
		else:
			intersacting_point = process_child_nodes(row, col, is_begin, visited, queue, path, maze, instructions_end, draw_package)
		if(intersacting_point!=-1):
			if(is_begin):
				ans = print_path_bidirection(intersacting_point[0], intersacting_point[1], path, (robot.row, robot.col), (goal[0], goal[1]), instructions_start, instructions_end)
			else:
				ans = print_path_bidirection(intersacting_point[1], intersacting_point[0], path, (robot.row, robot.col), (goal[0], goal[1]), instructions_start, instructions_end)
			return ans
		if(draw_package):
			if(not(grid[col][row].is_end() or grid[col][row].is_start())):
				grid[col][row].assign_pop_outside_queue()
		if(draw_package):
			draw()
			check_forbid_event()
			wait()
	return ("No solution found.", 0)