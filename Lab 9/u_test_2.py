import unittest

from Lab9 import *

#T ex kan ett test vara att kön innehåller en syntaktiskt korrekt molekyl,
# som A -> a -> 5
# (OBS! De fem funktionerna ska skrivas i nästa punkt.)
class SyntaxTest(unittest.TestCase):

    """WRONG"""

    # + : lägg till exempel

    def testWrongMolecule(self):
        self.assertEqual(check_syntax("C(Xx4)5"), "Okänd atom vid radslutet 4)5")
        self.assertEqual(check_syntax("C(OH4)C"), "Saknad siffra vid radslutet C")
        self.assertEqual(check_syntax("C(OH4C"), "Saknad högerparantes vid radslutet")
        self.assertEqual(check_syntax("H20)Fe"), "Felaktig gruppstart vid radslutet )Fe")
        self.assertEqual(check_syntax("H0"), "För litet tal vid radslutet")
        self.assertEqual(check_syntax("H1C"), "För litet tal vid radslutet C")
        self.assertEqual(check_syntax("H02C"), "För litet tal vid radslutet 2C")
        self.assertEqual(check_syntax("Nacl"), "Saknad stor bokstav vid radslutet cl")
        self.assertEqual(check_syntax("a"), "Saknad stor bokstav vid radslutet a")
        self.assertEqual(check_syntax("(C1)2)3"), "Felaktig gruppstart vid radslutet )3")
        self.assertEqual(check_syntax(")"), "Felaktig gruppstart vid radslutet )")
        self.assertEqual(check_syntax("2"), "Felaktig gruppstart vid radslutet 2")






if __name__ == '__main__':
    unittest.main()