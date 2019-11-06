import unittest

from Lab9 import *

#T ex kan ett test vara att kön innehåller en syntaktiskt korrekt molekyl,
# som A -> a -> 5
# (OBS! De fem funktionerna ska skrivas i nästa punkt.)
class SyntaxTest(unittest.TestCase):


    """CORRECT"""

    def testCorrectMolecule(self):
        self.assertEqual(check_syntax("Na"), "Formeln är syntastiskt korrekt")
        self.assertEqual(check_syntax("H20"), "Formeln är syntastiskt korrekt")
        self.assertEqual(check_syntax("Si(C3(COOH)2)4(H20)7"), "Formeln är syntastiskt korrekt")
        self.assertEqual(check_syntax("Na332"), "Formeln är syntastiskt korrekt")



if __name__ == '__main__':
    unittest.main()