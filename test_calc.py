import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-5, 4), -1)
        self.assertEqual(calc.add(-5, -5), -10)
        
    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-5, -5), 0)
        self.assertEqual(calc.subtract(-5, 4), -9)
        
    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 3), 6)
        self.assertEqual(calc.multiply(-5, -5), 25)
        self.assertEqual(calc.multiply(-5, 2), -10)
        
    def test_divide(self):
        self.assertEqual(calc.divide(10, 2), 5)
        self.assertEqual(calc.divide(-10, -5), 2)
        self.assertEqual(calc.divide(-10, 5), -2)
        
        with self.assertRaises(ValueError):
            calc.divide(10, 0)
        
        
if __name__ == '__main__':
    unittest.main()