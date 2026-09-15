import streamlit as st
from data.products import PRODUCTS, Product

@st.cache_data
def get_products() -> tuple[Product, ...]:
    return PRODUCTS

def get_product(slug_or_id: str) -> Product | None:
    return next((p for p in get_products() if slug_or_id in (p.slug, p.id)), None)

def related_products(product: Product, limit: int = 4) -> list[Product]:
    others = [p for p in get_products() if p.id != product.id]
    return sorted(others, key=lambda p: (p.category != product.category, not p.sisters_pick))[:limit]
