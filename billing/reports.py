"""Numbers finance asks for every month."""
from collections import defaultdict


def average_invoice_cents(invoices) -> int:
    """Average invoice total in cents (0 if there are no invoices)."""
    if not invoices:
        return 0
    return sum(i.total_cents for i in invoices) // len(invoices)


def revenue_by_country(invoices) -> dict:
    out = defaultdict(int)
    for inv in invoices:
        if inv.status == "paid":
            out[inv.country] += inv.total_cents
    return dict(out)
