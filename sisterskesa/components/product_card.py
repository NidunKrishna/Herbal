import streamlit as st
from components.ui import html, photo, e
from components.badges import badges
from utils.formatting import money
from utils.navigation import nav_button

def product_card(product, key: str) -> None:
    with st.container(key=f"card_{key}"):
        html(f'<article class="product-card"><div class="product-image">{photo(product.image, css="product-photo")}<div class="badges">{badges(product.badges)}</div><span class="product-volume">{e(product.sizes[0])}</span></div><div class="product-meta"><span>{e(product.brand)}</span><span aria-label="Rated {product.rating} out of 5">★ {product.rating} <span class="muted">({product.review_count})</span></span></div><h3>{e(product.name)}</h3><p class="descriptor">{e(product.description)}</p><p class="product-price">{money(product.sale_price if product.sale_price is not None else product.price)} {f"<del>{money(product.price)}</del>" if product.sale_price is not None else ""}</p></article>')
        nav_button(f"Discover {product.name} ↗", "product/"+product.slug, key=f"discover_{key}")
