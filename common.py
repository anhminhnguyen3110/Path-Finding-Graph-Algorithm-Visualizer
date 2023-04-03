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

def print_path(row, col, path, instructions, robot: Robot):
	trace = row, col
	ans = []
	while(trace != (robot.row, robot.col)):
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