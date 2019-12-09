import unittest
from main import *

class TestArrayValueGenerating(unittest.TestCase):

    def test_diagonala(self):
        """Sprawdza diagonalę. Zawsze równe trzy."""
        self.assertEqual(a(0, 0), 3)
        self.assertEqual(a(1, 1), 3)
        self.assertEqual(a(8, 8), 3)
        self.assertEqual(a(5, 5), 3)
        self.assertEqual(a(88, 88), 3)

    def test_srodek(self):
        """
        Sprawdza wartości tam, gdzie nie ucina z brzegu.

        Takie coś następuje w wierszach od 2 do N-2.
        """
        self.assertEqual(a(2, 0), 0.2)
        self.assertEqual(a(3, 1), 0.2)
        self.assertEqual(a(3, 5), 0.2)
        self.assertEqual(a(98, 96), 0.2)
        self.assertEqual(a(98, 100), 0.2)
        self.assertEqual(a(34, 32), 0.2)
        self.assertEqual(a(34, 33), 1)
        self.assertEqual(a(34, 35), 1)
        self.assertEqual(a(34, 36), 0.2)

    def test_pierwszy_wiersz(self):
        self.assertEqual(a(0, 0), 3)
        self.assertEqual(a(0, 1), 1)
        self.assertEqual(a(0, 2), 0.2)

    def test_ostatni_wiersz(self):
        self.assertEqual(a(7, 5), 0.2)
        self.assertEqual(a(7, 6), 1)
        self.assertEqual(a(7, 7), 3)

    def test_przedostatni_wiersz(self):
        self.assertEqual(a(6, 4), 0.2)
        self.assertEqual(a(6, 5), 1)
        self.assertEqual(a(6, 6), 3)
        self.assertEqual(a(6, 7), 1)

    def test_N_minus_trzeci_wiersz(self):
        self.assertEqual(a(5, 3), 0.2)
        self.assertEqual(a(5, 4), 1)
        self.assertEqual(a(5, 5), 3)
        self.assertEqual(a(5, 6), 1)
        self.assertEqual(a(5, 7), 0.2)

class TestBGeneration(unittest.TestCase):

    def test_all(self):
        self.assertEqual(b(5), 5)
        self.assertEqual(b(2), 2)
        self.assertEqual(b(100), 100)

if __name__ == '__main__':
    unittest.main()
