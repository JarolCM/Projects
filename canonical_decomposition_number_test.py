import unittest
from canonical import primes_until, decomposition


class PrimesUntilTest(unittest.TestCase):

    def test_primes_until_8(self):
        expected = [2, 3, 5, 7]
        result = primes_until(8)
        self.assertEqual(result, expected)

    def test_primes_until_10(self):
        expected = [2, 3, 5, 7]
        result = primes_until(10)
        self.assertEqual(result, expected)

    def test_primes_until_20(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19]
        result = primes_until(20)
        self.assertEqual(result, expected)

    def test_primes_until_50(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        result = primes_until(50)
        self.assertEqual(result, expected)

class DecompositionTest(unittest.TestCase):

    def test_decomposition_24(self):
        expected = "24 es descompuesto por: 2 ^ 3 x 3 ^ 1"
        result = decomposition(24)
        self.assertEqual(result, expected)

    def test_decomposition_90(self):
        expected = "90 es descompuesto por: 2 ^ 1 x 3 ^ 2 x 5 ^ 1"
        result = decomposition(90)
        self.assertEqual(result, expected)

    def test_decomposition_100(self):
        expected = "100 es descompuesto por: 2 ^ 2 x 5 ^ 2"
        result = decomposition(100)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()