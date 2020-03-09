import pytest

from src.sudoku.common.backtrack import check_rows
from src.sudoku.sudoku4x4.sudoku_gen import Sudoku

# Test check_rows()
def test_null_sudoku():
    data = None
    with pytest.raises(ValueError):
        check_rows(data, 0, 0)

def test_empty_board():
    data = Sudoku()
    data.board = []
    with pytest.raises(ValueError):
        check_rows(data, 0, 0)

def test_first_success():
    data = Sudoku()
    data.board = [
        #
        0,2,3,4, # Index 0
        3,1,1,2,
        1,3,4,1,
        4,1,2,3
    ]
    result = check_rows(data, 0, 1)
    assert(result is True)

def test_middle_success():
    data = Sudoku()
    data.board = [
            #
        1,2,3,2,
        3,4,0,1, # Index 6
        2,3,4,1,
        4,1,2,3
    ]
    result = check_rows(data, 6, 2)
    assert(result is True)

def test_last_success():
    data = Sudoku()
    data.board = [
              #
        1,2,3,4,
        3,4,1,3,
        2,3,3,1,
        4,1,2,0  # Index 15
    ]    
    result = check_rows(data, 15, 3)
    assert(result is True)


def test_first_fail():
    data = Sudoku()
    data.board = [
        #
        0,2,3,1, # Index 0
        3,4,1,2,
        0,3,4,1,
        4,1,2,3
    ]
    result = check_rows(data, 0, 1)
    assert(result is False)

def test_middle_fail():
    data = Sudoku()
    data.board = [
              #
        1,3,2,0, # Index 3
        3,4,1,2,
        2,3,4,1,
        4,1,2,0
    ]
    result = check_rows(data, 3, 3)
    assert(result is False)

def test_last_fail():
    data = Sudoku()
    data.board = [
            #
        1,2,3,4,
        3,4,1,2,
        2,3,4,1,
        4,2,0,3  # Index 14   
    ]    
    result = check_rows(data, 14, 2)
    assert(result is False)

