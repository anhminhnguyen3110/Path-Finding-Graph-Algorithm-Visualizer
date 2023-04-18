"""
Module common function for check if the robot founds all goals of check if 
- the robot can valid move to the adjacent square 
- check the stopping condition for searching strategy
- print the path after searching.
"""
from common import check_found_goals, check_valid_move, print_path
from maze import Maze
from robot import Robot


# Depth-first search strategy
def dfs(
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

    # Add the start position to the frontier
    stack = []
    stack.append((robot.row, robot.col))

    while stack:
        # Current square
        row, col = stack.pop()

        # Mark the current square as visited
        visited[row][col] = True

        # Found goal here
        if check_found_goals(maze.goals, row, col):
            return print_path((row, col), path, instructions, (robot.row, robot.col))

        # Check all possible moves from current position to adjacent squares
        for instruction in instructions:
            next_square = (
                row + instructions[instruction][0],
                col + instructions[instruction][1],
            )

            # Check if the adjacent square is valid (not visited, not wall, not out of bound)
            if check_valid_move(maze, visited, next_square[0], next_square[1]):
                # Add the adjacent square to the frontier and mark it as visited
                stack.append((next_square[0], next_square[1]))
                path[next_square[0]][next_square[1]] = instruction

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
