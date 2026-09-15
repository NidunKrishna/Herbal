from decimal import Decimal, ROUND_HALF_UP

def rounded(value: float | Decimal) -> Decimal:
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def money(value: float | Decimal) -> str:
    return f"${rounded(value):,.2f}"
