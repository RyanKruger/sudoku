import pytest

from src.sudoku.common.backtrack import find_unassigned
from src.sudoku.sudoku4x4.sudoku_gen import Sudoku

# Test find_unassigned()
def test_null_sudoku():
    data = None
    with pytest.raises(ValueError):
        find_unassigned(data)

def test_empty_board():
    data = Sudoku()
    data.board = []
    result = find_unassigned(data)
    assert(result is None)

def test_zero():
    data = Sudoku()
    data.board = [0,0,0,0]
    result = find_unassigned(data)
    assert(result == 0)

def test_middle():
    data = Sudoku()
    data.board = [1,2,0,4]
    result = find_unassigned(data)
    assert(result == 2)

def test_none_empty():
    data = Sudoku()
    data.board = [1,2,3,4]
    result = find_unassigned(data)
    assert(result is None)



