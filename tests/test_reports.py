import unittest

from billing.models import Invoice, LineItem
from billing.reports import average_invoice_cents, revenue_by_country


def _inv(total, country="ES", status="paid"):
    return Invoice("n", "x@example.com", country, items=[LineItem("x", total)], status=status)


class ReportTests(unittest.TestCase):
    def test_average(self):
        assert average_invoice_cents([_inv(1000), _inv(2000)]) == 1500
        assert average_invoice_cents([]) == 0

    def test_revenue_by_country(self):
        got = revenue_by_country([_inv(1000), _inv(500, "DE"), _inv(700, "ES", "open")])
        assert got == {"ES": 1000, "DE": 500}, got
