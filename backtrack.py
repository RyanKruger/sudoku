# Backtracking Algorithm

import math

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
    '''Checks to see if the ``digit`` at ``unassigned_cell`` is valid for its row.

    Args:
        board: Sudoku board to operate on.
        unassigned_cell: Index of the location in ``board`` to test.
        digit: Digit to try to place in the sudoku ``board``.

    Returns:
        Boolean of if the digit will fit in that row or not.
    '''
    row = unassigned_cell // board.get_width()
    board_width = board.get_width()
    for i in range(row*board_width, row*board_width+board_width):
        if board[i] == digit:
            return False # Digit already exists in this row

def check_cols(board: Board, unassigned_cell: int, digit: int) -> bool:
    '''Checks to see if the ``digit`` at ``unassigned_cell`` is valid for its collumn.

    Args:
        board: Sudoku board to operate on.
        unassigned_cell: Index of the location in ``board`` to test.
        digit: Digit to try to place in the sudoku ``board``.

    Returns:
        Boolean of if the digit will fit in that collumn or not.
    '''
    col = unassigned_cell % board.get_width()
    board_width = board.get_width()
    for i in range(col, (board_width**2)+col, board_width):
        if board[i] == digit:
            return False # Digit already exists in this collumn


def check_tile(board: Board, unassigned_cell: int, digit: int) -> bool:
    '''Checks to see if the ``digit`` at ``unassigned_cell`` is valid for its tile.
    NOTE: I cheaped out here a bit with a lookup table, probably only going to deal
          with 4x4 and 9x9 boards anyways.
    Args:
        board: Sudoku board to operate on.
        unassigned_cell: Index of the location in ``board`` to test.
        digit: Digit to try to place in the sudoku ``board``.

    Returns:
        Boolean of if the digit will fit in that tile or not.
    '''
    board_width = board.get_width()
    tile_width = math.sqrt(board_width)
    tile_num = find_tile_num(board, unassigned_cell)

    four_indices = [[0,1,4,5],     # Tile 0
                    [2,3,6,7],     # Tile 1
                    [8,9,12,13],   # Tile 2
                    [10,11,14,15]] # Tile 3

    nine_indices = [[0,1,2,9,10,11,18,19,20],     # Tile 0
                    [3,4,5,12,13,14,21,22,23],    # Tile 1
                    [6,7,8,15,16,17,24,25,26],    # Tile 2
                    [27,28,29,36,37,38,45,46,47], # Tile 3
                    [30,31,32,39,40,41,48,49,50], # Tile 4
                    [33,34,35,42,43,44,51,52,53], # Tile 5
                    [54,55,56,63,64,65,72,73,74], # Tile 6
                    [57,58,59,66,67,68,75,76,77], # Tile 7
                    [60,61,62,69,70,71,78,79,80]] # Tile 8
    
    if board_width != 4 and board_width != 9:
        raise ValueError(f"ERROR: Oops! I didn't handle board width {board_width}.")
    else if board_width == 4:
        lookup_table = four_indices
    else if board_width == 9:
        lookup_table = nine_indices

    for i in range(board_width):
        try:
            tile_num = nine_indices.index(unassigned_cell)
        except ValueError:
            pass # Keep looking

    for i, tile in enumerate(lookup_table):
        if board[i] == digit:
            return False # Digit already exists in this collumn




