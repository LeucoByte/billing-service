import unittest

from billing.proration import daily_rate_cents, prorate_cents


class ProrationTests(unittest.TestCase):
    def test_daily_rate(self):
        got = daily_rate_cents(125, 30)
        assert got == 4, f"expected 4 got {got}"

    def test_prorate_half(self):
        assert prorate_cents(3000, 15, 30) == 1500

    def test_bad_days(self):
        with self.assertRaises(ValueError):
            prorate_cents(3000, 31, 30)
