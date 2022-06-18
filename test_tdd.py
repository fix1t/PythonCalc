from logging import exception
import mathlib
import unittest

class test_addition(unittest.TestCase):
    def test_addition_integer(self):
        self.assertEqual(mathlib.addition(5,0),5)
        self.assertEqual(mathlib.addition(5,-10),-5)
        self.assertEqual(mathlib.addition(-5,-10),-15)

    def test_addition_float(self):
        self.assertAlmostEquals(mathlib.addition(5.5,0),5.5)
        self.assertAlmostEquals(mathlib.addition(5.2,-10.4),-5.2)
        self.assertAlmostEquals(mathlib.addition(-5.1,-10.8),-15.9)

class test_subtraction(unittest.TestCase):
    def test_subtraction_integer(self):
        self.assertEqual(mathlib.subtraction(5,10),-5)
        self.assertEqual(mathlib.subtraction(5,-10),15)
        self.assertEqual(mathlib.subtraction(-5,-10),5)

    def test_subtraction_float(self):
        self.assertAlmostEquals(mathlib.subtraction(5.5,0),5.5)
        self.assertAlmostEquals(mathlib.subtraction(5.2,-10.4),15.6)
        self.assertAlmostEquals(mathlib.subtraction(-5.1,10.8),-15.9)

class test_multiplication(unittest.TestCase):
    def test_multiplication_integer(self):
        self.assertEqual(mathlib.multiplication(5,10),50)
        self.assertEqual(mathlib.multiplication(5,-10),-50) 
        self.assertEqual(mathlib.multiplication(-5,-10),50)

    def test_multiplication_float(self):
        self.assertAlmostEquals(mathlib.multiplication(5.5,0),0)
        self.assertAlmostEquals(mathlib.multiplication(5.2,-10.4),-54.08)
        self.assertAlmostEquals(mathlib.multiplication(-5.1,-10.8),55.08)


class test_division(unittest.TestCase):
    def test_division_integer(self):
        self.assertAlmostEqual(mathlib.division(5,10),0.5)
        self.assertAlmostEquals(mathlib.division(5,-10),-0.5) 
        self.assertAlmostEquals(mathlib.division(-5,-10),0.5)

    def test_division_float(self):
        self.assertAlmostEquals(mathlib.division(5.2,-10.4),-0.5)
        self.assertAlmostEquals(mathlib.division(0,-10.4),0)
        self.assertAlmostEquals(mathlib.division(-5.1,-10.8),0.472222222)

    def test_div_division_by_zero(self):
        with self.assertRaises(ValueError):
            mathlib.division(10, 0)
        with self.assertRaises(ValueError):
            mathlib.division(10, 0.0)

class test_factorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(mathlib.factorial(5),120)
        self.assertEqual(mathlib.factorial(10),3628800)
        self.assertEqual(mathlib.factorial(15),1307674368000)
        self.assertEqual(mathlib.factorial(0),0)


    def test_factorial_failure_states(self):
        with self.assertRaises(ValueError):
            mathlib.factorial(1.1)
        with self.assertRaises(ValueError):
            mathlib.factorial(-5)

class test_power(unittest.TestCase):
    def test_power(self):
        self.assertEqual(mathlib.power(2,2),4)
        self.assertEqual(mathlib.power(2,8),256)
        self.assertEqual(mathlib.power(2,0),1)
        self.assertEqual(mathlib.power(4,2),16)

    def test_power_hard(self):
        self.assertEqual(mathlib.power(-2,3),-8)
        self.assertEqual(mathlib.power(0,8),0)
        self.assertEqual(mathlib.power(-4,2),16)
        self.assertAlmostEquals(mathlib.power(-3.3,2),10.89)

class test_root(unittest.TestCase):
    def test_root(self):
        self.assertEqual(mathlib.root(0,2),0)
        self.assertEqual(mathlib.root(4,2),2)
        self.assertEqual(mathlib.root(8,3),2)
        self.assertEqual(mathlib.root(64,2),8)
        self.assertEqual(mathlib.root(64,6),2)

    def test_root_hard(self):
        self.assertAlmostEqual(mathlib.root(5,5),1.379729661)
        self.assertAlmostEqual(mathlib.root(-64,3),-4)
        self.assertAlmostEqual(mathlib.root(-64,-3),-0.25)


    def test_factorial_failure_states(self):
        with self.assertRaises(ValueError):
            mathlib.root(-64,4)



# shorten python -m unittest tdd.py 
# allows to start test running only tdd.py
if __name__ == '__main__':
    unittest.main()