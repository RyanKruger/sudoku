# Creates a Sudoku board.
# Thank you https://github.com/techwithtim/ for the inspiration!

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

class Board:

    # An empty board
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]



def main():



if __name__ == "__main__":
    main()