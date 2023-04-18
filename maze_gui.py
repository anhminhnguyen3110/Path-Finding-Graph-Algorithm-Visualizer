import pygame
from constants import WAIT_VARIABLE_FOR_10_X_10, WAIT_VARIABLE_FOR_20_X_20, WAIT_VARIABLE_FOR_30_X_30
from constants import GREY
from maze import Maze
from robot import Robot
from square import Square


class MazeGui:
    def __init__(self, maze: Maze, robot: Robot, rows, cols, width) -> None:
        self.maze = maze
        self.robot = robot
        self.grid = []
        self.rows = rows
        self.cols = cols
        self.gap = 25
        self.width = self.gap * self.cols
        self.height = self.gap * self.rows
        self.number_of_goals = 1
        self.wait_variable = 0
        self.search_method = "BFS"
        self.start = None
        self.end = []
        self.assign_grid()

    def assign_grid(self) -> None:
        self.grid = []
        self.maze.clear()
        self.maze.set_size(self.cols, self.rows)
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.cols):
                square = Square(j, i, self.gap)
                self.grid[i].append(square)

    def get_clicked_pos_of_grid(self, pos) -> tuple[int, int]:
        # swap due to the way pygame draw the grid
        pos = (pos[1], pos[0])
        row = (pos[1] - 10) // self.gap
        col = (pos[0] - 10) // self.gap
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return None
        return self.grid[row][col]

    def draw_visual_grid(self, win):
        for i in range(self.cols + 1):
            pygame.draw.line(win, GREY, (0 + 10, i * self.gap + 10), (self.height + 10, i * self.gap + 10))
        for j in range(self.rows + 1):
            pygame.draw.line(win, GREY, (j * self.gap + 10, 0 + 10), (j * self.gap + 10, self.width + 10))

    def draw_grid(self, win):
        for row in self.grid:
            for square in row:
                square.draw(win)

    def clear_path(self):
        for i in range(self.grid.__len__()):
            for j in range(self.grid[0].__len__()):
                if self.grid[i][j].is_out_queue() or self.grid[i][j].is_in_queue() or self.grid[i][j].is_path():
                    self.grid[i][j].reset(self.maze, self.robot)

    def clear_wall(self):
        for i in range(self.grid.__len__()):
            for j in range(self.grid[0].__len__()):
                if (
                    self.grid[i][j].is_block()
                    or self.grid[i][j].is_out_queue()
                    or self.grid[i][j].is_in_queue()
                    or self.grid[i][j].is_path()
                ):
                    self.grid[i][j].reset(self.maze, self.robot)

    def clear_all(self):
        for i in range(self.grid.__len__()):
            for j in range(self.grid[0].__len__()):
                self.grid[i][j].reset(self.maze, self.robot)
        self.start = None
        self.number_of_goals = 1
        self.end = []

    def increase_no_of_goals(self):
        self.number_of_goals += 1

    def decrease_no_of_goals(self):
        if self.number_of_goals > 1:
            self.number_of_goals -= 1

    def increase_grid_size_col_size(self):
        if self.cols < 30:
            self.cols += 1
            self.width += 1 * self.gap
            self.clear_all()

        self.assign_grid()

    def increase_grid_size_row_size(self):
        if self.rows < 30:
            self.rows += 1
            self.height += 1 * self.gap
            self.clear_all()
        self.assign_grid()

    def decrease_grid_size_col_size(self):
        if self.cols > 2:
            self.cols -= 1
            self.width -= 1 * self.gap
            self.clear_all()
        self.assign_grid()

    def decrease_grid_size_row_size(self):
        if self.rows > 2:
            self.rows -= 1
            self.height -= 1 * self.gap
            self.clear_all()
        self.assign_grid()

    def pointer_in_grid(self, pos) -> bool:
        if pos[0] < 10 or pos[1] < 10 or pos[0] > self.height + 10 or pos[1] > self.width + 10:
            return False
        return True

    def execute_grid_left_click(self, square: Square):
        if not self.start and not square in self.end and not square.is_block():
            self.start = square
            square.assign_start(self.robot)

        elif (
            not square in self.end
            and square != self.start
            and self.end.__len__() < self.number_of_goals
            and not square.is_block()
        ):
            self.end.append(square)
            square.assign_end(self.maze)

        elif square != self.start and square not in self.end:
            square.assign_block(self.maze)

    def execute_grid_right_click(self, square: Square):
        square.reset(self.maze, self.robot)
        if square == self.start:
            self.start = None
        elif square in self.end:
            self.end.remove(square)

    def check_wait_time(self):
        if self.rows <= 10 or self.cols <= 10:
            self.wait_variable = WAIT_VARIABLE_FOR_10_X_10
        elif self.rows <= 20 or self.cols <= 20:
            self.wait_variable = WAIT_VARIABLE_FOR_20_X_20
        elif self.rows <= 30 or self.cols <= 30:
            self.wait_variable = WAIT_VARIABLE_FOR_30_X_30
        # elif self.rows <= 40 or self.cols <= 40:
        #     self.wait_variable = WAIT_VARIABLE_FOR_40_X_40

    def adapt_new_maze(self, maze: Maze, robot: Robot):
        self.maze = maze
        for i, x in enumerate(maze.grid):
            for j, y in enumerate(maze.grid[0]):
                if maze.grid[i][j] == "#":
                    self.grid[j][i].assign_block(self.maze)
                elif i == robot.row and j == robot.col:
                    self.grid[j][i].assign_start(self.robot)
                    self.start = self.grid[j][i]
                elif maze.grid[i][j] == "G":
                    self.grid[j][i].assign_end(self.maze)
                    self.end.append(self.grid[j][i])
                    if self.number_of_goals < self.end.__len__():
                        self.number_of_goals += 1
