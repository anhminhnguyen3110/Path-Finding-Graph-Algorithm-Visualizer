# Maze class for the grid visualization


class Maze:
    def __init__(self, col_size: int, row_size: int):
        self.col_size = col_size
        self.row_size = row_size
        self.grid = [["*" for i in range(col_size)] for j in range(row_size)]
        self.goals = []

    def set_maze_block(self, col: int, row: int, width: int, height: int):
        for i in range(height):
            for j in range(width):
                self.grid[row + i][col + j] = "#"

    def __str__(self) -> str:
        return str(self.grid)

    def set_size(self, row_size: int, col_size: int):
        self.row_size = row_size
        self.col_size = col_size
        self.grid = [["*" for i in range(col_size)] for j in range(row_size)]

    def get_maze(self, row: int, col: int):
        return self.grid[row][col]

    def set_goal(self, col: int, row: int):
        self.grid[row][col] = "G"
        self.goals.append((row, col))

    def clear(self):
        self.grid = [["*" for i in range(self.col_size)] for j in range(self.row_size)]
        self.goals = []

    def reset_single_node(self, row: int, col: int):
        self.grid[row][col] = "*"

    def add_goal(self, row: int, col: int):
        self.goals.append((row, col))

    def remove_goal(self, row: int, col: int):
        self.goals.remove((row, col))

    def set_block(self, row: int, col: int):
        self.grid[row][col] = "#"
