import pytest

from utils import increment_array

# Test increment_array()
def test_null_value():
    data = None
    with pytest.raises(ValueError):
        result = increment_array(data, 2)

def test_zero():
    data = [0,0,0,0]
    result = increment_array(data, 2)
    assert(result == [0,0,0,1])

def test_max():
    data = [1,1,1,1]
    result = increment_array(data, 2)
    assert(result == [1,1,1,1])        

def test_invalid_base():
    data = [0,0,0,0]
    with pytest.raises(ValueError):
        result = increment_array(data,1)

def test_array_num_over_radix():
    data = [0,2,0,0]
    with pytest.raises(ValueError):
        result = increment_array(data,2)

def test_small_array():
    data = [0]
    result = increment_array(data,2)
    assert(result == [1])

def test_prepopulated_array():
    data = [1,0,0,0]
    result = increment_array(data,2)
    assert(result == [1,0,0,1])

def test_base10_rollover():
    data = [0,0,0,9]
    result = increment_array(data,10)
    assert(result == [0,0,1,0])

def test_base10_multirollover():
    data = [0,9,9,9]
    result = increment_array(data,10)
    assert(result == [1,0,0,0])

def test_base2_rollover():
    data = [0,0,0,1]
    result = increment_array(data,2)
    assert(result == [0,0,1,0])

def test_base2_multirollover():
    data = [0,1,1,1]
    result = increment_array(data,2)
    assert(result == [1,0,0,0])

    
