import unittest
import calculator

class TestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator.addition(9,1), 10)
        self.assertEqual(calculator.addition(-10,5), -5)
        self.assertEqual(calculator.addition(-3,0), -3)
        self.assertEqual(calculator.addition(10.5,3), 13.5)

    def test_subtraction(self):
        self.assertEqual(calculator.subtraction(1,1), 0)
        self.assertEqual(calculator.subtraction(20,10), 10)
        self.assertEqual(calculator.subtraction(-10,10), -20)
        self.assertEqual(calculator.subtraction(5,2.5), 2.5)

    def test_multiplication(self):
        self.assertEqual(calculator.multiplication(10,10), 100)
        self.assertEqual(calculator.multiplication(-5,-5), 25)
        self.assertEqual(calculator.multiplication(20,-5), -100)
        self.assertEqual(calculator.multiplication(2.5,10), 25)

    def test_division(self):
        self.assertEqual(calculator.division(10,2.5), 4)
        self.assertEqual(calculator.division(100,0), None)
        self.assertEqual(calculator.division(-10,5), -2)
        self.assertEqual(calculator.division(16,4), 4)

       

if __name__ == '__main__':
    unittest.main()