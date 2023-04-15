from common import check_found_goals, check_valid_move, print_path
from maze import Maze
from robot import Robot

def bfs(robot: Robot, maze: Maze, instructions: dict, draw_package):
	#gui
	if(draw_package): 
		draw, grid, wait, check_forbid_event = draw_package
  
	for(goal_row, goal_col) in maze.goals:
		if(robot.row == goal_row and robot.col == goal_col):
			return ("", 0)

	rows = len(maze.grid)
	cols = len(maze.grid[0])
	visited = [[False for j in range(cols)] for i in range(rows)]
	path = [["$" for j in range(cols)] for i in range(rows)]
	queue = []
	queue.append((robot.row, robot.col))
	visited[robot.row][robot.col] = True
 

	while(queue):
		row, col = queue.pop(0)
		if(check_found_goals(maze.goals, row, col)):
			ans = print_path(row, col, path, instructions, (robot.row, robot.col))
			return ans
		for instruction in instructions:
			new_row = row + instructions[instruction][0]
			new_col = col + instructions[instruction][1]
			if(check_valid_move(maze, visited, new_row, new_col)):
				queue.append((new_row, new_col))
				path[new_row][new_col] = instruction
				visited[new_row][new_col] = True
    
				#gui
				if(draw_package and not(grid[new_col][new_row].is_end() or grid[new_col][new_row].is_start())):
					grid[new_col][new_row].assign_push_inside_queue()
		#gui
		if(draw_package):
			if(not(grid[col][row].is_end() or grid[col][row].is_start())):
				grid[col][row].assign_pop_outside_queue()
		if(draw_package):
			draw()
			check_forbid_event()
			wait()
   
	return ("No solution found.", 0)
