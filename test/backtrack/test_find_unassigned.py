import pytest

from src.sudoku.common.backtrack import find_unassigned

# Test find_unassigned()
def test_null_board():
    data = None
    with pytest.raises(ValueError):
        result = find_unassigned(data)

def test_empty_board():
    data = []
    result = find_unassigned(data)
    assert(result is None)

def test_zero():
    data = [0,0,0,0]
    result = find_unassigned(data)
    assert(result == 0)

def test_middle():
    data = [1,2,0,4]
    result = find_unassigned(data)
    assert(result == 2)

def test_none_empty():
    data = [1,2,3,4]
    result = find_unassigned(data)
    assert(result is None)



