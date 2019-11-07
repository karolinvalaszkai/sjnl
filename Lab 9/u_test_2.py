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

    def testWrongMolecule2(self):
        self.assertEqual(check_syntax("C(OH4)C"), "Saknad siffra vid radslutet C")

    def testWrongMolecule3(self):
        self.assertEqual(check_syntax("C(OH4C"), "Saknad högerparentes vid radslutet")

    def testWrongMolecule4(self):
        self.assertEqual(check_syntax("H2O)Fe"), "Felaktig gruppstart vid radslutet )Fe")

    def testWrongMolecule5(self):
        self.assertEqual(check_syntax("H0"), "För litet tal vid radslutet")

    def testWrongMolecule6(self):
        self.assertEqual(check_syntax("H1C"), "För litet tal vid radslutet C")

    def testWrongMolecule7(self):
        self.assertEqual(check_syntax("H02C"), "För litet tal vid radslutet 2C")

    def testWrongMolecule8(self):
        self.assertEqual(check_syntax("Nacl"), "Saknad stor bokstav vid radslutet cl")

    def testWrongMolecule9(self):
        self.assertEqual(check_syntax("a"), "Saknad stor bokstav vid radslutet a")

    def testWrongMolecule10(self):
        self.assertEqual(check_syntax("(Cl)2)3"), "Felaktig gruppstart vid radslutet )3")

    def testWrongMolecule11(self):
        self.assertEqual(check_syntax(")"), "Felaktig gruppstart vid radslutet )")

    def testWrongMolecule12(self):
        self.assertEqual(check_syntax("2"), "Felaktig gruppstart vid radslutet 2")


if __name__ == '__main__':
    unittest.main()