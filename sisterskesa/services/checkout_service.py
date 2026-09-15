import re
from uuid import uuid4
from datetime import datetime, timezone
from copy import deepcopy
from services.cart_service import totals
from services.catalog_service import get_product

def validate_details(details: dict) -> list[str]:
    errors = []
    if not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", details.get("email", "").strip()):
        errors.append("Enter a valid email address.")
    for key, label in (("name","full name"),("address","address"),("city","city"),("postal","postal code")):
        if not 2 <= len(details.get(key, "").strip()) <= 200:
            errors.append(f"Enter your {label} (2–200 characters).")
    if details.get("country") not in ("United States", "United Kingdom", "Canada", "Australia", "India"):
        errors.append("Choose an available demo destination.")
    return errors

def place_demo_order(cart: dict, details: dict, consent: bool) -> dict:
    errors = validate_details(details)
    if not consent: errors.append("Confirm that this is a demo order.")
    if not cart: errors.append("Your bag is empty.")
    for item in cart.values():
        p = get_product(item["product_id"])
        if p is None or p.availability == "Out of Stock": errors.append("An item is currently unavailable.")
    if errors: raise ValueError(" ".join(errors))
    return {"id": "TS-DEMO-"+uuid4().hex[:8].upper(), "created": datetime.now(timezone.utc).isoformat(), "items": deepcopy(cart), "totals": {k:str(v) for k,v in totals(cart).items()}, "first_name": details["name"].strip().split()[0], "demo": True}
