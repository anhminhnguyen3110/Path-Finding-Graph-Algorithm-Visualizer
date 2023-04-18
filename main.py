# Description: This file is the main file of the project. It reads the input_line file and creates the maze and robot objects.
import sys
from gui import gui
from maze import Maze
from robot import Robot
from search_function import execute_search

robot = Robot(0, 0)
maze = Maze(0, 0)


def read_file_and_create_mize(file_name) -> None:
    try:
        with open(file_name, "r", encoding="utf8") as file:
            input_lines = file.read().splitlines()
    except IOError:
        print("File not found")
        return 1

    for index, input_line in enumerate(input_lines):
        if index == 0:
            strings = input_line[1:-1].split(",")
            if strings[1][-1] == ")" or strings[1][-1] == "]":
                strings[1] = strings[1][:-1]
            maze.set_size(int(strings[0]), int(strings[1]))

        if index == 1:
            strings = input_line[1:-1].split(",")
            if strings[0] == "" or strings[1] == "":
                robot.set_location(0, 0)
                continue
            elif strings[1][-1] == ")" or strings[1][-1] == "]":
                strings[1] = strings[1][:-1]
            robot.set_location(int(strings[1]), int(strings[0]))

        if index == 2:
            goals_in_stringsing = input_line[1:-1].split(
                ") | (",
            )
            for goal_in_stringsing in goals_in_stringsing:
                goal = goal_in_stringsing.split(",")
                if goal[0] == "" or goal[1] == "":
                    continue
                elif goal[1][-1] == ")" or goal[1][-1] == "]":
                    goal[1] = goal[1][:-1]
                maze.set_goal(int(goal[0]), int(goal[1]))
        if index > 2:
            stringss = input_line[1:-1].split(",")
            block_input_line = []
            for index, strings in enumerate(stringss):
                if strings[-1] == ")" or strings[-1] == "]":
                    strings = strings[:-1]
                block_input_line.append(int(strings))
            maze.set_maze_block(
                block_input_line[0],
                block_input_line[1],
                block_input_line[2],
                block_input_line[3],
            )
    file.close()
    return


def main():
    file_name = sys.argv[1]
    method = sys.argv[2]
    read_file_and_create_mize(file_name)
    answer, step = execute_search(robot, maze, method)
    if maze.row_size < 30 or maze.col_size <= 30:
        gui(
            maze,
            robot,
            maze.row_size,
            maze.col_size,
            is_call_independent=False,
            file_name=file_name,
            search_method=method,
        )
    else:
        print(file_name, method, step)
        print(answer)
    return


main()
