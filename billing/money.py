"""Money helpers. Everything is integer cents internally."""
from decimal import Decimal, ROUND_HALF_UP


def to_cents(amount) -> int:
    """Convert a decimal amount (str, int, Decimal) to integer cents, half up."""
    return int((Decimal(str(amount)) * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def format_cents(cents: int, currency: str = "EUR") -> str:
    sign = "-" if cents < 0 else ""
    cents = abs(cents)
    return f"{sign}{cents // 100}.{cents % 100:02d} {currency}".rstrip()


def div_round_half_up(numerator: int, denominator: int) -> int:
    """Integer division rounded half up (for non negative numbers)."""
    return (numerator * 2 + denominator) // (denominator * 2)
