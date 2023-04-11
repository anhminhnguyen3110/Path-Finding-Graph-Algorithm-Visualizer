import pygame
from button import Button
from maze import Maze
from robot import Robot
from search_function import execute_search
from text_box import TextBox
INSTRUCTIONS = { "up" : (-1, 0), "left" : (0, -1), "down" : (1, 0), "right" : (0, 1) }
WIDTH = 720
WIDTH_WINDOW = 1450
HEIGHT_WINDOW = 760
WIN = pygame.display.set_mode((WIDTH_WINDOW, HEIGHT_WINDOW), pygame.RESIZABLE)
WAIT_VARIABLE_FOR_10_x_10 = 70
WAIT_VARIABLE_FOR_20_x_20 = 50
WAIT_VARIABLE_FOR_30_x_30 = 40
WAIT_VARIABLE_FOR_40_x_40 = 30
pygame.display.set_caption("RoboNavigation")

textBox = TextBox("","", "", 230, 100, (WIDTH+30, 15), WIN)

RED = (255, 0, 0)
CYAN = (0,255,255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
LIGHT_GREEN = (188,245,188)

class Node:
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.y = row * width
		self.x = col * width
		self.color = WHITE
		self.width = width

	def get_pos(self):
		return self.row, self.col

	def is_start(self):
		return self.color == GREEN

	def is_end(self):
		return self.color == RED

	def is_in_queue(self):
		return self.color == LIGHT_GREEN

	def is_out_queue(self):
		return self.color == CYAN
 
	def reset(self, maze: Maze, robot: Robot):
		maze.reset_single_node(self.row, self.col)
		if(self.color == GREEN):
			robot.reset()
		elif(self.color == RED):
			maze.remove_goal(self.row, self.col)
		self.color = WHITE
  
	def assign_start(self, robot: Robot):		
		self.color = GREEN
		robot.set_location(self.row, self.col)

	def assign_end(self, maze: Maze):
		self.color = RED
		maze.add_goal(self.row, self.col)
  
	def assign_pop_outside_queue(self):
		self.color = CYAN

	def assign_push_inside_queue(self):
		self.color = LIGHT_GREEN

	def assign_block(self, maze: Maze):
		self.color = BLACK
		maze.set_block(self.row, self.col)

	def assign_path(self):
		self.color = YELLOW

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x + 10, self.y + 10, self.width, self.width))
	
def algorithm(draw, wait, check_forbid_event, robot: Robot, maze: Maze, type_of_function, grid):
	(ans, number_of_steps) = execute_search(robot, maze, type_of_function, (draw, grid, wait, check_forbid_event))
	instruction_list = ans.split("; ")
	trace_col, trace_row = robot.col, robot.row
	while(instruction_list.__len__() - 1):
		instruction = INSTRUCTIONS[instruction_list.pop(0)]
		trace_row += instruction[0]
		trace_col += instruction[1]
		grid[trace_col][trace_row].assign_path()
	return number_of_steps


def assign_grid(rows,cols, width, maze: Maze):
	grid = []
	maze.clear()
	maze.set_size(cols, rows)
	gap = width // rows
	for i in range(cols):
		grid.append([])
		for j in range(rows):
			node = Node(j, i, gap, rows)
			grid[i].append(node)
	return grid


def draw_grid(win, rows,cols, width):
	gap = width // rows
	x = 0
	if(rows == cols):
		x = width
	elif(rows > cols):
		x = width - (gap * (abs(rows-cols)))
	else:
		x = width + (gap * (abs(rows-cols)))
	for i in range(rows+1):
		pygame.draw.line(win, GREY, (0 + 10, i * gap + 10), (x + 10, i * gap + 10))
		for j in range(cols+1):
			pygame.draw.line(win, GREY, (j * gap + 10, 0 + 10), (j * gap + 10, width + 10))

def assign_search_methods():
	search_methods = ['BFS', 'DFS', 'GBFS', 'ASTAR', 'Bidirectional Search', 'Bidirectional A Star']
	buttons = []
	for i in range(len(search_methods)):
		buttons.append(Button(search_methods[i], 200, 40, (1000,60 + i * 70), WIN, GREEN))
	buttons[0].is_selected = True
	return buttons

def assign_functional_button(search_methods):
	functional_button = ['Start', 'Clear Path', 'Clear Wall', 'Increase NoGoal', 'Decrease NoGoal', 'Increase Grid Size', 'Decrease Grid Size']
	buttons = []
	buttons.append(Button(functional_button[0], 200, 40, (1000,60 + search_methods.__len__() * 70 + 50), WIN, RED))

	buttons.append(Button(functional_button[1], 200, 40, (1000 - 200 - 10,60 + search_methods.__len__() * 70 + 70 + 50), WIN, RED))
	buttons.append(Button(functional_button[2], 200, 40, (1000,60 + search_methods.__len__() * 70 + 70 + 50), WIN, RED))
	buttons.append(Button(functional_button[3], 200, 40, (1000 + 200 + 10,60 + search_methods.__len__() * 70 + 70 + 50), WIN, RED))
 
	buttons.append(Button(functional_button[4], 200, 40, (1000 - 200 - 10,60 + (search_methods.__len__() + 1) * 70 + 70 + 50), WIN, RED))
	buttons.append(Button(functional_button[5], 200, 40, (1000,60 + (search_methods.__len__() + 1) * 70 + 70 + 50), WIN, RED))
	buttons.append(Button(functional_button[6], 200, 40, (1000 + 200 + 10,60 + (search_methods.__len__() + 1) * 70 + 70 + 50), WIN, RED))
 
	return buttons

def get_clicked_pos_of_search_buttons(pos, buttons, grid, maze, robot) -> str:
	for button in buttons:
		if button.is_clicked(pos):
			for i in range(len(buttons)):
				buttons[i].is_selected = False
			button.is_selected = True
			for i in range(grid.__len__()):
				for j in range(grid[0].__len__()):
					if(grid[i][j].color == CYAN or grid[i][j].color == LIGHT_GREEN or grid[i][j].color == YELLOW):
						grid[i][j].reset(maze, robot)
			return button.text
	return "BFS"

def get_clicked_pos_of_functional_buttons(pos, buttons, grid, maze, robot, draw, wait,check_forbid_event, type_of_function, max_end, ROWS, COLS, start, end):
	for button in buttons:
		if button.is_clicked(pos):
			if(button.text == 'Start' and type_of_function != '' and start and end.__len__()):
				number_of_steps = algorithm(draw,wait,check_forbid_event, robot, maze, type_of_function, grid)
				return (max_end, ROWS, COLS, start, end, grid, number_of_steps)
			if(button.text == 'Clear Path'):
				for i in range(grid.__len__()):
					for j in range(grid[0].__len__()):
						if(grid[i][j].color == CYAN or grid[i][j].color == LIGHT_GREEN or grid[i][j].color == YELLOW):
							grid[i][j].reset(maze, robot)
			if(button.text == 'Clear Wall'):
				for i in range(grid.__len__()):
					for j in range(grid[0].__len__()):
						if(grid[i][j].color == BLACK or grid[i][j].color == CYAN or grid[i][j].color == LIGHT_GREEN or grid[i][j].color == YELLOW):
							grid[i][j].reset(maze, robot)
			if(button.text == 'Increase NoGoal'):
					if(max_end < 5):
						max_end += 1
						return (max_end, ROWS, COLS, start, end, grid, 0)
			if(button.text == 'Decrease NoGoal'):
					if(max_end > 1):
						max_end -= 1
						if(end.__len__() > max_end):
							node = end.pop()
							for i in range(grid.__len__()):
								for j in range(grid[0].__len__()):
									if(grid[i][j].row == node.row and grid[i][j].col == node.col):
										grid[i][j].reset(maze, robot)
										break
						return (max_end, ROWS, COLS, start, end, grid, 0)
			if(button.text == 'Increase Grid Size'):
				if(ROWS < 40 and COLS < 40):
					ROWS += 10
					COLS += 10
					for i in range(grid.__len__()):
						for j in range(grid[0].__len__()):
								grid[i][j].reset(maze, robot)
					end = []
					start = None
					grid = assign_grid(ROWS, COLS, WIDTH, maze)
					max_end = 1
					return (max_end, ROWS, COLS, start, end, grid, 0)
			if(button.text == 'Decrease Grid Size'):
				if(COLS > 10 and ROWS > 10):
					COLS -= 10
					ROWS -= 10
					for i in range(grid.__len__()):
						for j in range(grid[0].__len__()):
								grid[i][j].reset(maze, robot)
					end = []
					start = None
					grid = assign_grid(ROWS, COLS, WIDTH, maze)
					max_end = 1
					return (max_end, ROWS, COLS, start, end, grid, 0)
	return (max_end, ROWS, COLS, start, end, grid, 0)

def draw_search_method(buttons, functional_buttons):
	for button in buttons:
		button.draw()
	for button in functional_buttons:
		button.draw()

def draw(win, grid, rows, cols, width, search_buttons, functional_buttons):
	win.fill(WHITE)

	for row in grid:
		for node in row:
			node.draw(win)

	draw_grid(win, rows,cols, width)
	draw_search_method(search_buttons, functional_buttons)
	textBox.draw()
	pygame.display.update()

def get_clicked_pos_of_grid(y,x, rows, width):
	x -= 10
	y -= 10
	gap = width // rows
	row = (y) // gap
	col = (x) // gap
	return row, col

def wait(x):
	pygame.time.wait(x)
def check_wait_time(rows, cols):
		if(rows == 10 and cols == 10):
			return WAIT_VARIABLE_FOR_10_x_10
		elif(rows == 20 and cols == 20):
			return WAIT_VARIABLE_FOR_20_x_20
		elif(rows == 30 and cols == 30):
			return WAIT_VARIABLE_FOR_30_x_30
		elif(rows == 40 and cols == 40):
			return WAIT_VARIABLE_FOR_40_x_40
def check_forbid_event():
	for event in pygame.event.get():	
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.VIDEORESIZE:
			pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

def main(win, width):
	ROWS = 20
	COLS = 20
	wait_variable = 0
	
	search_buttons = assign_search_methods()
	functional_buttons = assign_functional_button(search_buttons)
	robot: Robot = Robot(-1, -1)
	maze: Maze = Maze(10,10)
	grid = assign_grid(ROWS, COLS, width, maze)
	number_of_steps = 0
	start = 0
	end = []
	max_end = 1
	search_method = "BFS"
	run = True
	start_algorithm = False
 
	while run:
		draw(win, grid, ROWS,COLS, width, search_buttons, functional_buttons)
		textBox.update(str(maze.grid.__len__()), str(max_end), str(number_of_steps))
		wait_variable = check_wait_time(ROWS, COLS)
		for event in pygame.event.get():	
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.VIDEORESIZE:
				pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					run = False
			if pygame.mouse.get_pressed()[0]: # left pointer
				if(start_algorithm):
					continue
				pos = pygame.mouse.get_pos()
				(x,y) = pos
				if(x > WIDTH+10 and y < 450 and y > 60):
					search_method = get_clicked_pos_of_search_buttons(pos, search_buttons, grid, maze, robot)
					continue
				if(x > WIDTH+10 and y > 520 and y < 720):
					start_algorithm = True
					(max_end, ROWS, COLS, start, end, grid, number_of_steps) = get_clicked_pos_of_functional_buttons(pos, functional_buttons, grid, maze, robot, lambda: draw(win, grid, ROWS,COLS, width, search_buttons, functional_buttons), lambda: wait(wait_variable), lambda: check_forbid_event(), search_method, max_end, ROWS, COLS, start, end)
					start_algorithm = False
				if(x < 10 or y < 10 or x > WIDTH+10 or y > WIDTH + 10):
					continue
				row, col = get_clicked_pos_of_grid(x, y, ROWS, width)
				if(row < 0 or col < 0 or col >= ROWS or row >= COLS):
					continue
				node = grid[row][col]
				if not start and not node in end:
					start = node
					start.assign_start(robot)

				elif not node in end and node != start and end.__len__() < max_end:
					end.append(node)
					node.assign_end(maze)

				elif node != start and node not in end:
					node.assign_block(maze)

			elif pygame.mouse.get_pressed()[2]: # right pointer
				if(start_algorithm):
					continue
				pos = pygame.mouse.get_pos()
				(x,y) = pos
				if(x < 10 or y < 10 or x > WIDTH+10 or y > WIDTH + 10):
					continue
				row, col = get_clicked_pos_of_grid(x, y, ROWS, width)
				if(row < 0 or col < 0 or col >= ROWS or row >= COLS):
					continue
				node = grid[row][col]
				node.reset(maze, robot)
				if node == start:
					start = None
				elif node in end:
					end.remove(node)

			if event.type == pygame.KEYDOWN:
				if(start_algorithm):
					continue
				if event.key == pygame.K_SPACE and start and end:
					start_algorithm = True
					for i in range(grid.__len__()):
						for j in range(grid[0].__len__()):
							if(grid[i][j].color == CYAN or grid[i][j].color == LIGHT_GREEN or grid[i][j].color == YELLOW):
								grid[i][j].reset(maze, robot)
					number_of_steps = algorithm(lambda: draw(win, grid, ROWS,COLS, width, search_buttons, functional_buttons),lambda: wait(wait_variable), lambda: check_forbid_event(), robot, maze, search_method, grid)
					start_algorithm = False
				if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
					max_end = 1
					start = None
					end = []
					grid = assign_grid(ROWS, COLS, width, maze)
	pygame.quit()

main(WIN, WIDTH)