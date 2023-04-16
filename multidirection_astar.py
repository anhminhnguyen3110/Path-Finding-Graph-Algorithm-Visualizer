from common import check_valid_move, heuristic, heuristic_for_multiple_goals, print_path_multidirection_astar
from maze import Maze
from robot import Robot
from queue import PriorityQueue

def process_child_nodes(is_start: bool, weight: list, row:int, col:int, queue: PriorityQueue,maze: Maze, visited: list, path: list, instructions: dict(), destination, draw_package = None):
    #gui
	if(draw_package):
		_, grid, _, _ = draw_package
	for ind, instruction in enumerate(instructions):
		new_row = row + instructions[instruction][0]
		new_col = col + instructions[instruction][1]
		if(check_valid_move(maze, visited, new_row, new_col)):
			weight[new_row][new_col] = weight[row][col] + 1
			if(is_start):
				f = heuristic_for_multiple_goals((new_row, new_col), destination) + weight[new_row][new_col]
			else:
				f = heuristic((new_row, new_col), destination) + weight[new_row][new_col]
			queue.put((f, weight[new_row][new_col],(new_row, new_col)))
			path[new_row][new_col] = instruction
			visited[new_row][new_col] = True
			#gui
			if(draw_package and not(grid[new_col][new_row].is_end() or grid[new_col][new_row].is_start())):
				grid[new_col][new_row].assign_push_inside_queue()

def multidirection_astar(robot: Robot, maze: Maze, instructions_start, instructions_end, draw_package):
	if(draw_package):
		draw, grid, wait, check_forbid_event = draw_package
	for(goal_row, goal_col) in maze.goals:
		if(robot.row == goal_row and robot.col == goal_col):
			return ("", 0)

	rows = len(maze.grid)
	cols = len(maze.grid[0])
	start = (robot.row, robot.col)
	visited_start = [[False for j in range(cols)] for i in range(rows)]
	visited_end = [[False for j in range(cols)] for i in range(rows)]
	path_start = [["$" for j in range(cols)] for i in range(rows)]
	path_end = [["$" for j in range(cols)] for i in range(rows)]
	weight_start = [[0 for j in range(cols)] for i in range(rows)]
	weight_end = [[0 for j in range(cols)] for i in range(rows)]
	queue_start = PriorityQueue()
	queue_end = PriorityQueue()
 
	weight_start[start[0]][start[1]] = 0
 
	queue_start.put((0, weight_start[start[0]][start[1]], (start[0], start[1])))
 
	visited_start[start[0]][start[1]] = True

	goals = sorted(maze.goals, key = lambda x: (x[0], x[1]))
	for goal in goals:
		weight_end[goal[0]][goal[1]] = 0
		queue_end.put((0, weight_end[goal[0]][goal[1]], (goal[0], goal[1])))
		visited_end[goal[0]][goal[1]] = True 
 
	while(not queue_start.empty() and not queue_end.empty()):
		#starting from start point
		_, _, (row_start, col_start) = queue_start.get()
		process_child_nodes(True, weight_start, row_start, col_start, queue_start, maze, visited_start, path_start, instructions_start, goals, draw_package)
		
  		#gui
		if(draw_package):
			if(not(grid[col_start][row_start].is_end() or grid[col_start][row_start].is_start())):
				grid[col_start][row_start].assign_pop_outside_queue()
		if(draw_package):
			draw()
			check_forbid_event()
			wait()
   
   		#starting from end point
		_, _, (row_end, col_end) = queue_end.get()
		process_child_nodes(False, weight_end, row_end, col_end, queue_end, maze, visited_end, path_end, instructions_end, start, draw_package)
  
		#gui
		if(draw_package):
			if(not(grid[col_end][row_end].is_end() or grid[col_end][row_end].is_start())):
				grid[col_end][row_end].assign_pop_outside_queue()
		if(draw_package):
			draw()
			check_forbid_event()
			wait()
   
		#check if two path intersect
		if (visited_end[row_start][col_start]) or (visited_start[row_end][col_end]):
			if(visited_end[row_start][col_start]):
				intersect_node = (row_start, col_start)
				ans = print_path_multidirection_astar(intersect_node, path_start, path_end, (robot.row, robot.col), goals, instructions_start, instructions_end)
				return ans
			else:
				intersect_node = (row_end, col_end)
				ans = print_path_multidirection_astar(intersect_node, path_start, path_end, (robot.row, robot.col), goals, instructions_start, instructions_end)
				return ans
	return ("No solution found.", 0)