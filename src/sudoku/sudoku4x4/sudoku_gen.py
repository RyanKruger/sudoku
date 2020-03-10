# Creates a 4x4 Sudoku board.

import math



"""
A mini-sudoku board is a 4x4 grid of digits [1-4]
Each row must contain exactly one of each digit [1-4]
Each collumn must contain exactly one of each digit [1-4]
Each non-overlapping 2x2 tile contain exactly one of each digit [1-4] (see below)

A sample solved boardstate may look like:
    1   2 | 3   4  
    3   4 | 1   2
    -------------
    2   3 | 4   1
    4   1 | 2   3

"""

class Sudoku:
    
    # An empty board
    def __init__(self, board=None):
        if board is not None:
            self.board = board
        else:
            self.board = [
                0, 0, 0, 0,
                0, 0, 0, 0,
                0, 0, 0, 0,
                0, 0, 0, 0
            ] 

    def set_num(self, index: int, value: int) -> None:
        self.board[index] = value

    def get_num(self, index: int) -> int:
        return self.board[index]

    def get_width(self) -> float:
        width = math.sqrt(len(self.board))
        if width != 4.0:
            raise ValueError(f"ERROR: Found width to be {width}. Expected 4 for a 4x4 board.")
        return 4

    def __str__(self) -> str:
        string = ''
        for index in range(0,len(self.board),self.get_width()):
            string += ', '.join(str(digit) for digit in self.board[index:index+self.get_width()])
            string += '\n'
        return string


def generateAllSudokus(sudoku: Sudoku):
    '''Creates a 4x4 Sudoku of every possible combination of numbers
    including illegal board states.
    '''
    NUMBOARDS = 1
    RADIX = 4
    SIDE_LEN = 4

    print(sudoku)

    # Generate the first 4 boards
    for boardNum in range(NUMBOARDS):
        for msb in range(RADIX**10):
            ptr = (SIDE_LEN * SIDE_LEN) - 1
            while sudoku.board[ptr] == (RADIX - 1):
                sudoku.set_num(ptr, 0)
                ptr -= 1
            sudoku.set_num(ptr, sudoku.board[ptr] + 1)
            print(sudoku)




def main():
    sudoku = Sudoku()
    generateAllSudokus(sudoku)


if __name__ == "__main__":
    main()