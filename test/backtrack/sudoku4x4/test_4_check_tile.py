import pytest

from src.sudoku.common.backtrack import check_tile, ElementNotFoundError
from src.sudoku.sudoku4x4.sudoku_gen import Sudoku

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
        0,2,1,4, # Index 0
        3,4,1,2,
        1,3,4,1,
        4,1,2,3
    ]
    result = check_tile(data, 0, 1)
    assert(result is True)

def test_middle_success():
    data = Sudoku()
    data.board = [
            #
        1,2,3,4,
        3,2,0,1, # Index 6
        2,3,4,1,
        4,1,2,3
    ]
    result = check_tile(data, 6, 2)
    assert(result is True)

def test_last_success():
    data = Sudoku()
    data.board = [
              #
        1,2,3,4,
        3,4,1,2,
        2,3,4,1,
        4,2,3,0  # Index 15
    ]    
    result = check_tile(data, 15, 2)
    assert(result is True)


def test_first_fail():
    data = Sudoku()
    data.board = [
        #
        0,2,3,4, # Index 0
        3,1,1,2,
        2,3,4,1,
        4,1,2,3
    ]
    result = check_tile(data, 0, 1)
    assert(result is False)

def test_middle_fail():
    data = Sudoku()
    data.board = [
              #
        1,2,2,0, # Index 3
        3,4,3,2,
        2,3,4,1,
        4,1,2,0
    ]
    result = check_tile(data, 3, 3)
    assert(result is False)

def test_last_fail():
    data = Sudoku()
    data.board = [
            #
        1,2,3,4,
        3,4,1,2,
        2,3,0,2,
        4,1,0,3  # Index 14   
    ]    
    result = check_tile(data, 14, 2)
    assert(result is False)

