USD_TO_EUR_RATE = 0.92


def usd_to_eur(amount_usd: float) -> float:
    """Convert US Dollars to Euros.

    Args:
        amount_usd: Amount in USD to convert. Negative values represent
            a negative balance and are converted proportionally.

    Returns:
        Equivalent amount in EUR.
    """
    return round(amount_usd * USD_TO_EUR_RATE, 2)
