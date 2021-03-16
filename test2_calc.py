import unittest
import Calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calc.add(10,5),15)
        self.assertEqual(Calc.add(10,5),15)
        self.assertEqual(Calc.add(-1,1),0)
        self.assertEqual(Calc.add(-1,-2),-3)

if __name__ == '__main__':
    unittest.main()