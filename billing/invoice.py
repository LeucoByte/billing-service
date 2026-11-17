"""Invoice construction."""
from .models import Invoice, LineItem
from .tax import tax_cents


def build_invoice(number: str, customer_email: str, country: str, items: list) -> Invoice:
    """Build an open invoice. VAT is computed per line and summed."""
    if not items:
        raise ValueError("an invoice needs at least one line")
    customer_email = customer_email.strip()
    lines = [LineItem(*i) if isinstance(i, tuple) else i for i in items]
    vat = sum(tax_cents(line.net_cents, country) for line in lines)
    return Invoice(number=number, customer_email=customer_email, country=country,
                   items=lines, tax_cents=vat, status="open")
