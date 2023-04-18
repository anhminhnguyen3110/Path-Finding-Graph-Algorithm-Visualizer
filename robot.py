class Robot:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __str__(self):
        return "Robot is at ({}, {})".format(self.row, self.col)

    def set_location(self, row: int, col: int):
        self.row = row
        self.col = col

    def reset(self):
        self.row = -1
        self.col = -1
