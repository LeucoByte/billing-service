"""Volume discounts for invoice line items."""
from .config import VOLUME_TIERS


def volume_discount_percent(quantity: int) -> int:
    for min_qty, percent in VOLUME_TIERS:
        if quantity >= min_qty:
            return percent
    return 0


def apply_discount_cents(net_cents: int, percent: int) -> int:
    discount = net_cents * percent // 100
    return net_cents - discount
