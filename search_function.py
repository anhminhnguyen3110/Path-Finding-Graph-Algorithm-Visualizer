from maze import Maze
from robot import Robot
from queue import PriorityQueue

def execute_search(robot: Robot, maze: Maze, type_of_function: str):
    type_of_function = type_of_function.lower()
    instructions = { "up" : (-1, 0), "left" : (0, -1), "down" : (1, 0), "right" : (0, 1) }
    instructions_dfs = { "right" : (0, 1), "down" : (1, 0), "left" : (0, -1), "up" : (-1, 0) }
    priority_direction = {"up" : 0, "left" : 1, "down" : 2, "right" : 3}
    match type_of_function:
        case 'dfs':
            return dfs(robot, maze, instructions_dfs)
        case 'bfs':
            return bfs(robot, maze, instructions)
        case 'gbfs':
            return gbfs()
        case 'astar':
            return astar()
        case 'a*':
            return astar()
        case default:
            return bfs(robot, maze, instructions)
        
def bfs(robot: Robot, maze: Maze, instructions: dict):
    rows = len(maze.grid)
    cols = len(maze.grid[0])
    visited = [[False for j in range(cols)] for i in range(rows)]
    path = [["$" for j in range(cols)] for i in range(rows)]
    queue = []
    queue.append((robot.row, robot.col))
    visited[robot.row][robot.col] = True
    while(queue):
        row, col = queue.pop(0)
        if(check_found_goal(maze, row, col)):
            ans = print_path(row, col, path, instructions, robot)
            return ans
        for instruction in instructions:
            add_row = instructions[instruction][0]
            add_col = instructions[instruction][1]
            if(check_valid_move(maze, visited, row + add_row, col + add_col)):
                queue.append((row + add_row, col + add_col))
                path[row+add_row][col+add_col] = instruction
                visited[row + add_row][col + add_col] = True
    return path

def dfs(robot: Robot, maze: Maze, instructions: dict):
    rows = len(maze.grid)
    cols = len(maze.grid[0])
    visited = [[False for j in range(cols)] for i in range(rows)]
    path = [["$" for j in range(cols)] for i in range(rows)]
    stack = []
    stack.append((robot.row, robot.col))
    while(stack):
        row, col = stack.pop()
        visited[row][col] = True
        if(check_found_goal(maze, row, col)):
            ans = print_path(row, col, path, instructions, robot)
            return ans
        for instruction in instructions:
            add_row = instructions[instruction][0]
            add_col = instructions[instruction][1]
            if(check_valid_move(maze, visited, row + add_row, col + add_col)):
                stack.append((row + add_row, col + add_col))
                path[row+add_row][col+add_col] = instruction
    return path

def gbfs():
    # Path: search_function.py
    pass        

def astar():
#     rows = len(maze.grid)
#     cols = len(maze.grid[0])
#     visited = [[False for j in range(cols)] for i in range(rows)]
#     path = [["$" for j in range(cols)] for i in range(rows)]
#     queue = PriorityQueue()
#     queue._put((robot.row, robot.col))
#     visited[robot.row][robot.col] = True

#     while(queue):
#         row, col = queue.pop(0)
#         if(check_found_goal(maze, row, col)):
#             ans = print_path(row, col, path, instructions, robot)
#             return ans
#         for instruction in instructions:
#             add_row = instructions[instruction][0]
#             add_col = instructions[instruction][1]
#             if(check_valid_move(maze, visited, row + add_row, col + add_col)):
#                 queue.append((row + add_row, col + add_col))
#                 path[row+add_row][col+add_col] = instruction
#                 visited[row + add_row][col + add_col] = True
#                 # print(row + add_row, col + add_col)
#     return path
    pass

def check_valid_move(maze: Maze, visited, row, col):
    grid = maze.grid
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= row < rows and 0 <= col < cols and not visited[row][col] and grid[row][col] != "#"

def check_found_goal(maze: Maze, row, col):
    for goal in maze.get_goals():
        if(goal[0] == row and goal[1] == col):
            return True
    return False

def print_path(row, col, path, instructions, robot: Robot):
    trace = row, col
    ans = []
    while(trace != (robot.row, robot.col)):
        ans.append(path[trace[0]][trace[1]])
        parent = (trace[0] - instructions[path[trace[0]][trace[1]]][0], trace[1] - instructions[path[trace[0]][trace[1]]][1])
        trace = parent
    ans.reverse()
    return "; ".join(ans)

def heuristic(row, col, goal) -> int:
    return abs(row - goal[0]) + abs(col - goal[1])