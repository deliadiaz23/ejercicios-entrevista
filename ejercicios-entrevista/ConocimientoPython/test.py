import unittest
from main import word_counter

class TestWordCounting(unittest.TestCase):

    def test_no_string(self):    
        result = word_counter(20)
        self.assertEqual(result, "Esta función solo recibe Strings")
    
    def test_successful_result(self):
        result = word_counter("hace mucho tiempo en lugar en mucho mucho calor tiempo")
        self.assertEqual(isinstance(result, list), True)

        expected_result = [("mucho", 3), ("tiempo", 2), ("en", 2), ("hace", 1), ("lugar", 1), ("calor", 1)]
        self.assertCountEqual(result, expected_result)
    
    def test_successful_order_result(self):
        result = word_counter("mucho tiempo mucho mucho calor tiempo")
        self.assertEqual(isinstance(result, list), True)

        expected_result = [("mucho", 3), ("tiempo", 2), ("calor", 1)]
        self.assertSequenceEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()