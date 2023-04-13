from common import check_valid_move, find_goal_in_multiple_goals, heuristic, print_path_bidirection_astar
from maze import Maze
from robot import Robot
from queue import PriorityQueue

def process_child_nodes(weight: list, row:int, col:int, queue: PriorityQueue,maze: Maze, visited: list, path: list, instructions: dict(), destination: tuple, draw_package = None):
	if(draw_package):
		draw, grid, wait, check_forbid_event = draw_package
	for ind, instruction in enumerate(instructions):
		new_row = row + instructions[instruction][0]
		new_col = col + instructions[instruction][1]
		if(check_valid_move(maze, visited, new_row, new_col)):
			weight[new_row][new_col] = weight[row][col] + 1
			f = heuristic((new_row, new_col), destination) + weight[new_row][new_col]
			queue.put((f, ind,(new_row, new_col)))
			path[new_row][new_col] = instruction
			visited[new_row][new_col] = True
			if(draw_package and not(grid[new_col][new_row].is_end() or grid[new_col][new_row].is_start())):
				grid[new_col][new_row].assign_push_inside_queue()

def bidirection_astar(robot: Robot, maze: Maze, instructions_start, instructions_end, draw_package):
	if(draw_package):
		draw, grid, wait, check_forbid_event = draw_package
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
 
	if(goal[0] == robot.row and goal[1] == robot.col):
		return ("", 0)

	while(not queue_start.empty() and not queue_end.empty()):
		f, instruction, (row_start, col_start) = queue_start.get()
		if visited_start[row_start][col_start] and visited_end[row_start][col_start]:
			mu = min(mu, weight_start[row_start][col_start] + weight_end[row_start][col_start])
			intersect_node = (row_start, col_start)
		
		process_child_nodes(weight_start, row_start, col_start, queue_start, maze, visited_start, path_start, instructions_start, goal, draw_package)
		
		if(draw_package):
			if(not(grid[col_start][row_start].is_end() or grid[col_start][row_start].is_start())):
				grid[col_start][row_start].assign_pop_outside_queue()
		if(draw_package):
			draw()
		f, priority, (row_end, col_end) = queue_end.get()
		if visited_start[row_end][col_end] and visited_end[row_end][col_end]:
			mu = min(mu, weight_start[row_end][col_end] + weight_end[row_end][col_end])
			intersect_node = (row_end, col_end)
  		
		process_child_nodes(weight_end, row_end, col_end, queue_end, maze, visited_end, path_end, instructions_end, start, draw_package)
		if(draw_package):
			if(not(grid[col_end][row_end].is_end() or grid[col_end][row_end].is_start())):
				grid[col_end][row_end].assign_pop_outside_queue()
		if(draw_package):
			draw()
			check_forbid_event()
			wait()
   
		if(queue_end.empty() or queue_start.empty()):
			break
		top1, top2 = queue_start.queue[0], queue_end.queue[0]
		if max(top1[0], top2[0]) >= mu:
			ans = print_path_bidirection_astar(intersect_node, path_start, path_end, (robot.row, robot.col), (goal[0], goal[1]), instructions_start, instructions_end)
			return ans
	return ("No solution found.", 0)