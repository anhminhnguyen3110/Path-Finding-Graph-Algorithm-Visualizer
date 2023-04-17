"""
Module maze to get information regarding the maze.
"""
from maze import Maze

instructions = {(-1, 0): "up", (0, -1): "left", (1, 0): "down", (0, 1): "right"}

# Check if the current position is a goal
def check_found_goals(goals: list[tuple[int, int]], row: int, col: int) -> bool:
    for goal in goals:
        if goal[0] == row and goal[1] == col:
            return True
    return False

# Check if the adjacent square is valid (not visited, not wall, not out of bound)
def check_valid_move(maze: Maze, visited: list, row: int, col: int) -> bool:
    grid = maze.grid
    rows = len(grid)
    cols = len(grid[0])
    return (
        0 <= row < rows
        and 0 <= col < cols
        and not visited[row][col]
        and grid[row][col] != "#"
    )

# Print the path from the start to the goal
def print_path(
    end: tuple[int, int],
    path: list,
    instruction: dict[str, tuple[int, int]],
    start: tuple[int, int],
) -> tuple[str, int]:
    trace = end
    ans = []
    # Trace back the path from the goal to the start
    while trace != start:
        ans.insert(0, path[trace[0]][trace[1]])
        direction = instruction[path[trace[0]][trace[1]]]
        parent = (
            trace[0] - direction[0],
            trace[1] - direction[1],
        )
        trace = parent
    return ("; ".join(ans), len(ans))


# Heuristic function for a single goal (Manhattan distance)
def heuristic(start: tuple[int, int], goal: tuple[int, int]) -> int:
    # Manhattan distance
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])


# Heuristic function for multiple goals (minimum Manhattan distance)
def heuristic_for_multiple_goals(
    start: tuple[int, int], goals: list[tuple[int, int]]
) -> int:
    result = float("inf")
    # Find the minimum Manhattan distance from the start to all goals
    for goal in goals:
        result = min(result, heuristic(start, goal))
    return result


# Check if the adjacent square is valid (not wall, not out of bound)
def check_valid_move_for_multidirectional_search(
    maze: Maze, row: int, col: int
) -> bool:
    grid = maze.grid
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= row < rows and 0 <= col < cols and grid[row][col] != "#"


# Print the path from the start to the intersect point and from the intersect point to the goal
def print_path_multidirection(
    intersect_start: tuple[int, int],
    intersect_end: tuple[int, int],
    path: list,
    start: tuple[int, int],
    end: list[tuple[int, int]],
    instructions_start: dict[str, tuple[int, int]],
    instructions_end: dict[str, tuple[int, int]],
) -> tuple[str, int]:
    ans = []
    trace = (intersect_start[0], intersect_start[1])
    # Trace back the path from the intersect point to the start
    while trace != start:
        ans.insert(0, path[trace[0]][trace[1]])
        direction = instructions_start[path[trace[0]][trace[1]]]
        parent = (
            trace[0] - direction[0],
            trace[1] - direction[1],
        )
        trace = parent
    trace = (intersect_end[0], intersect_end[1])
    
    # Add the intersect point to the path
    ans.append(
        instructions[
            (
                intersect_end[0] - intersect_start[0],
                intersect_end[1] - intersect_start[1],
            )
        ]
    )
    
    # Trace back the path from the intersect point to the goal
    while not trace in end:
        ans.append(path[trace[0]][trace[1]])
        direction = instructions_end[path[trace[0]][trace[1]]]
        parent = (
            trace[0] - direction[0],
            trace[1] - direction[1],
        )
        trace = parent
    return ("; ".join(ans), len(ans))


# Print the path from the start to the intersect point and from the intersect point to the goal
def print_path_multidirection_astar(
    intersect_node: tuple[int, int],
    path_start: list,
    path_end: list,
    start: tuple[int, int],
    end: list[tuple[int, int]],
    instructions_start: dict[str, tuple[int, int]],
    instructions_end: dict[str, tuple[int, int]],
) -> tuple[str, int]:
    ans = []

    trace = (intersect_node[0], intersect_node[1])
    # Trace back the path from the intersect point to the start
    while trace != start:
        ans.insert(0, path_start[trace[0]][trace[1]])
        direction = instructions_start[path_start[trace[0]][trace[1]]]
        parent = (
            trace[0] - direction[0],
            trace[1] - direction[1],
        )
        trace = parent

    trace = (intersect_node[0], intersect_node[1])
    
    # Add the intersect point to the path
    while not trace in end:
        ans.append(path_end[trace[0]][trace[1]])
        direction = instructions_end[path_end[trace[0]][trace[1]]]
        parent = (
            trace[0] - direction[0],
            trace[1] - direction[1],
        )
        trace = parent
    return ("; ".join(ans), len(ans))
