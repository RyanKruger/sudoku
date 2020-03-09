import pytest

from src.sudoku.common.backtrack import is_good_fit
from src.sudoku.sudoku4x4.sudoku_gen import Sudoku

# Test is_good_fit()
def test_null_sudoku():
    data = None
    with pytest.raises(ValueError):
        is_good_fit(data, 0, 0)

def test_empty_board():
    data = Sudoku()
    data.board = []
    with pytest.raises(ValueError):
        is_good_fit(data, 0, 0)

def test_row_fail():
    data = Sudoku()
    data.board = [
        0,2,3,4,
        3,4,1,2,
        2,3,4,1,
        4,1,2,3
    ]
    result = is_good_fit(data, 0, 2)
    assert(result is False)

def test_col_fail():
    data = Sudoku()
    data.board = [
        0,2,3,4,
        3,4,1,2,
        2,3,4,1,
        4,1,2,3
    ]
    result = is_good_fit(data, 0, 4)
    assert(result is False)

def test_first_tile_fail():
    data = Sudoku()
    data.board = [
        1,2,3,4,
        3,0,1,2,
        2,3,4,1,
        4,1,2,3
    ]
    result = is_good_fit(data, 5, 1)
    assert(result is False)

def test_fourth_tile_fail():
    data = Sudoku()
    data.board = [
        1,2,3,4,
        3,4,1,0,
        2,3,2,1,
        4,1,0,0
    ]
    result = is_good_fit(data, 15, 2)
    assert(result is False)

def test_first_tile_success():
    data = Sudoku()
    data.board = [
        1,2,3,4,
        0,4,1,2,
        2,3,4,1,
        4,1,2,3
    ]
    result = is_good_fit(data, 4, 3)
    assert(result is True)

def test_fourth_tile_success():
    data = Sudoku()
    data.board = [
        1,2,3,4,
        3,4,1,2,
        2,3,4,1,
        4,1,0,3
    ]
    result = is_good_fit(data, 14, 2)
    assert(result is True)
