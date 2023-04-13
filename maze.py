class Maze:
    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.grid = [['*' for i in range(col)] for j in range(row)]
        self.goals = []
        
    def __str__(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.grid[i][j], end = " ")
            print()
            
    def set_maze_block(self, col, row, width, height):
        for i in range(height):
            for j in range(width):
                self.grid[row+i][col+j] = '#'
        
    def set_size(self, col, row):
        self.col = col
        self.row = row
        self.grid = [['*' for i in range(col)] for j in range(row)]
    
    def get_maze(self, row, col):
        return self.grid[row][col]
    
    def get_size(self):
        return self.col, self.row
    
    def get_goals(self):
        return self.goals
    
    def set_goal(self, col, row):
        self.grid[row][col] = 'G'
        self.goals.append((row, col))
        
    def clear(self):
        self.grid = [['*' for i in range(self.col)] for j in range(self.row)]
        self.goals = []
    
    def reset_single_node(self, row, col):
        self.grid[row][col] = '*'
    
    def add_goal(self, row, col):
        self.goals.append((row, col))
    
    def remove_goal(self, row, col):
        self.goals.remove((row, col))
    
    def set_block(self, row, col):
        self.grid[row][col] = '#'