import pytest

from src.sudoku.common.backtrack import check_tile, ElementNotFoundError
from src.sudoku.sudoku9x9.sudoku_gen import Sudoku

# Test check_tile()
def test_null_sudoku():
    data = None
    with pytest.raises(ValueError):
        check_tile(data, 0, 0)

def test_empty_board():
    data = Sudoku()
    data.board = []
    with pytest.raises(ValueError):
        check_tile(data, 0, 0)

def test_strange_board_width():
    data = Sudoku()
    data.board = [ # 8x8 board
        0, 3, 0, 0, 0, 1, 0, 0,
        0, 1, 2, 0, 3, 4, 5, 6,
        0, 3, 4, 5, 0, 6, 1, 8,
        0, 0, 1, 0, 5, 8, 2, 0,
        0, 0, 8, 6, 0, 0, 0, 0,
        1, 2, 0, 0, 0, 7, 0, 5,
        0, 0, 3, 7, 0, 5, 0, 2,
        0, 8, 0, 0, 6, 0, 7, 0
    ]
    with pytest.raises(ValueError):
        check_tile(data, 0, 0)

def test_strange_unassigned_cell_neg():
    data = Sudoku()
    with pytest.raises(ElementNotFoundError):
        check_tile(data, -1, 0)

def test_strange_unassigned_cell_large():
    data = Sudoku()
    with pytest.raises(ElementNotFoundError):
        check_tile(data, 81, 0)


def test_first_success():
    data = Sudoku()
    data.board = [
        #
        0, 0, 0, 5, 0, 1, 0, 0, 0, # Index 0
        0, 1, 2, 0, 3, 4, 5, 6, 7,
        0, 3, 4, 5, 0, 6, 1, 8, 2,
        5, 0, 1, 0, 5, 8, 2, 0, 6,
        0, 0, 8, 6, 0, 0, 0, 0, 1,
        1, 2, 0, 0, 0, 7, 0, 5, 0,
        0, 0, 3, 7, 0, 5, 0, 2, 8,
        0, 8, 0, 0, 6, 0, 7, 0, 0,
        2, 0, 7, 0, 8, 3, 6, 1, 5
    ]
    result = check_tile(data, 0, 5)
    assert(result is True)

def test_middle_success():
    data = Sudoku()
    data.board = [
                    #
        0, 0, 0, 0, 1, 1, 0, 0, 0,
        0, 1, 2, 0, 3, 4, 5, 6, 7,
        0, 3, 4, 5, 0, 6, 1, 8, 2,
        0, 0, 1, 0, 5, 8, 2, 0, 6,
        0, 1, 8, 6, 0, 2, 0, 0, 1, # Index 40
        1, 2, 0, 0, 0, 7, 0, 5, 0,
        0, 0, 3, 7, 0, 5, 0, 2, 8,
        0, 8, 0, 0, 6, 0, 7, 0, 0,
        2, 0, 7, 0, 8, 3, 6, 1, 5
    ]
    result = check_tile(data, 40, 1)
    assert(result is True)

def test_last_success():
    data = Sudoku()
    data.board = [
                                #
        0, 0, 0, 9, 0, 1, 0, 0, 0,
        0, 1, 2, 0, 3, 4, 5, 6, 7,
        0, 3, 4, 5, 0, 6, 1, 8, 2,
        0, 0, 1, 0, 5, 8, 2, 0, 6,
        0, 0, 8, 6, 0, 0, 0, 0, 1,
        1, 2, 0, 0, 0, 7, 0, 5, 3,
        0, 0, 3, 7, 0, 5, 0, 2, 8,
        0, 8, 0, 0, 6, 3, 7, 9, 0, # Index 71
        2, 0, 7, 0, 8, 3, 6, 1, 5
    ]    
    result = check_tile(data, 71, 3)
    assert(result is True)


def test_first_fail():
    data = Sudoku()
    data.board = [
        #
        0, 0, 0, 0, 0, 0, 0, 0, 0, # Index 0
        0, 0, 2, 0, 3, 4, 5, 6, 7,
        0, 3, 4, 5, 0, 6, 1, 8, 2,
        0, 0, 1, 0, 5, 8, 2, 0, 6,
        0, 0, 8, 6, 0, 0, 0, 0, 1,
        1, 2, 0, 0, 0, 7, 0, 5, 0,
        0, 0, 3, 7, 0, 5, 0, 2, 8,
        0, 8, 0, 0, 6, 0, 7, 0, 0,
        0, 0, 7, 0, 8, 3, 6, 1, 5
    ]
    result = check_tile(data, 0, 2)
    assert(result is False)

def test_middle_fail():
    data = Sudoku()
    data.board = [
           #
        0, 0, 0, 0, 0, 1, 0, 0, 0,
        0, 1, 2, 0, 3, 4, 5, 6, 7,
        0, 3, 4, 5, 0, 6, 1, 8, 2,
        0, 0, 1, 0, 5, 8, 2, 0, 6,
        0, 0, 8, 6, 0, 0, 0, 0, 1, # Index 37
        0, 2, 9, 0, 0, 7, 0, 5, 0,
        0, 0, 3, 7, 0, 5, 0, 2, 8,
        0, 8, 0, 0, 6, 0, 7, 0, 0,
        2, 0, 7, 0, 8, 3, 6, 1, 5
    ]
    result = check_tile(data, 37, 9)
    assert(result is False)

def test_last_fail():
    data = Sudoku()
    data.board = [
                                #
        0, 0, 0, 9, 0, 1, 0, 0, 0,
        0, 1, 2, 0, 3, 4, 5, 6, 7,
        0, 3, 4, 5, 0, 6, 1, 8, 2,
        0, 0, 1, 0, 5, 8, 2, 0, 6,
        0, 0, 8, 6, 0, 0, 0, 0, 1,
        1, 2, 0, 0, 0, 7, 0, 5, 0,
        0, 0, 3, 7, 0, 5, 3, 0, 8,
        0, 8, 0, 0, 6, 0, 7, 0, 0, # Index 71
        2, 0, 7, 0, 8, 3, 6, 1, 5 
    ]    
    result = check_tile(data, 71, 3)
    assert(result is False)

