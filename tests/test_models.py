import unittest

from billing.models import Invoice, LineItem


class ModelTests(unittest.TestCase):
    def test_totals(self):
        inv = Invoice("2024-0001", "a@example.com", "ES",
                      items=[LineItem("Pro plan", 1000, 2), LineItem("Setup", 500)])
        inv.tax_cents = 525
        assert inv.net_cents == 2500
        assert inv.total_cents == 3025
