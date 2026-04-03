import unittest
from converter import usd_to_eur


class TestUsdToEur(unittest.TestCase):
    def test_basic_conversion(self):
        self.assertAlmostEqual(usd_to_eur(100), 92.0)

    def test_zero(self):
        self.assertEqual(usd_to_eur(0), 0.0)

    def test_small_amount(self):
        self.assertAlmostEqual(usd_to_eur(1), 0.92)

    def test_rounding(self):
        self.assertAlmostEqual(usd_to_eur(10.555), 9.71)

    def test_negative_amount(self):
        self.assertAlmostEqual(usd_to_eur(-50), -46.0)


if __name__ == "__main__":
    unittest.main()
