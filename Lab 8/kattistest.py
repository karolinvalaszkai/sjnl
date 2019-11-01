import unittest

from Lab8 import *

#T ex kan ett test vara att kön innehåller en syntaktiskt korrekt molekyl,
# som A -> a -> 5




class SyntaxTest(unittest.TestCase):

    """CORRECT/WRONG"""


    def testCorrectMolecule(self):
        self.assertEqual(check_syntax("H2"), "Formeln är syntastiskt korrekt")
        self.assertEqual(check_syntax("P21"), "Formeln är syntastiskt korrekt")
        self.assertEqual(check_syntax("Ag3"), "Formeln är syntastiskt korrekt")
        self.assertEqual(check_syntax("Fe12"), "Formeln är syntastiskt korrekt")
        self.assertEqual(check_syntax("Xx5"), "Formeln är syntastiskt korrekt")



    def testWrongUPC(self):
        self.assertEqual(check_syntax("a"), "Fel, borde vara uppercase: a")
        self.assertEqual(check_syntax("cr12"), "Fel, borde vara uppercase: c")
        self.assertEqual(check_syntax("8"), "Fel, borde vara uppercase: 8")


    def testWrongNum(self):
        self.assertEqual(check_syntax("Cr0"), "För litet tal vid radslutet")
        self.assertEqual(check_syntax("Pb1"), "För litet tal vid radslutet")






if __name__ == '__main__':
    unittest.main()