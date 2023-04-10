from maze import Maze
from robot import Robot
from square import Square

instructions = {(-1, 0): "up", (0, -1):  "left", (1, 0): "down",(0, 1): "right" }

def check_found_goals(goals, current_square: Square) -> bool:
	for goal in goals:
		if(goal[0] == current_square.row and goal[1] == current_square.col):
			return True
	return False

def print_path(current_square: Square, path, instructions, start: Square):
	trace = current_square
	ans = []
	while(trace != start):
		ans.append(path[trace.row][trace.col])
		trace = Square(trace.row - instructions[path[trace.row][trace.col]][0], trace.col - instructions[path[trace.row][trace.col]][1])
	ans.reverse()
	return "; ".join(ans)

def check_valid_move(maze: Maze, visited, next_square) -> bool:
	grid = maze.grid
	rows = len(grid)
	cols = len(grid[0])
	return 0 <= next_square.row < rows and 0 <= next_square.col < cols and not visited[next_square.row][next_square.col] and grid[next_square.row][next_square.col] != "#"

def find_goal_in_multiple_goals(maze: Maze, start: Square) -> tuple[int, int]:
	row, col = start.row, start.col
	goals = maze.get_goals()
	result = heuristic(start, maze.goals[0]), maze.goals[0]
	for goal in goals:
		if(heuristic(start, goal) < result[0]):
			result = (heuristic(start, goal), goal)
	return result[1]

def heuristic(current_square: Square, goal) -> int:
	return abs(current_square.row - goal[0]) + abs(current_square.col - goal[1])

def check_valid_move_for_bidirectional_search(maze: Maze, next_square:Square) -> bool:
	grid = maze.grid
	rows = len(grid)
	cols = len(grid[0])
	return 0 <= next_square.row < rows and 0 <= next_square.col < cols and grid[next_square.row][next_square.col] != "#"

def print_path_bidirection(intersect_start:Square, intersect_end:Square, path, start:Square, end:Square, instructions_start, instructions_end):
	ans = []
	trace = intersect_start
	while(trace != start):
		ans.insert(0, path[trace.row][trace.col][0])
		parent = Square(trace.row - instructions_start[path[trace.row][trace.col][0]][0], trace.col - instructions_start[path[trace.row][trace.col][0]][1])
		trace = parent
	trace = intersect_end
	ans.append(instructions[(intersect_end.row - intersect_start.row, intersect_end.col - intersect_start.col)])
	while(trace != end):
		ans.append(path[trace.row][trace.col][0])
		parent = Square(trace.row - instructions_end[path[trace.row][trace.col][0]][0], trace.col - instructions_end[path[trace.row][trace.col][0]][1])
		trace = parent
	return "; ".join(ans)

def print_path_bidirection_astar(intersect_node, path_start, path_end, start, end, instructions_start, instructions_end):
	ans = []
 
	trace = (intersect_node[0], intersect_node[1])

	while(trace != start):
		ans.append(path_start[trace.row][trace.col])
		parent = (trace.row - instructions_start[path_start[trace.row][trace.col]][0], trace.col - instructions_start[path_start[trace.row][trace.col]][1])
		trace = parent
  
	trace = (intersect_node[0], intersect_node[1])


	ans.reverse()
	while(trace != end):
		ans.append(path_end[trace.row][trace.col])
		parent = (trace.row - instructions_end[path_end[trace.row][trace.col]][0], trace.col - instructions_end[path_end[trace.row][trace.col]][1])
		trace = parent
	return "; ".join(ans)