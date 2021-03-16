import unittest
import Calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calc.add(10,5),15)
        self.assertEqual(Calc.add(-1,1),0)
        self.assertEqual(Calc.add(-1,-2),-3)

    def test_subtract(self):
        self.assertEqual(Calc.subtract(10,5),5)
        self.assertEqual(Calc.subtract(-1,1),-2)
        self.assertEqual(Calc.subtract(-1,-1),0)

    def test_multiply(self):
        self.assertEqual(Calc.multiply(10,5),100000)
        self.assertEqual(Calc.multiply(-1,1),-1)
        self.assertEqual(Calc.multiply(-1,-1),-1)

    def test_divide(self):
        self.assertEqual(Calc.divide(10,5),2)
        self.assertEqual(Calc.divide(-1,1),-1)
        self.assertEqual(Calc.divide(-1,-1),1)
        self.assertEqual(Calc.divide(5,2),2.50)

        with self.assertRaises(ValueError):
            Calc.divide(10,0)

if __name__ == '__main__':
    unittest.main()