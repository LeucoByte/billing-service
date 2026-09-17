"""VAT calculation."""
from .money import to_cents

# percent, by ISO country code. TODO: move this to a table we can update without a deploy
TAX_RATES = {"ES": 21, "DE": 19, "FR": 20, "PT": 23, "IT": 22, "US": 0}


def rate_for(country: str) -> int:
    try:
        return TAX_RATES[country.upper()]
    except KeyError:
        raise ValueError(f"no tax rate for {country!r}")


def tax_cents(net_cents: int, country: str) -> int:
    """VAT for one amount, rounded half up to the cent."""
    rate = rate_for(country)
    return (net_cents * rate * 2 + 100) // 200
