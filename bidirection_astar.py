"""
Module common function for check if the robot founds all goals of check if 
- the robot can valid move to the adjacent square 
- check the stopping condition for searching strategy
- heuristic function for multiple goals
- heuristic function for single goal
- print the path after searching.
"""
from queue import PriorityQueue
from common import (
    check_valid_move,
    heuristic,
    heuristic_for_multiple_goals,
    print_path_bidirection_astar,
)
from maze import Maze
from robot import Robot


def process_child_nodes(
    is_start: bool,
    cost: list,
    row: int,
    col: int,
    queue: PriorityQueue,
    maze: Maze,
    visited: list,
    path: list,
    instructions: dict[str, tuple[int, int]],
    destination: tuple[int, int] | list[tuple[int, int]],
    number_of_nodes, # number of nodes
    draw_package: tuple = None,
):
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
        if check_valid_move(maze, visited, next_square[0], next_square[1]):
            # Calculate the cost and f_variable of the adjacent square
            cost[next_square[0]][next_square[1]] = cost[row][col] + 1
            if is_start:
                # f = g + h (calculate for next square from start position)
                f_variable = (
                    heuristic_for_multiple_goals((next_square[0], next_square[1]), destination)
                    + cost[next_square[0]][next_square[1]]
                )
            else:
                # f = g + h (calculate for next square from goals position)
                f_variable = (
                    heuristic((next_square[0], next_square[1]), destination) + cost[next_square[0]][next_square[1]]
                )

            number_of_nodes += 1
            # Add the adjacent square to the frontier and mark it as visited
            queue.put(
                (
                    f_variable,
                    number_of_nodes,
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
    return number_of_nodes


# Bidirectional A* strategy
def bidirection_astar(
    robot: Robot,
    maze: Maze,
    instructions_start: dict[str, tuple[int, int]],
    instructions_end: dict[str, tuple[int, int]],
    draw_package: tuple = None,
) -> tuple[str, int]:
    # Gui
    if draw_package:
        draw, grid, wait, check_forbid_event = draw_package

    #number of nodes
    number_of_nodes = 1
    
    # Check if the robot is already at the goal
    for goal_row, goal_col in maze.goals:
        if robot.row == goal_row and robot.col == goal_col:
            return ("", 0, number_of_nodes)

    # Initialize the frontier, visited, path and cost for start and end point
    row_length = len(maze.grid)
    col_length = len(maze.grid[0])
    start = (robot.row, robot.col)
    visited_start = [[False for j in range(col_length)] for i in range(row_length)]
    visited_end = [[False for j in range(col_length)] for i in range(row_length)]
    path_start = [["$" for j in range(col_length)] for i in range(row_length)]
    path_end = [["$" for j in range(col_length)] for i in range(row_length)]
    cost_start = [[float("inf") for j in range(col_length)] for i in range(row_length)]
    cost_end = [[float("inf") for j in range(col_length)] for i in range(row_length)]
    queue_start = PriorityQueue()
    queue_end = PriorityQueue()
    mu = float("inf")
    # Add the start position to the start_frontier, mark it as visited, and set its cost to 0
    cost_start[start[0]][start[1]] = 0
    visited_start[start[0]][start[1]] = True
    queue_start.put((0, number_of_nodes, (start[0], start[1])))

    # Add the goals position to the end_frontier, mark them as visited, and set their cost to 0
    goals = sorted(maze.goals, key=lambda x: (x[0], x[1]))
    for goal in goals:
        cost_end[goal[0]][goal[1]] = 0
        number_of_nodes += 1
        queue_end.put((0, number_of_nodes, (goal[0], goal[1])))
        visited_end[goal[0]][goal[1]] = True

    while not queue_start.empty() and not queue_end.empty():
        # Search forward
        _, _, (row_start, col_start) = queue_start.get()
        # if this is not the shortest path then update it as the shortest path
        if visited_start[row_start][col_start] and visited_end[row_start][col_start]:
            if(mu > cost_start[row_start][col_start] + cost_end[row_start][col_start]):
                mu = cost_start[row_start][col_start] + cost_end[row_start][col_start]
                intersect_node = (row_start, col_start)
                
        number_of_nodes = process_child_nodes(
            True,  # is_start
            cost_start,  # cost
            row_start,  # row from start point
            col_start,  # col from start point
            queue_start,  # queue of start point
            maze,
            visited_start,  # visited of start point
            path_start,  # path of start point to trace back
            instructions_start,  # instructions of start point
            goals,  # list of destination
            number_of_nodes, # number of nodes
            draw_package,
        )
        # Gui
        if draw_package:
            if not (grid[col_start][row_start].is_end() or grid[col_start][row_start].is_start()):
                grid[col_start][row_start].assign_pop_outside_queue()
        if draw_package:
            draw()
            check_forbid_event()
            wait()

        # Search backward
        _, _, (row_end, col_end) = queue_end.get()
        # if this is not the shortest path then update it as the shortest path
        if visited_start[row_end][col_end] and visited_end[row_end][col_end]:
            if(mu > cost_start[row_end][col_end] + cost_end[row_end][col_end]):
                mu = cost_start[row_end][col_end] + cost_end[row_end][col_end]
                intersect_node = (row_end, col_end)
                
        number_of_nodes = process_child_nodes(
            False,  # is_start
            cost_end,  # cost
            row_end,  # row from end point
            col_end,  # col from end point
            queue_end,  # queue of end point
            maze,
            visited_end,  # visited of end point
            path_end,  # path of end point to trace back
            instructions_end,  # instructions of end point
            start,  # start point (robot position)
            number_of_nodes, # number of nodes
            draw_package,
        )
        # Gui
        if draw_package:
            if not (grid[col_end][row_end].is_end() or grid[col_end][row_end].is_start()):
                grid[col_end][row_end].assign_pop_outside_queue()
        if draw_package:
            draw()
            check_forbid_event()
            wait()
            
        if queue_end.empty() or queue_start.empty():
            break
        
        top1, top2 = queue_start.queue[0], queue_end.queue[0]
        if mu <= max(top1[0], top2[0]):
            ans = print_path_bidirection_astar(
                intersect_node,
                path_start,
                path_end,
                (robot.row, robot.col),
                goals,
                instructions_start,
                instructions_end,
            )
            return (ans[0], ans[1], number_of_nodes)

    return ("No solution found.", 0, number_of_nodes)
