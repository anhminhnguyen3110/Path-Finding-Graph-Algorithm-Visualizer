"""
Module common function for check if the robot founds all goals of check if 
- the robot can valid move to the adjacent square 
- check the stopping condition for searching strategy
- heuristic function for multiple goals
- print the path after searching.
"""
from queue import PriorityQueue
from common import (
    check_found_goals,
    check_valid_move,
    heuristic_for_multiple_goals,
    print_path,
)
from maze import Maze
from robot import Robot


# Greedy Best First Search strategy
def gbfs(
    robot: Robot,
    maze: Maze,
    instructions: dict[str, tuple[int, int]],
    draw_package: tuple = None,
) -> tuple[str, int]:
    # Gui
    if draw_package:
        draw, grid, wait, check_forbid_event = draw_package

        # Check if the robot is already at the goal
    for goal_row, goal_col in maze.goals:
        if robot.row == goal_row and robot.col == goal_col:
            return ("", 0)

        # Initialize the frontier, visited, path
    row_length = len(maze.grid)
    col_length = len(maze.grid[0])
    visited = [[False for j in range(col_length)] for i in range(row_length)]
    path = [["$" for j in range(col_length)] for i in range(row_length)]
    queue = PriorityQueue()

    # Add the start position to the frontier, and mark it as visited
    queue.put((0, -1, (robot.row, robot.col)))
    visited[robot.row][robot.col] = True

    while not queue.empty():
        # Current square
        _, _, (row, col) = queue.get()

        # Found goal here
        if check_found_goals(maze.goals, row, col):
            return print_path((row, col), path, instructions, (robot.row, robot.col))

        # Check all possible moves from current position to adjacent squares
        for ind, instruction in enumerate(instructions):
            next_square = (
                row + instructions[instruction][0],
                col + instructions[instruction][1],
            )

            # Check if the adjacent square is valid (not visited, not wall, not out of bound)
            if check_valid_move(maze, visited, next_square[0], next_square[1]):
                # Calculate the heuristic of the adjacent square
                h_value = heuristic_for_multiple_goals((next_square[0], next_square[1]), maze.goals)

                # Add the adjacent square to the frontier and mark it as visited
                queue.put(
                    (
                        h_value,
                        ind,  # To break ties when h_value is the same, we use the order of the instruction
                        (next_square[0], next_square[1]),
                    )
                )
                path[next_square[0]][next_square[1]] = instruction
                visited[next_square[0]][next_square[1]] = True

                # Gui
                if draw_package and not (
                    grid[next_square[1]][next_square[0]].is_end() or grid[next_square[1]][next_square[0]].is_start()
                ):
                    grid[next_square[1]][next_square[0]].assign_push_inside_queue()

        # Gui
        if draw_package:
            if not (grid[col][row].is_end() or grid[col][row].is_start()):
                grid[col][row].assign_pop_outside_queue()
        if draw_package:
            draw()
            check_forbid_event()
            wait()
    return ("No solution found.", 0)
