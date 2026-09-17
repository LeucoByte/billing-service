import unittest

from billing.tax import rate_for, tax_cents


class TaxTests(unittest.TestCase):
    def test_rates(self):
        assert rate_for("es") == 21
        with self.assertRaises(ValueError):
            rate_for("XX")

    def test_rounding(self):
        assert tax_cents(1000, "ES") == 210
        assert tax_cents(1, "ES") == 0
        assert tax_cents(3, "DE") == 1
