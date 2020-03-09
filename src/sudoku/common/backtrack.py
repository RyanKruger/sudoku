# Backtracking Algorithm

import math

from src.sudoku.sudoku9x9.sudoku_gen import Sudoku

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

class ElementNotFoundError(Exception):
    pass


def fill_grid(sudoku: Sudoku) -> bool:
    '''Backtracking Algorithm. Uses recursion to handle
    multiple incorrect digit placements by backtracking to
    an earlier state to try a different path.

    Args:
        sudoku: Sudoku class to operate on.
    
    Returns:
        Boolean of if a valid digit could be placed.
    '''
    unassigned_cell = find_unassigned()
    if unassigned_cell is None:
        return True
    for digit in range(1,9):
        good_fit = is_good_fit(sudoku, unassigned_cell, digit)
        if good_fit == True:
            sudoku.set_num(unassigned_cell, digit)
            recursion_successful = fill_grid(sudoku)
            if recursion_succesful:
                return True
            else:
                sudoku.set_num(unassigned_cell, 0) # Remove the digit.
    return False


def find_unassigned(sudoku: Sudoku) -> int:
    '''Find an empty cell in the given sudoku board.

    Args:
        sudoku: Sudoku class to operate on.
    Returns:
        Index of the unassigned space, or None if none.
    '''
    if sudoku is None:
        raise ValueError("ERROR: sudoku is None. Can't find_unassigned.")
    for i, cell in enumerate(sudoku.board):
        if cell == 0:
            return i    
    return None


def is_good_fit(sudoku: Sudoku, unassigned_cell: int, digit: int) -> bool:
    '''Checks to see if ``digit`` would be a legal fit in ``unassigned_cell``.

    Args:
        sudoku: Sudoku class to operate on.
        unassigned_cell: Index of the location in sudoku board to test.
        digit: Digit to try to place in the sudoku board.

    Returns:
        Boolean of if the digit will fit in the sudoku board or not.
    '''
    if sudoku is None:
        raise ValueError("ERROR: sudoku is None. Can't is_good_fit.")
    if not check_rows(sudoku, unassigned_cell, digit):
        return False
    if not check_cols(sudoku, unassigned_cell, digit):
        return False
    if not check_tile(sudoku, unassigned_cell, digit):
        return False
    return True


def check_rows(sudoku: Sudoku, unassigned_cell: int, digit: int) -> bool:
    '''Checks to see if the ``digit`` at ``unassigned_cell`` is valid for its row.

    Args:
        sudoku: Sudoku class to operate on.
        unassigned_cell: Index of the location in sudoku board to test.
        digit: Digit to try to place in the sudoku board.

    Returns:
        Boolean of if the digit will fit in that row or not.
    '''
    if sudoku is None:
        raise ValueError("ERROR: sudoku is None. Can't check_rows.")

    board_width = sudoku.get_width()
    if board_width < 1:
        raise ValueError(f"ERROR: board_width is {board_width}. Can't check_rows.")
    row = unassigned_cell // board_width
    for i in range(row*board_width, row*board_width+board_width):
        if sudoku.board[i] == digit:
            return False # Digit already exists in this row
    return True


def check_cols(sudoku: Sudoku, unassigned_cell: int, digit: int) -> bool:
    '''Checks to see if the ``digit`` at ``unassigned_cell`` is valid for its collumn.

    Args:
        sudoku: Sudoku class to operate on.
        unassigned_cell: Index of the location in sudoku board to test.
        digit: Digit to try to place in the sudoku board.

    Returns:
        Boolean of if the digit will fit in that collumn or not.
    '''
    if sudoku is None:
        raise ValueError("ERROR: sudoku is None. Can't check_cols.")

    board_width = sudoku.get_width()
    if board_width < 1:
        raise ValueError(f"ERROR: board_width is {board_width}. Can't check_cols.")
    col = unassigned_cell % board_width
    for i in range(col, (board_width**2)+col, board_width):
        if sudoku.board[i] == digit:
            return False # Digit already exists in this collumn
    return True

def check_tile(sudoku: Sudoku, unassigned_cell: int, digit: int) -> bool:
    '''Checks to see if the ``digit`` at ``unassigned_cell`` is valid for its tile.
    NOTE: I cheaped out here a bit with a lookup table, probably only going to deal
          with 4x4 and 9x9 boards anyways.
    Args:
        sudoku: Sudoku class to operate on.
        unassigned_cell: Index of the location in sudoku board to test.
        digit: Digit to try to place in the sudoku board.

    Returns:
        Boolean of if the digit will fit in that tile or not.
    '''
    if sudoku is None:
        raise ValueError("ERROR: sudoku is None. Can't check_tile.")

    board_width = sudoku.get_width()
    tile_width = math.sqrt(board_width)

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
    elif board_width == 4:
        lookup_table = four_indices
    elif board_width == 9:
        lookup_table = nine_indices

    for indices in lookup_table:
        try:
            tile_num = indices.index(unassigned_cell)
            break
        except ValueError:
            pass # Keep looking
    else:
        raise ElementNotFoundError("ERROR: Could not find element in lookup table.")

    for cell in lookup_table[tile_num]:
        if sudoku.board[cell] == digit:
            return False # Digit already exists in this tile
    return True




