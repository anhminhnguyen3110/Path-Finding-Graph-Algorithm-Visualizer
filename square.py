class Square:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
    def __add__(self, other):
        return Square(self.row + other.row, self.col + other.col)
    def __eq__(self, other) -> bool:
        return self.row == other.row and self.col == other.col
    def __sub__(self, other):
        return Square(self.row - other.row, self.col - other.col)
    def __ne__(self, other: object) -> bool:
        return self.row != other.row or self.col != other.col
    def __str__(self) -> str:
        return f"({self.row}, {self.col})"
    def __lt__(self, other: object) -> bool:
        return self.row < other.row or self.col < other.col
    def __le__(self, other: object) -> bool:
        return self.row <= other.row or self.col <= other.col
    def __gt__(self, other: object) -> bool:
        return self.row > other.row or self.col > other.col
    def __ge__(self, other: object) -> bool:
        return self.row >= other.row or self.col >= other.col
        