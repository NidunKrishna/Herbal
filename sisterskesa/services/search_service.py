from data.products import Product

def search_products(products: list[Product] | tuple[Product, ...], query: str) -> list[Product]:
    words = query.casefold().strip().split()
    return [p for p in products if all(w in " ".join((p.name, p.brand, p.category.replace('-', ' '), *p.care_goals, *p.ingredients, *p.tags)).casefold() for w in words)]
