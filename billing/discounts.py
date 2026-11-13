"""Volume discounts for invoice line items."""


def volume_discount_percent(quantity: int) -> int:
    if quantity >= 100:
        return 15
    if quantity >= 50:
        return 10
    if quantity >= 10:
        return 5
    return 0


def apply_discount_cents(net_cents: int, percent: int) -> int:
    discount = net_cents * percent // 100
    return net_cents - discount
