import pytest

from src.sudoku.common.backtrack import check_cols
from src.sudoku.sudoku4x4.sudoku_gen import Sudoku

# Test check_cols()
def test_null_sudoku():
    data = None
    with pytest.raises(ValueError):
        check_cols(data, 0, 0)

def test_empty_board():
    data = Sudoku()
    data.board = []
    with pytest.raises(ValueError):
        check_cols(data, 0, 0)

def test_first_success():
    data = Sudoku()
    data.board = [
        #
        0,2,1,4, # Index 0
        3,1,1,2,
        2,3,4,1,
        4,1,2,3
    ]
    result = check_cols(data, 0, 1)
    assert(result is True)

def test_middle_success():
    data = Sudoku()
    data.board = [
            #
        1,2,3,4,
        3,4,0,1, # Index 6
        2,3,4,1,
        4,1,2,3
    ]
    result = check_cols(data, 6, 1)
    assert(result is True)

def test_last_success():
    data = Sudoku()
    data.board = [
              #
        1,2,3,4,
        3,4,1,2,
        2,3,4,1,
        4,1,3,0  # Index 15
    ]    
    result = check_cols(data, 15, 3)
    assert(result is True)


def test_first_fail():
    data = Sudoku()
    data.board = [
        #
        0,2,3,4, # Index 0
        3,4,1,2,
        1,3,4,1,
        4,1,2,3
    ]
    result = check_cols(data, 0, 1)
    assert(result is False)

def test_middle_fail():
    data = Sudoku()
    data.board = [
              #
        1,2,2,0, # Index 3
        3,4,1,2,
        2,3,4,1,
        4,1,2,3
    ]
    result = check_cols(data, 3, 3)
    assert(result is False)

def test_last_fail():
    data = Sudoku()
    data.board = [
            #
        1,2,3,4,
        3,4,2,2,
        2,3,4,1,
        4,1,0,3  # Index 14   
    ]    
    result = check_cols(data, 14, 2)
    assert(result is False)

