import pygame
from constants import BLACK, CYAN, GREEN, LIGHT_GREEN, RED, WHITE, YELLOW
from maze import Maze
from robot import Robot


class Square:
    def __init__(self, row, col, width):
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

    def is_path(self):
        return self.color == YELLOW

    def is_block(self):
        return self.color == BLACK

    def reset(self, maze: Maze, robot: Robot):
        maze.reset_single_node(self.row, self.col)
        if self.is_start():
            robot.reset()
        elif self.is_end():
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
        pygame.draw.rect(
            win, self.color, (self.x + 10, self.y + 10, self.width, self.width)
        )
    def __str__(self) -> str:
        return "Square is at ({}, {})".format(self.row, self.col)