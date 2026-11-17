import unittest

from billing.discounts import apply_discount_cents, volume_discount_percent


class DiscountTests(unittest.TestCase):
    def test_tiers(self):
        assert volume_discount_percent(1) == 0
        assert volume_discount_percent(10) == 5
        assert volume_discount_percent(99) == 10
        assert volume_discount_percent(100) == 15

    def test_full_discount(self):
        assert apply_discount_cents(1000, 100) == 0
        assert apply_discount_cents(0, 15) == 0
