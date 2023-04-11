from common import check_valid_move, find_goal_in_multiple_goals, heuristic, print_path_bidirection_astar
from maze import Maze
from robot import Robot
from queue import PriorityQueue

def process_child_nodes(weight: list, row:int, col:int, queue: PriorityQueue,maze: Maze, visited: list, path: list, instructions: dict(), destination: tuple):
	for ind, instruction in enumerate(instructions):
		new_row = row + instructions[instruction][0]
		new_col = col + instructions[instruction][1]
		if(check_valid_move(maze, visited, new_row, new_col)):
			weight[new_row][new_col] = weight[row][col] + 1
			f = heuristic((new_row, new_col), destination) + weight[new_row][new_col]
			queue.put((f, ind,(new_row, new_col)))
			path[new_row][new_col] = instruction
			visited[new_row][new_col] = True

def bidirection_astar(robot: Robot, maze: Maze, instructions_start, instructions_end):
	rows = len(maze.grid)
	cols = len(maze.grid[0])
	goal = find_goal_in_multiple_goals(maze, robot)
	start = (robot.row, robot.col)
	visited_start = [[False for j in range(cols)] for i in range(rows)]
	visited_end = [[False for j in range(cols)] for i in range(rows)]
	path_start = [["$" for j in range(cols)] for i in range(rows)]
	path_end = [["$" for j in range(cols)] for i in range(rows)]
	weight_start = [[0 for j in range(cols)] for i in range(rows)]
	weight_end = [[0 for j in range(cols)] for i in range(rows)]
 
	queue_start = PriorityQueue()
	queue_end = PriorityQueue()
 
	queue_start.put((heuristic(start, goal), -1, (robot.row, robot.col)))
	queue_end.put((heuristic(goal, start), -1, (goal[0], goal[1])))
 
	visited_start[start[0]][start[1]] = True
	visited_end[goal[0]][goal[1]] = True 
	weight_start[start[0]][start[1]] = 0
	weight_end[goal[0]][goal[1]] = 0
	mu = float('inf')
	intersect_node = -1
	while(not queue_start.empty() and not queue_end.empty()):
		f, priority, (row_start, col_start) = queue_start.get()
		# print(row_start, col_start)
		if visited_start[row_start][col_start] and visited_end[row_start][col_start]:
			mu = min(mu, weight_start[row_start][col_start] + weight_end[row_start][col_start])
			intersect_node = (row_start, col_start)
			# print(row_start, col_start, weight_start[row_start][col_start], weight_end[row_start][col_start])
			# print()
		
		process_child_nodes(weight_start, row_start, col_start, queue_start, maze, visited_start, path_start, instructions_start, goal)
		
  
		f, priority, (row_end, col_end) = queue_end.get()
		# print(row_end, col_end)
		# print()
		if visited_start[row_end][col_end] and visited_end[row_end][col_end]:
			mu = min(mu, weight_start[row_end][col_end] + weight_end[row_end][col_end])
			intersect_node = (row_end, col_end)
			# print(row_end, col_end, weight_start[row_end][col_end], weight_end[row_end][col_end])
			# print()
  		
		process_child_nodes(weight_end, row_end, col_end, queue_end, maze, visited_end, path_end, instructions_end, start)
		if(queue_end.empty() or queue_start.empty()):
			break
		top1, top2 = queue_start.queue[0], queue_end.queue[0]
		# print("top1: ",top1[0],", top2: ", top2[0])
		if max(top1[0], top2[0]) >= mu:
			ans = print_path_bidirection_astar(intersect_node, path_start, path_end, (robot.row, robot.col), (goal[0], goal[1]), instructions_start, instructions_end)
			return ans
	return "No solution found."