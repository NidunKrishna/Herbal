import streamlit as st
from components.ui import html, photo, e
from data.categories import CATEGORIES
from utils.navigation import nav_button

def category_strip() -> None:
    with st.container(key="categorystrip"):
        a, b = st.columns([1, 1.6], gap="large")
        with a:
            html('<p class="eyebrow">A PLACE FOR EVERY RITUAL</p><h2>Rooted in herbs,<br><em>made for your rituals.</em></h2><p>A little closer to nature.<br>Find your place to begin.</p>')
        with b:
            for i, (slug, category) in enumerate(CATEGORIES.items(), 1):
                with st.expander(f"0{i}   {category['name'].upper()}", expanded=i == 1):
                    html(f'<div class="category-reveal">{photo(category["image"])}<p>{e(category["copy"])}</p></div>')
                    nav_button("VIEW MORE  ↗", "category/"+slug, f"category_{slug}")
