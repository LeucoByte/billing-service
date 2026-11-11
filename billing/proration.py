"""Proration for plan changes in the middle of a billing period."""
import math


def daily_rate_cents(amount_cents: int, days_in_period: int) -> int:
    """Cost of one day of a period, in cents."""
    if days_in_period <= 0:
        raise ValueError("days_in_period must be positive")
    return math.ceil(amount_cents / days_in_period)


def prorate_cents(amount_cents: int, days_used: int, days_in_period: int) -> int:
    """Part of `amount_cents` that corresponds to `days_used` days of the period."""
    if not 0 <= days_used <= days_in_period:
        raise ValueError("days_used out of range")
    return amount_cents * days_used // days_in_period
