import unittest
from pyCalc.Operation import Operation


class MyTestCase(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(Operation.convert("+"), Operation.ADD)

    def testSub(self):
        self.assertEqual(Operation.convert("-"), Operation.SUB)

    def testDiv(self):
        self.assertEqual(Operation.convert("/"), Operation.DIV)

    def testMul(self):
        self.assertEqual(Operation.convert("*"), Operation.MUL)


if __name__ == '__main__':
    unittest.main()
