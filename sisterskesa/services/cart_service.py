"""Server-side prices derived from catalogue; session cart stores selections only."""
from decimal import Decimal
from data.products import Product
from services.catalog_service import get_product
from utils.formatting import rounded

FREE_SHIPPING = Decimal("85.00")
SHIPPING_FEE = Decimal("6.00")
CADENCES = ("Every month", "Every 6 weeks", "Every 2 months")

def unit_price(product: Product, size: str, subscription: bool = False, *, original: bool = False) -> Decimal:
    if size not in product.sizes:
        raise ValueError("Choose a valid size.")
    base = Decimal(str(product.price if original or product.sale_price is None else product.sale_price))
    # Sample travel-size pricing, explicitly editable here.
    size_factor = Decimal("1") if size == product.sizes[0] else Decimal("0.65")
    price = rounded(base * size_factor)
    return rounded(price * Decimal("0.85")) if subscription and not original else price

def add_item(cart: dict, product: Product, size: str, subscription: bool = False, cadence: str = "Every month", quantity: int = 1) -> str:
    if product.availability == "Out of Stock":
        raise ValueError("This item is currently out of stock.")
    unit_price(product, size, subscription)
    if not isinstance(quantity, int) or not 1 <= quantity <= 20:
        raise ValueError("Choose a quantity from 1 to 20.")
    if subscription and cadence not in CADENCES:
        raise ValueError("Choose a valid delivery schedule.")
    cadence = cadence if subscription else "One-time purchase"
    key = f"{product.id}|{size}|{subscription}|{cadence}"
    current = cart.get(key, {}).get("quantity", 0)
    if current + quantity > 20:
        raise ValueError("A maximum of 20 of each selection can be added.")
    cart[key] = {"product_id": product.id, "size": size, "subscription": subscription, "cadence": cadence, "quantity": current + quantity}
    return key

def set_quantity(cart: dict, key: str, quantity: int) -> None:
    if key not in cart:
        raise ValueError("Item is no longer in your bag.")
    if not isinstance(quantity, int) or not 1 <= quantity <= 20:
        raise ValueError("Choose a quantity from 1 to 20.")
    cart[key]["quantity"] = quantity

def totals(cart: dict) -> dict:
    subtotal = Decimal("0")
    retail = Decimal("0")
    for item in cart.values():
        p = get_product(item["product_id"])
        if p is None:
            raise ValueError("An item is no longer in the catalogue.")
        subtotal += unit_price(p, item["size"], item["subscription"]) * item["quantity"]
        retail += unit_price(p, item["size"], original=True) * item["quantity"]
    shipping = SHIPPING_FEE if 0 < subtotal < FREE_SHIPPING else Decimal("0")
    return {"subtotal": subtotal, "savings": retail-subtotal, "shipping": shipping, "total": subtotal+shipping, "remaining": max(Decimal("0"), FREE_SHIPPING-subtotal)}

def count(cart: dict) -> int:
    return sum(item["quantity"] for item in cart.values())
