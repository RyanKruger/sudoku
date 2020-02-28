import pytest
import minisudoku

from minisudoku.utils import *

# Test decrement_array()
def test_null_value():
    data = None
    with pytest.raises(ValueError):
        result = decrement_array(data, 2)

def test_zero():
    data = [0,0,0,0]
    result = decrement_array(data, 2)
    assert(result == [0,0,0,0])

def test_max():
    data = [1,1,1,1]
    result = decrement_array(data, 2)
    assert(result == [1,1,1,0])  

def test_invalid_base():
    data = [0,0,0,0]
    with pytest.raises(ValueError):
        result = decrement_array(data,1)

def test_array_num_over_radix():
    data = [0,2,0,0]
    with pytest.raises(ValueError):
        result = decrement_array(data,2)

def test_small_array():
    data = [1]
    result = decrement_array(data,2)
    assert(result == [0])

def test_prepopulated_array():
    data = [1,0,1,1]
    result = decrement_array(data,2)
    assert(result == [1,0,1,0])

def test_base10_rollunder():
    data = [0,0,1,0]
    result = decrement_array(data,10)
    assert(result == [0,0,0,9])

def test_base10_multirollunder():
    data = [0,1,0,0]
    result = decrement_array(data,10)
    assert(result == [0,0,9,9])

def test_base2_rollunder():
    data = [0,0,1,0]
    result = decrement_array(data,2)
    assert(result == [0,0,0,1])

def test_base2_multirollunder():
    data = [1,0,0,0]
    result = decrement_array(data,2)
    assert(result == [0,1,1,1])

