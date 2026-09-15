from data.products import Product

FILTER_OPTIONS = {
    "availability": ("In Stock", "Limited Edition"),
    "subcategory": ("Face Powder", "Powder Cleanser", "Powder Mask", "Face Oil", "Face Mist", "Hair Oil", "Scalp Oil", "Herbal Hair Wash", "Hair Mask", "Body Oil", "Hand Oil", "Bath Powder", "Body Polish", "Botanical Bath Blend", "Linen Mist", "Botanical Sachet", "Bath Oil"),
    "texture": ("Powder", "Oil", "Mist / Spray", "Dried Botanicals"),
    "fragrance_profile": ("Floral", "Herbal", "Earthy", "Woody", "Nutty"),
    "values": ("Botanical Ingredients", "Herbal Powders", "Botanical Oils", "Hydrosols", "Dried Herbs & Flowers"),
    "care_goals": ("Face Ritual", "Fresh Start", "Hair Ritual", "Scalp Ritual", "Body Ritual", "Bathing Ritual", "Slow Evenings"),
}
FILTER_LABELS = {"availability": "Availability", "subcategory": "Product type", "texture": "Texture", "fragrance_profile": "Botanical notes", "values": "Botanical composition", "care_goals": "Your ritual"}

def filter_products(products: list[Product] | tuple[Product, ...], filters: dict, category: str = "all", new_only: bool = False) -> list[Product]:
    result = []
    for p in products:
        if category != "all" and p.category != category:
            continue
        if new_only and not p.new_arrival:
            continue
        low, high = filters.get("price", (10, 320))
        if not low <= (p.sale_price if p.sale_price is not None else p.price) <= high:
            continue
        matched = True
        for field in FILTER_OPTIONS:
            selected = set(filters.get(field, []))
            if not selected:
                continue
            value = getattr(p, field)
            candidates = set(value) if isinstance(value, tuple) else {value}
            if field == "availability" and value == "Limited Edition":
                candidates.add("In Stock")
            # Composition tags are requested together; other groups use OR.
            if not (selected <= candidates if field == "values" else selected & candidates):
                matched = False
                break
        if matched:
            result.append(p)
    return result

def sort_products(products: list[Product], sort: str) -> list[Product]:
    if sort == "Price: low to high":
        return sorted(products, key=lambda p: p.sale_price if p.sale_price is not None else p.price)
    if sort == "Price: high to low":
        return sorted(products, key=lambda p: p.sale_price if p.sale_price is not None else p.price, reverse=True)
    if sort == "Top rated":
        return sorted(products, key=lambda p: (p.rating, p.review_count), reverse=True)
    if sort == "Newest":
        return sorted(products, key=lambda p: not p.new_arrival)
    return sorted(products, key=lambda p: (not p.sisters_pick, not p.featured))

def active_count(filters: dict) -> int:
    return sum(len(filters.get(k, [])) for k in FILTER_OPTIONS) + (tuple(filters.get("price", (10, 320))) != (10, 320))
