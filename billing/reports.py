"""Numbers finance asks for every month."""
from collections import defaultdict


def _paid(invoices):
    return [i for i in invoices if i.status == "paid"]


def average_invoice_cents(invoices) -> int:
    """Average total in cents of the paid invoices (0 if there are no invoices)."""
    if not invoices:
        return 0
    paid = _paid(invoices)
    return sum(i.total_cents for i in paid) // len(paid)


def revenue_by_country(invoices) -> dict:
    out = defaultdict(int)
    for inv in _paid(invoices):
        out[inv.country] += inv.total_cents
    return dict(out)
