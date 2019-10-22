import unittest

from Lab8 import *

#T ex kan ett test vara att kön innehåller en syntaktiskt korrekt molekyl,
# som A -> a -> 5
# (OBS! De fem funktionerna ska skrivas i nästa punkt.)
class SyntaxTest(unittest.TestCase):

    """CORRECT/WRONG"""

    """MOLECULE"""
    # < molekyl >::= < atom > | < atom > < num >

    def testCorrectMolecule(self):
        self.assertEqual(check_syntax("H2"), "Formeln är syntastiskt korrekt")
        self.assertEqual(check_syntax("P21"), "Formeln är syntastiskt korrekt")
        self.assertEqual(check_syntax("Ag3"), "Formeln är syntastiskt korrekt")
        self.assertEqual(check_syntax("Fe12"), "Formeln är syntastiskt korrekt")
        self.assertEqual(check_syntax("Xx5"), "Formeln är syntastiskt korrekt")


    # def testWrongMolecule(self):
    #     self.assertEqual(check_syntax("a"), "Saknad stor bokstav")


    """ATOM"""
    #< atom >::= < LETTER > | < LETTER > < letter >

    # def testCorrectAtom(self):
    #     self.assertEqual(check_syntax("P21"), "Formeln är syntastiskt korrekt")
    #
    # def testWrongAtom(self):
    #     self.assertEqual(check_syntax("cr12"), "Saknad stor bokstav")


    """UPPER CASE LETTER"""
    #< LETTER >::= A | B | C | ... | Z

    # def testCorrectUPC(self):
    #     self.assertEqual(check_syntax("Ag3"), "Formeln är syntastiskt korrekt")

    def testWrongUPC(self):
        self.assertEqual(check_syntax("a"), "Fel, borde vara uppercase: ")
        self.assertEqual(check_syntax("cr12"), "Fel, borde vara uppercase: ")
        self.assertEqual(check_syntax("8"), "Fel, borde vara uppercase: ")



    """LOWER CASE LETTER"""
    #< letter >::= a | b | c | ... | z

    # def testCorrectLPC(self):
    #     self.assertEqual(check_syntax("Fe12"), "Formeln är syntastiskt korrekt")
    #
    # def testWrongLPC(self):
    #     self.assertEqual(check_syntax("Cr0"), "Fel, borde vara lowercase: ")


    """NUMBER"""
    #< num >::= 2 | 3 | 4 | ...

    # def testCorrectNum(self):
    #     self.assertEqual(check_syntax("Xx5"), "Formeln är syntastiskt korrekt")

    def testWrongNum(self):
        self.assertEqual(check_syntax("Cr0"), "För litet tal vid radslutet")
        self.assertEqual(check_syntax("Pb1"), "För litet tal vid radslutet")






if __name__ == '__main__':
    unittest.main()