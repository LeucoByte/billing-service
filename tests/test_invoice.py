import unittest

from billing.invoice import build_invoice


class InvoiceTests(unittest.TestCase):
    def test_build(self):
        inv = build_invoice("2024-0002", "b@example.com", "DE", [("Pro plan", 1000, 1), ("Seats", 250, 4)])
        assert inv.net_cents == 2000
        assert inv.tax_cents == 380
        assert inv.status == "open"

    def test_empty(self):
        with self.assertRaises(ValueError):
            build_invoice("2024-0003", "c@example.com", "ES", [])

    def test_email_is_trimmed(self):
        inv = build_invoice("2024-0004", "  d@example.com ", "ES", [("Pro plan", 1000, 1)])
        assert inv.customer_email == "d@example.com"
