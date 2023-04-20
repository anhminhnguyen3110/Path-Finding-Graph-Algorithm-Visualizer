"""
Module search function for execute search strategy
"""
from astar import astar
from bfs import bfs
from bidirection_search import bidirection_search
from bidirection_astar import bidirection_astar
from dfs import dfs
from gbfs import gbfs
from maze import Maze
from robot import Robot


def execute_search(robot: Robot, maze: Maze, type_of_function: str, draw_package: tuple = None) -> tuple[str, int, int]:                         
    type_of_function = type_of_function.lower()
    instructions_bfs = {"up": (-1, 0), "left": (0, -1), "down": (1, 0), "right": (0, 1)}
    instructions_dfs = {"right": (0, 1), "down": (1, 0), "left": (0, -1), "up": (-1, 0)}
    instructions_gbfs = {
        "up": (-1, 0),
        "left": (0, -1),
        "down": (1, 0),
        "right": (0, 1),
    }
    instructions_astar = {
        "up": (-1, 0),
        "left": (0, -1),
        "down": (1, 0),
        "right": (0, 1),
    }
    instructions_bidirection = {
        "down": (-1, 0),
        "right": (0, -1),
        "up": (1, 0),
        "left": (0, 1),
    }
    if type_of_function == "bfs":
        return bfs(robot, maze, instructions_bfs, draw_package)
    elif type_of_function == "dfs":
        return dfs(robot, maze, instructions_dfs, draw_package)
    elif type_of_function == "gbfs":
        return gbfs(robot, maze, instructions_gbfs, draw_package)
    elif type_of_function == "astar" or type_of_function == "as":
        return astar(robot, maze, instructions_astar, draw_package)
    elif type_of_function == "cus1" or type_of_function == "bidirectional search":
        return bidirection_search(robot, maze, instructions_bfs, instructions_bidirection, draw_package)
    elif type_of_function == "cus2" or type_of_function == "bidirectional a*":
        return bidirection_astar(robot, maze, instructions_astar, instructions_bidirection, draw_package)
    else:
        return bfs(robot, maze, instructions_bfs, draw_package)
