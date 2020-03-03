# Creates a 4x4 Sudoku board with brute force!

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

class Board:
    
    board = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0
    ]

    def set_num(self, index: int, value: int) -> None:
        self.board[index] = value

    def get_num(self, index: int) -> int:
        return self.board[index]

    def get_width(self) -> int:
        return math.sqrt(len(self.board))

    def __str__(self):
        string = ''
        for index in range(0,16,4):
            string += ','.join(str(digit) for digit in self.board[index:index+4])
            string += '\n'
        return string

def generateAllBoards(board: Board):
    '''Creates a 4x4 Board of every possible combination of numbers
    including illegal boardstates.
    '''
    NUMBOARDS = 1
    RADIX = 4
    SIDE_LEN = 4

    print(board)

    # Generate the first 4 boards
    for boardNum in range(NUMBOARDS):
        for msb in range(RADIX**10):
            ptr = (SIDE_LEN * SIDE_LEN) - 1
            while board.get_num(ptr) == (RADIX - 1):
                board.set_num(ptr, 0)
                ptr -= 1
            board.set_num(ptr, board.get_num(ptr) + 1)
            print(board)




def main():
    board = Board()
    generateAllBoards(board)


if __name__ == "__main__":
    main()