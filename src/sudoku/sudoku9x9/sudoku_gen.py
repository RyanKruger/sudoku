# Creates a Sudoku board.
# Thank you https://github.com/techwithtim/ for the inspiration!

import math

"""
A sudoku board is a 9x9 grid of digits [1-9]
Each row must contain exactly one of each digit [1-9]
Each collumn must contain exactly one of each digit [1-9]
Each non-overlapping 3x3 tile contain exactly one of each digit [1-9] (see below)

A sample solved boardstate may look like:
    ---------------------------------
    4   3   5 | 2   6   9 | 7   8   1
    6   8   2 | 5   7   1 | 4   9   3
    1   9   7 | 8   3   4 | 5   6   2
    ---------------------------------
    8   2   6 | 1   9   5 | 3   4   7
    3   7   4 | 6   8   2 | 9   1   5
    9   5   1 | 7   4   3 | 6   2   8
    ---------------------------------
    5   1   9 | 3   2   6 | 8   7   4
    2   4   8 | 9   5   7 | 1   3   6
    7   6   3 | 4   1   8 | 2   5   9
    --------------------------------- 

A puzzle can be created by removing some of the numbers (different board):
    ---------------------------------
              |           |          
        1   2 |     3   4 | 5   6   7
        3   4 | 5       6 | 1   8   2
    ---------------------------------
            1 |     5   8 | 2       6
            8 | 6         |         1
        2     |         7 |     5    
    ---------------------------------
            3 | 7       5 |     2   8
        8     |     6     | 7        
    2       7 |     8   3 | 6   1   5
    --------------------------------- 

"""

class Sudoku:

    # An empty board
    def __init__(self, board=None):
        if board is not None:
                self.board = board
        else:
            self.board = [
                0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0
            ] 

    def set_num(self, index: int, value: int) -> None:
        self.board[index] = value

    def get_num(self, index: int) -> int:
        return self.board[index]

    def get_width(self) -> float:
        width = math.sqrt(len(self.board))
        if width != 9.0:
            raise ValueError(f"ERROR: Found width to be {width}. Expected 9 for a 9x9 board.")
        return 9

    def __str__(self) -> str:
        string = ''
        for index in range(0,len(self.board),self.get_width()):
            string += ', '.join(str(digit) for digit in self.board[index:index+self.get_width()])
            string += '\n'
        return string


def main():
    pass


if __name__ == "__main__":
    main()