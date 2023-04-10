from common import check_valid_move_for_bidirectional_search, find_goal_in_multiple_goals, print_path_bidirection
from maze import Maze
from robot import Robot
from square import Square
   
def bfs_for_bidirection(current_square:Square, is_begin: bool, visited: list, queue: list, path: list, maze: Maze, instructions: dict):
	for instruction in instructions:
		next_square = Square(current_square.row + instructions[instruction][0], current_square.col + instructions[instruction][1])
		if(check_valid_move_for_bidirectional_search(maze, next_square)):
			if(not visited[next_square.row][next_square.col][0]):
				queue.append((next_square, is_begin))
				path[next_square.row][next_square.col] = (instruction, is_begin)
				visited[next_square.row][next_square.col] = (1, is_begin)
			elif(visited[next_square.row][next_square.col][0] and visited[next_square.row][next_square.col][1] != is_begin):
				return (current_square, next_square)
	return -1

def bidirection(robot: Robot, maze: Maze, instructions_start: dict, instructions_end: dict):
	intersacting_point = -1
	row_size = len(maze.grid)
	col_size = len(maze.grid[0])
	visited = [[(0, True) for j in range(col_size)] for i in range(row_size)]
	path = [["$" for j in range(col_size)] for i in range(row_size)]
	start = Square(robot.row, robot.col)
	goal = find_goal_in_multiple_goals(maze, start)
	queue = []
 
	queue.append((start, True))
	queue.append((Square(goal[0], goal[1]), False))
 
	visited[start.row][start.col] = (1, True)
	visited[goal[0]][goal[1]] = (1, False)
 
	path[start.row][start.col] = ("start", True)
	path[goal[0]][goal[1]] = ("end", False)
 
	while(queue):
		current_square,is_begin = queue.pop(0)
		if(is_begin):
			intersacting_point = bfs_for_bidirection(current_square, is_begin, visited, queue, path, maze, instructions_start)
		else:
			intersacting_point = bfs_for_bidirection(current_square, is_begin, visited, queue, path, maze, instructions_end)
		if(intersacting_point!=-1):
			if(is_begin):
				ans = print_path_bidirection(intersacting_point[0], intersacting_point[1], path, Square(robot.row, robot.col), Square(goal[0], goal[1]), instructions_start, instructions_end)
			else:
				ans = print_path_bidirection(intersacting_point[1], intersacting_point[0], path, Square(robot.row, robot.col), Square(goal[0], goal[1]), instructions_start, instructions_end)
			return ans
	return "No solution found."