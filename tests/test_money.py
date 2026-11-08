import unittest

from billing.money import format_cents, to_cents


class MoneyTests(unittest.TestCase):
    def test_to_cents_half_up(self):
        assert to_cents("10.005") == 1001
        assert to_cents(3) == 300

    def test_format(self):
        assert format_cents(123456) == "1234.56 EUR"
        assert format_cents(-5) == "-0.05 EUR"

    def test_div_round_half_up(self):
        from billing.money import div_round_half_up
        assert div_round_half_up(125, 30) == 4
        assert div_round_half_up(15, 10) == 2
