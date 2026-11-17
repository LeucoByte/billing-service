import unittest

from billing.exporter import invoices_to_csv
from billing.models import Invoice, LineItem


class ExporterTests(unittest.TestCase):
    def test_csv(self):
        inv = Invoice("2024-0010", "z@example.com", "FR", items=[LineItem("Pro", 1000)], tax_cents=200, status="paid")
        lines = invoices_to_csv([inv]).splitlines()
        assert lines[0].startswith("number,customer_email")
        assert lines[1].startswith("2024-0010,z@example.com,FR,10.00,2.00,12.00,paid,EUR"), lines[1]
