from common import check_valid_move_for_bidirectional_search, find_goal_in_multiple_goals, print_path_bidirection
from maze import Maze
from robot import Robot
   
def bfs_for_bidirection(row: int, col: int, is_begin: bool, visited: list, queue: list, path: list, maze: Maze, instructions: dict):
	for instruction in instructions:
		new_row = row + instructions[instruction][0]
		new_col = col + instructions[instruction][1]
		if(check_valid_move_for_bidirectional_search(maze, new_row, new_col)):
			if(not visited[new_row][new_col][0]):
				queue.append((new_row, new_col, is_begin))
				path[new_row][new_col] = (instruction, is_begin)
				visited[new_row][new_col] = (1, is_begin)
			elif(visited[new_row][new_col][0] and visited[new_row][new_col][1] != is_begin):
				return ((row, col), (new_row, new_col))
	return -1

def bidirection(robot: Robot, maze: Maze, instructions_start: dict, instructions_end: dict):
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
			intersacting_point = bfs_for_bidirection(row, col, is_begin, visited, queue, path, maze, instructions_start)
		else:
			intersacting_point = bfs_for_bidirection(row, col, is_begin, visited, queue, path, maze, instructions_end)
		if(intersacting_point!=-1):
			if(is_begin):
				ans = print_path_bidirection(intersacting_point[0], intersacting_point[1], path, (robot.row, robot.col), (goal[0], goal[1]), instructions_start, instructions_end)
			else:
				ans = print_path_bidirection(intersacting_point[1], intersacting_point[0], path, (robot.row, robot.col), (goal[0], goal[1]), instructions_start, instructions_end)
			return ans
	return ("No solution found.", 0)