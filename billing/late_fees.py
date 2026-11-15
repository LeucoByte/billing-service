"""Late payment fees. WIP."""

# TODO: confirm the grace period with finance
GRACE_DAYS = 5


def late_fee_cents(total_cents: int, days_late: int) -> int:
    if days_late <= GRACE_DAYS:
        return 0
    # TODO: per day or flat?
    return total_cents * 2 // 100
