# billing-service

Internal service that builds and exports customer invoices for the subscription product.
It is a plain Python package (no web framework yet, the API layer lives in `portal-api`).

## What it does

- builds an invoice from line items (`billing.invoice.build_invoice`)
- computes VAT per line using the country table in `billing/tax.py`
- prorates plan changes in the middle of a period (`billing/proration.py`)
- exports invoices to CSV for accounting (`billing/exporter.py`)
- a couple of reports used by finance (`billing/reports.py`)

All amounts are integer cents. Never use floats for money.

## Running the tests

```
python -m unittest discover -s tests -v
```

Python 3.11+ and no third party dependencies.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Quick example

```python
from billing.invoice import build_invoice
from billing.exporter import invoices_to_csv

inv = build_invoice("2024-0101", "ops@example.com", "ES", [("Pro plan", 4900, 1)])
print(invoices_to_csv([inv]))
```
