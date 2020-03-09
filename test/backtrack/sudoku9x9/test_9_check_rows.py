import pytest

from src.sudoku.common.backtrack import check_rows
from src.sudoku.sudoku9x9.sudoku_gen import Sudoku

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
        0, 0, 0, 0, 0, 1, 0, 0, 0, # Index 4
        0, 1, 2, 0, 3, 4, 5, 6, 7,
        0, 3, 4, 5, 0, 6, 1, 8, 2,
        0, 0, 1, 0, 5, 8, 2, 0, 6,
        0, 0, 8, 6, 0, 0, 0, 0, 1,
        1, 2, 0, 0, 0, 7, 0, 5, 0,
        0, 0, 3, 7, 0, 5, 0, 2, 8,
        0, 8, 0, 0, 6, 0, 7, 0, 0,
        2, 0, 7, 0, 8, 3, 6, 1, 5
    ]
    result = check_rows(data, 4, 3)
    assert(result is True)

def test_middle_success():
    data = Sudoku()
    data.board = [
           #
        0, 0, 0, 0, 0, 1, 0, 0, 0,
        0, 1, 2, 0, 3, 4, 5, 6, 7,
        0, 3, 4, 5, 0, 6, 1, 8, 2,
        0, 0, 1, 0, 5, 8, 2, 0, 6,
        0, 0, 8, 6, 0, 0, 0, 0, 1, # Index 37
        1, 2, 0, 0, 0, 7, 0, 5, 0,
        0, 0, 3, 7, 0, 5, 0, 2, 8,
        0, 8, 0, 0, 6, 0, 7, 0, 0,
        2, 0, 7, 0, 8, 3, 6, 1, 5
    ]
    result = check_rows(data, 37, 2)
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
        1, 2, 0, 0, 0, 7, 0, 5, 0,
        0, 0, 3, 7, 0, 5, 0, 2, 8,
        0, 8, 0, 0, 6, 0, 7, 0, 0,
        2, 0, 7, 0, 8, 3, 6, 1, 5  # Index 75
    ]    
    result = check_rows(data, 75, 9)
    assert(result is True)


def test_first_fail():
    data = Sudoku()
    data.board = [
                    #
        0, 0, 0, 0, 0, 1, 0, 0, 0, # Index 4
        0, 1, 2, 0, 3, 4, 5, 6, 7,
        0, 3, 4, 5, 0, 6, 1, 8, 2,
        0, 0, 1, 0, 5, 8, 2, 0, 6,
        0, 0, 8, 6, 0, 0, 0, 0, 1,
        1, 2, 0, 0, 0, 7, 0, 5, 0,
        0, 0, 3, 7, 0, 5, 0, 2, 8,
        0, 8, 0, 0, 6, 0, 7, 0, 0,
        2, 0, 7, 0, 8, 3, 6, 1, 5
    ]
    result = check_rows(data, 4, 1)
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
        1, 2, 0, 0, 0, 7, 0, 5, 0,
        0, 0, 3, 7, 0, 5, 0, 2, 8,
        0, 8, 0, 0, 6, 0, 7, 0, 0,
        2, 0, 7, 0, 8, 3, 6, 1, 5
    ]
    result = check_rows(data, 37, 1)
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
        0, 0, 3, 7, 0, 5, 0, 2, 8,
        0, 8, 0, 0, 6, 0, 7, 0, 0,
        2, 0, 7, 0, 8, 3, 6, 1, 5  # Index 75
    ]    
    result = check_rows(data, 75, 5)
    assert(result is False)

