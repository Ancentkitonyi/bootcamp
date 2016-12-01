import unittest
from is_prime import is_prime

class TestCalculator(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(is_prime(5), 'is a prime number')
    def test_negative(self):
        self.assertEqual(is_prime(-5), False)
    def test_zero_non_prime(self):
        self.assertEqual(is_prime(0), False)
    def test_string(self):
        self.assertEqual(is_prime('jj'), False) 
    def test_list(self):
        self.assertEqual(is_prime([6,7]), False)
    def test_dictionary(self):
        self.assertEqual(is_prime({'hhhh':8}), False)
    def test_float(self):
        self.assertEqual(is_prime(7.7), False)
    def test_is_prime(self):
        self.assertEqual(is_prime(2), 'is a prime number')
    def test_is_prime(self):
        self.assertEqual(is_prime(1), False)
    def test_is_prime(self):
        self.assertEqual(is_prime(1000), False)
    def test_not_boolen(self):
        self.assertEqual(is_prime(True), False)
    def test_is_7_prime(self):
        self.assertEqual(is_prime(7), 'is a prime number')
    def test_is_3_prime(self):
        self.assertEqual(is_prime(3), 'is a prime number')
    
    
if __name__ == '__main__':
	unittest.main()
