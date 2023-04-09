from common import check_intersecting_node, check_valid_move, find_goal_in_multiple_goals, print_path_bidirection
from maze import Maze
from robot import Robot
   
def bfs_for_bidirection( row:int, col:int, visited: list, queue: list, path: list, maze: Maze, instructions: dict):
	for instruction in instructions:
		new_row = row + instructions[instruction][0]
		new_col = col + instructions[instruction][1]
		if(check_valid_move(maze, visited, new_row, new_col)):
			queue.append((new_row, new_col))
			path[new_row][new_col] = instruction
			visited[new_row][new_col] = True

def bidirection(robot: Robot, maze: Maze, instructions_start: dict, instructions_end: dict):
	rows = len(maze.grid)
	cols = len(maze.grid[0])
	goal = find_goal_in_multiple_goals(maze, robot)
	visited_start = [[False for j in range(cols)] for i in range(rows)]
	visited_end = [[False for j in range(cols)] for i in range(rows)]
	path_start = [["$" for j in range(cols)] for i in range(rows)]
	path_end = [["$" for j in range(cols)] for i in range(rows)]
	queue_start = []
	queue_end = []
 
	queue_start.append((robot.row, robot.col))
	visited_start[robot.row][robot.col] = True
	path_start[robot.row][robot.col] = "start"
 
	queue_end.append((goal[0], goal[1]))
	visited_end[goal[0]][goal[1]] = True
	path_end[goal[0]][goal[1]] = "end"
 
	while(queue_start and queue_end):
		row_start, col_start = queue_start.pop(0)
		row_end, col_end = queue_end.pop(0)
		# print(row_start, col_start)
		# print(row_end, col_end)
		# print()
		if(check_intersecting_node(row_start, col_start, row_end, col_end, visited_start, visited_end)!=-1):
			intersect_row, intersect_col = check_intersecting_node(row_start, col_start, row_end, col_end, visited_start, visited_end)
			# print(intersect_row, intersect_col)
			# print()
			ans = print_path_bidirection(intersect_row, intersect_col, path_start, path_end, (robot.row, robot.col), (goal[0], goal[1]), instructions_start, instructions_end)
			# print(ans)
			return ans
		bfs_for_bidirection(row_start, col_start, visited_start, queue_start, path_start, maze, instructions_start)
		bfs_for_bidirection(row_end, col_end, visited_end, queue_end, path_end, maze, instructions_end)
	return "No solution found."

