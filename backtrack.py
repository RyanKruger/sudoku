# Backtracking Algorithm
"""
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
        [0, 1, 2, 0, 3, 4, 5, 6, 7],
        [0, 3, 4, 5, 0, 6, 1, 8, 2],
        [0, 0, 1, 0, 5, 8, 2, 0, 6],
        [0, 0, 8, 6, 0, 0, 0, 0, 1],
        [0, 2, 0, 0, 0, 7, 0, 5, 0],
        [0, 0, 3, 7, 0, 5, 0, 2, 8],
        [0, 8, 0, 0, 6, 0, 7, 0, 0],
        [2, 0, 7, 0, 8, 3, 6, 1, 5]
    ]

    def get_width(self):
        pass

def fill_grid(board: Board) -> bool:
    unassigned_cell = find_unassigned()
    if unassigned_cell is None:
        return True
    for digit in range(1,9):
        good_fit = is_good_fit(board, unassigned_cell, digit)
        if good_fit == True:
            assign_digit(board, unassigned_cell, digit)
            recursion_successful = fill_grid(board)
            if recursion_succesful:
                return True
            else:
                assign_digit(unassigned_cell, 0) # Remove the digit.
    else:
        return False

def find_unassigned(board: Board) -> int:
    '''Find an empty cell in the given sudoku board.

    Args:
        board: Sudoku board to operate on.
    Returns:
        Index of the unassigned space, or None if none.
    '''

    for i, cell in enumerate(board):
        if cell == 0:
            return i
    else:
        return None


def is_good_fit(board: Board, unassigned_cell: int, digit: int) -> bool:
    if not check_rows(board, unassigned_cell, digit):
        return False
    '''if not check_cols(board, unassigned_cell, digit):
        return False
    if not check_tile(board, unassigned_cell, digit):
        return False'''
    return True

def check_rows(board: Board, unassigned_cell: int, digit: int) -> bool:
    '''

    Args:
        board: Sudoku board to operate on.
        digit: Digit to try to place in the sudoku board.

    Returns:
        Boolean if the digit will fit or not.
    '''
    row = unassigned_cell // board.get_width()
    for i in range(row*board.get_width(), row*board.get_width()+board.get_width()):
        if board[i] == digit:
            return False # Digit already exists in this row