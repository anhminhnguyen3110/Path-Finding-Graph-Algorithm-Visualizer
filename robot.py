class Robot:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        
    def __str__(self):
        return "Robot is at ({}, {})".format(self.row, self.col)
    
    def set_location(self, row, col):
        self.row = row
        self.col = col
        
    def move(self, action):
        if(action == "UP"):
            self.col += 1
        elif(action == "DOWN"):
            self.col -= 1
        elif(action == "LEFT"):
            self.row -= 1
        elif(action == "RIGHT"):
            self.row += 1
        return 0