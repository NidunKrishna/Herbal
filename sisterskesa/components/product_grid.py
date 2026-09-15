import streamlit as st
from components.product_card import product_card
from components.ui import html, photo

def product_grid(products, key: str = "grid", columns: int = 4, editorial: bool = False) -> None:
    for start in range(0, len(products), columns):
        with st.container(key=f"productrow_{key}_{start}"):
            cols = st.columns(columns, gap="medium")
            for col, product in zip(cols, products[start:start+columns]):
                with col:
                    product_card(product, f"{key}_{product.id}")
        if editorial and start == columns and len(products) > columns * 2:
            html(f'<div class="shop-editorial">{photo("editorial_ritual")}<div><p class="eyebrow">THE ART OF DOING LESS</p><h2>Herbs at heart.<br><em>Care in every ritual.</em></h2><p>A little space in your day to reconnect with nature.</p></div></div>')
