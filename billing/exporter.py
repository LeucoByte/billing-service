"""CSV export for the accounting team."""
import csv
import io

from .money import format_cents

HEADER = ["number", "customer_email", "country", "net", "tax", "total", "status", "currency"]


def invoices_to_csv(invoices) -> str:
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(HEADER)
    for inv in invoices:
        w.writerow([inv.number, inv.customer_email, inv.country,
                    format_cents(inv.net_cents, ""), format_cents(inv.tax_cents, ""),
                    format_cents(inv.total_cents, ""), inv.status, inv.currency])
    return buf.getvalue()
