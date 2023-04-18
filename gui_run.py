from constants import DEFAULT_COLS, DEFAULT_ROWS
from robot import Robot
from maze import Maze
from gui import gui
import sys


col_size = (int)(sys.argv[1])
row_size = (int)(sys.argv[2])
gui(Maze(row_size, col_size), Robot(0, 0), row_size, col_size, is_call_independent=True)
