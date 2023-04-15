
from common import check_found_goals, check_valid_move, heuristic_for_multiple_goals, print_path
from maze import Maze
from robot import Robot
from queue import PriorityQueue


def astar(robot: Robot, maze: Maze, instructions: dict, draw_package):
	if(draw_package):
		draw, grid, wait, check_forbid_event = draw_package
	for(goal_row, goal_col) in maze.goals:
		if(robot.row == goal_row and robot.col == goal_col):
			return ("", 0)

	rows = len(maze.grid)
	cols = len(maze.grid[0])
	visited = [[False for j in range(cols)] for i in range(rows)]
	path = [["$" for j in range(cols)] for i in range(rows)]
	weight = [[0 for j in range(cols)] for i in range(rows)]
	queue = PriorityQueue()
	weight[robot.row][robot.col] = 0
	visited[robot.row][robot.col] = True
	queue.put((0, 0, (robot.row, robot.col)))
 

	while(not queue.empty()):
		f, weights, (row, col) = queue.get()
		if(check_found_goals(maze.goals, row, col)):
			ans = print_path(row, col, path, instructions, (robot.row, robot.col))
			return ans
		for ind, instruction in enumerate(instructions):
			new_row = row + instructions[instruction][0]
			new_col = col + instructions[instruction][1]
			if(check_valid_move(maze, visited, new_row, new_col)):
				weight[new_row][new_col] = weight[row][col] + 1
				f = heuristic_for_multiple_goals((new_row, new_col), maze.goals) + weight[new_row][new_col]
				queue.put((f, weight[new_row][new_col],(new_row, new_col)))
				path[new_row][new_col] = instruction
				visited[new_row][new_col] = True
				if(draw_package and not(grid[new_col][new_row].is_end() or grid[new_col][new_row].is_start())):
					grid[new_col][new_row].assign_push_inside_queue()
		if(draw_package):
			if(not(grid[col][row].is_end() or grid[col][row].is_start())):
				grid[col][row].assign_pop_outside_queue()
		if(draw_package):
			draw()
			check_forbid_event()
			wait()
	return ("No solution found.", 0)