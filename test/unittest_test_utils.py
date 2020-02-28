import unittest
import minisudoku

from minisudoku.utils import *

class TestIncrement(unittest.TestCase):
    def test_null_value(self):
        data = None
        with self.assertRaises(ValueError):
            result = increment_array(data, 2)
    
    def test_zero(self):
        data = [0,0,0,0]
        result = increment_array(data, 2)
        self.assertEqual(result, [0,0,0,1])

    def test_max(self):
        data = [1,1,1,1]
        result = increment_array(data, 2)
        self.assertEqual(result, [1,1,1,1])        

    def test_invalid_base(self):
        data = [0,0,0,0]
        with self.assertRaises(ValueError):
            result = increment_array(data,1)

    def test_array_num_over_radix(self):
        data = [0,2,0,0]
        with self.assertRaises(ValueError):
            result = increment_array(data,2)

    def test_small_array(self):
        data = [0]
        result = increment_array(data,2)
        self.assertEqual(result, [1])

    def test_prepopulated_array(self):
        data = [1,0,0,0]
        result = increment_array(data,2)
        self.assertEqual(result, [1,0,0,1])

    def test_base10_rollover(self):
        data = [0,0,0,9]
        result = increment_array(data,10)
        self.assertEqual(result, [0,0,1,0])

    def test_base10_multirollover(self):
        data = [0,9,9,9]
        result = increment_array(data,10)
        self.assertEqual(result, [1,0,0,0])

    def test_base2_rollover(self):
        data = [0,0,0,1]
        result = increment_array(data,2)
        self.assertEqual(result, [0,0,1,0])

    def test_base2_multirollover(self):
        data = [0,1,1,1]
        result = increment_array(data,2)
        self.assertEqual(result, [1,0,0,0])

    
class TestDecrement(unittest.TestCase):
    def test_null_value(self):
        data = None
        with self.assertRaises(ValueError):
            result = decrement_array(data, 2)

    def test_zero(self):
        data = [0,0,0,0]
        result = decrement_array(data, 2)
        self.assertEqual(result, [0,0,0,0])

    def test_max(self):
        data = [1,1,1,1]
        result = decrement_array(data, 2)
        self.assertEqual(result, [1,1,1,0])  

    def test_invalid_base(self):
        data = [0,0,0,0]
        with self.assertRaises(ValueError):
            result = decrement_array(data,1)

    def test_array_num_over_radix(self):
        data = [0,2,0,0]
        with self.assertRaises(ValueError):
            result = decrement_array(data,2)

    def test_small_array(self):
        data = [1]
        result = decrement_array(data,2)
        self.assertEqual(result, [0])

    def test_prepopulated_array(self):
        data = [1,0,1,1]
        result = decrement_array(data,2)
        self.assertEqual(result, [1,0,1,0])

    def test_base10_rollunder(self):
        data = [0,0,1,0]
        result = decrement_array(data,10)
        self.assertEqual(result, [0,0,0,9])

    def test_base10_multirollunder(self):
        data = [0,1,0,0]
        result = decrement_array(data,10)
        self.assertEqual(result, [0,0,9,9])

    def test_base2_rollunder(self):
        data = [0,0,1,0]
        result = decrement_array(data,2)
        self.assertEqual(result, [0,0,0,1])

    def test_base2_multirollunder(self):
        data = [1,0,0,0]
        result = decrement_array(data,2)
        self.assertEqual(result, [0,1,1,1])
    

    
    

if __name__ == "__main__":
    unittest.main()