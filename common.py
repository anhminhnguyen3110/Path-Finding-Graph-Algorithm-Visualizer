from maze import Maze
from robot import Robot


def check_found_goals(goals, row, col) -> bool:
	for goal in goals:
		if(goal[0] == row and goal[1] == col):
			return True
	return False


def check_valid_move(maze: Maze, visited, row, col) -> bool:
	grid = maze.grid
	rows = len(grid)
	cols = len(grid[0])
	return 0 <= row < rows and 0 <= col < cols and not visited[row][col] and grid[row][col] != "#"

def print_path(row, col, path, instructions, start):
	trace = row, col
	ans = []
	while(trace != (start[0], start[1])):
		ans.append(path[trace[0]][trace[1]])
		parent = (trace[0] - instructions[path[trace[0]][trace[1]]][0], trace[1] - instructions[path[trace[0]][trace[1]]][1])
		trace = parent
	ans.reverse()
	return "; ".join(ans)

def heuristic(row, col, goal) -> int:
	return abs(row - goal[0]) + abs(col - goal[1])

def find_goal_in_multiple_goals(maze: Maze, robot: Robot) -> tuple[int, int]:
	row, col = robot.row, robot.col
	goals = maze.get_goals()
	result = heuristic(row, col, maze.goals[0]), maze.goals[0]
	for goal in goals:
		if(heuristic(row, col, goal) < result[0]):
			result = (heuristic(row, col, goal), goal)
	return result[1]

def print_path_bidirection(intersect_row, intersect_col, path_start, path_end, start, end, instructions_start, instructions_end):
	ans = []
 
	trace = (intersect_row, intersect_col)

	while(trace != start):
		ans.append(path_start[trace[0]][trace[1]])
		parent = (trace[0] - instructions_start[path_start[trace[0]][trace[1]]][0], trace[1] - instructions_start[path_start[trace[0]][trace[1]]][1])
		trace = parent
  
	trace = (intersect_row, intersect_col)

	ans.reverse()
	while(trace != end):
		ans.append(path_end[trace[0]][trace[1]])
		parent = (trace[0] - instructions_end[path_end[trace[0]][trace[1]]][0], trace[1] - instructions_end[path_end[trace[0]][trace[1]]][1])
		trace = parent
	return "; ".join(ans)

	
def check_intersecting_node(row_start, col_start, row_end, col_end, visited_start, visited_end):
	if(visited_start[row_end][col_end]):
		return (row_end, col_end)
	elif(visited_end[row_start][col_start]):
		return (row_start, col_start)
	return -1