import pytest

from sudoku.backtrack import is_good_fit


# Test is_good_fit()
def test_null_board():
    data = None
    with pytest.raises(ValueError):
        result = find_unassigned(data)

def test_row_fail():
    data = [
        #
        0, 0, 0, 0, 0, 0, 0, 0, 0
        0, 1, 2, 0, 3, 4, 5, 6, 7 # Index 9
        0, 3, 4, 5, 0, 6, 1, 8, 2
        0, 0, 1, 0, 5, 8, 2, 0, 6
        0, 0, 8, 6, 0, 0, 0, 0, 1
        0, 2, 0, 0, 0, 7, 0, 5, 0
        0, 0, 3, 7, 0, 5, 0, 2, 8
        0, 8, 0, 0, 6, 0, 7, 0, 0
        2, 0, 7, 0, 8, 3, 6, 1, 5
    ]
    result = is_good_fit(data, 9, 7)
    assert(result is False)

def test_col_fail():
    data = [
        #
        0, 0, 0, 0, 0, 0, 0, 0, 0
        0, 1, 2, 0, 3, 4, 5, 6, 7
        0, 3, 4, 5, 0, 6, 1, 8, 2
        0, 0, 1, 0, 5, 8, 2, 0, 6
        0, 0, 8, 6, 0, 0, 0, 0, 1 # Index 36
        0, 2, 0, 0, 0, 7, 0, 5, 0
        0, 0, 3, 7, 0, 5, 0, 2, 8
        0, 8, 0, 0, 6, 0, 7, 0, 0
        2, 0, 7, 0, 8, 3, 6, 1, 5
    ]
    result = is_good_fit(data, 36, 2)
    assert(result is False)

def test_first_tile_fail():
    data = [
        #
        0, 0, 0, 0, 0, 1, 0, 0, 0 # Index 0
        0, 1, 2, 0, 3, 4, 5, 6, 7
        0, 3, 4, 5, 0, 6, 1, 8, 2
        0, 0, 1, 0, 5, 8, 2, 0, 6
        0, 0, 8, 6, 0, 0, 0, 0, 1
        1, 2, 0, 0, 0, 7, 0, 5, 0
        0, 0, 3, 7, 0, 5, 0, 2, 8
        0, 8, 0, 0, 6, 0, 7, 0, 0
        2, 0, 7, 0, 8, 3, 6, 1, 5
    ]
    result = is_good_fit(data, 0, 1)
    assert(result is False)

def test_fifth_tile_fail():
    data = [
                    #
        0, 0, 0, 0, 0, 1, 0, 0, 0
        0, 1, 2, 0, 3, 4, 5, 6, 7
        0, 3, 4, 5, 0, 6, 1, 8, 2
        0, 0, 1, 0, 5, 8, 2, 0, 6
        6, 0, 8, 6, 0, 0, 0, 0, 1 # Index 40
        1, 2, 0, 0, 0, 7, 0, 5, 0
        0, 0, 3, 7, 0, 5, 0, 2, 8
        0, 8, 0, 0, 6, 0, 7, 0, 0
        2, 0, 7, 0, 8, 3, 6, 1, 5
    ]
    result = is_good_fit(data, 40, 6)
    assert(result is False)

def test_first_tile_success():
    data = [
        #
        0, 0, 0, 0, 0, 1, 0, 0, 0 # Index 0
        0, 1, 2, 0, 3, 4, 5, 6, 7
        0, 3, 4, 5, 0, 6, 1, 8, 2
        0, 0, 1, 0, 5, 8, 2, 0, 6
        0, 0, 8, 6, 0, 0, 0, 0, 1
        1, 2, 0, 0, 0, 7, 0, 5, 0
        0, 0, 3, 7, 0, 5, 0, 2, 8
        0, 8, 0, 0, 6, 0, 7, 0, 0
        2, 0, 7, 0, 8, 3, 6, 1, 5
    ]
    result = is_good_fit(data, 0, 5)
    assert(result is True)

def test_fifth_tile_fail():
    data = [
                    #
        0, 0, 0, 0, 0, 1, 0, 0, 0
        0, 1, 2, 0, 3, 4, 5, 6, 7
        0, 3, 4, 5, 0, 6, 1, 8, 2
        0, 0, 1, 0, 5, 8, 2, 0, 6
        6, 0, 8, 6, 0, 0, 0, 0, 1 # Index 40
        1, 2, 0, 0, 0, 7, 0, 5, 0
        0, 0, 3, 7, 0, 5, 0, 2, 8
        0, 8, 0, 0, 6, 0, 7, 0, 0
        2, 0, 7, 0, 8, 3, 6, 1, 5
    ]
    result = is_good_fit(data, 40, 2)
    assert(result is True)
