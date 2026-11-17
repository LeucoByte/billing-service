"""Plain data classes for invoices."""
from dataclasses import dataclass, field
from typing import List


@dataclass
class LineItem:
    description: str
    unit_cents: int
    quantity: int = 1

    @property
    def net_cents(self) -> int:
        return self.unit_cents * self.quantity


@dataclass
class Invoice:
    number: str
    customer_email: str
    country: str
    items: List[LineItem] = field(default_factory=list)
    tax_cents: int = 0
    status: str = "draft"   # draft | open | paid | void
    currency: str = "EUR"

    @property
    def net_cents(self) -> int:
        return sum(i.net_cents for i in self.items)

    @property
    def total_cents(self) -> int:
        return self.net_cents + self.tax_cents
