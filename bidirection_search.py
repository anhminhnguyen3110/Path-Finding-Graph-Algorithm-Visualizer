"""
Module common function for check if the robot founds all goals of check if 
- the robot can valid move to the adjacent square 
- check the stopping condition for searching strategy
- print the path after searching.
"""
from common import (
    check_valid_move_for_bidirectional_search,
    print_path_bidirection,
)
from maze import Maze
from robot import Robot


def process_child_nodes(
    row: int,
    col: int,
    is_start: bool,
    visited: list,
    queue: list,
    path: list,
    maze: Maze,
    instructions: dict[str, tuple[int, int]],
    draw_package: tuple = None,
) -> tuple[tuple[int, int], tuple[int, int]]:
    # Gui
    if draw_package:
        _, grid, _, _ = draw_package

    # Check all possible moves from current position to adjacent squares
    for instruction in instructions:
        next_square = (
            row + instructions[instruction][0],
            col + instructions[instruction][1],
        )
        # Check if the adjacent square is valid (not visited, not wall, not out of bound)
        if check_valid_move_for_bidirectional_search(maze, next_square[0], next_square[1]):
            # Check if the adjacent square is not visited
            if not visited[next_square[0]][next_square[1]][0]:
                # Add the adjacent square to the frontier and mark it as visited
                queue.append((next_square[0], next_square[1], is_start))
                path[next_square[0]][next_square[1]] = instruction
                visited[next_square[0]][next_square[1]] = (1, is_start)
                # Gui
                if draw_package and not (
                    grid[next_square[1]][next_square[0]].is_end() or grid[next_square[1]][next_square[0]].is_start()
                ):
                    grid[next_square[1]][next_square[0]].assign_push_inside_queue()
            # Check if the adjacent square is visited by the other robot (overlapping)
            elif visited[next_square[0]][next_square[1]][0] and visited[next_square[0]][next_square[1]][1] != is_start:
                return ((row, col), (next_square[0], next_square[1]))
    return -1


# Bidirectional search strategy
def bidirection_search(
    robot: Robot,
    maze: Maze,
    instructions_start: dict,
    instructions_end: dict,
    draw_package: tuple = None,
) -> tuple[str, int]:
    # Gui
    if draw_package:
        draw, grid, wait, check_forbid_event = draw_package

    # Check if the robot is already at the goal
    for goal_row, goal_col in maze.goals:
        if robot.row == goal_row and robot.col == goal_col:
            return ("", 0)

    # Initialize the frontier, visited and path
    intersacting_point = -1
    row_length = len(maze.grid)
    col_length = len(maze.grid[0])
    visited = [[(0, True) for j in range(col_length)] for i in range(row_length)]
    path = [["$" for j in range(col_length)] for i in range(row_length)]
    queue = []

    # Add the start position to the frontier and mark it as visited
    queue.append((robot.row, robot.col, True))
    visited[robot.row][robot.col] = (1, True)
    path[robot.row][robot.col] = "start"

    # Add the list of goals to the frontier and mark it as visited
    goals = sorted(maze.goals, key=lambda x: (x[0], x[1]))
    for goal in goals:
        visited[goal[0]][goal[1]] = (1, False)
        queue.append((goal[0], goal[1], False))
        path[goal[0]][goal[1]] = "end"

    while queue:
        # Current square and its direction (search forward or backward)
        row, col, is_start = queue.pop(0)
        if is_start:  # Search forward
            intersacting_point = process_child_nodes(
                row,  # row from start point
                col,  # col from start point
                is_start,  # is start point
                visited,
                queue,
                path,
                maze,
                instructions_start,  # search forward
                draw_package,
            )
        else:  # Search backward
            intersacting_point = process_child_nodes(
                row,  # row from end point
                col,  # col from end point
                is_start,  # is end point
                visited,
                queue,
                path,
                maze,
                instructions_end,  # search backward
                draw_package,
            )

        # Gui
        if draw_package:
            if not (grid[col][row].is_end() or grid[col][row].is_start()):
                grid[col][row].assign_pop_outside_queue()
        if draw_package:
            draw()
            check_forbid_event()
            wait()

        # Check if two search forward and backward intersect
        if intersacting_point != -1:
            if is_start:
                # Check if the intersacting point is coming from the start point
                return print_path_bidirection(
                    intersacting_point[0],  # start point
                    intersacting_point[1],  # end point
                    path,  # path
                    (robot.row, robot.col),  # start point
                    goals,  # list of goals
                    instructions_start,  # instructions of start point
                    instructions_end,  # instructions of end point
                )
            else:
                # Check if the intersacting point is coming from the end point
                return print_path_bidirection(
                    intersacting_point[1],  # end point
                    intersacting_point[0],  # start point
                    path,  # path
                    (robot.row, robot.col),  # start point
                    goals,  # list of goals
                    instructions_start,  # instructions of start point
                    instructions_end,  # instructions of end point
                )
    return ("No solution found.", 0)
