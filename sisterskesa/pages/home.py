import streamlit as st
from components.hero import hero
from components.ui import html, heading
from components.category_strip import category_strip
from components.editorial_section import founders_section, editorial_section
from components.product_grid import product_grid
from components.newsletter import newsletter
from services.catalog_service import get_products
from utils.navigation import nav_button

def render() -> None:
    hero()
    with st.container(key="philosophy"):
        html('<p class="eyebrow">OUR PHILOSOPHY</p><h2>The simplicity of herbs.<br>The beauty of everyday rituals.<br><em>Closer to nature.</em></h2><p>Rooted in authenticity. Inspired by the herbs around us.</p>')
        nav_button("READ OUR STORY  ↗", "about", "philosophy_story")
    category_strip()
    with st.container(key="favourites"):
        a, b = st.columns([3, 1], vertical_alignment="bottom")
        with a: heading("OUR CURRENT FAVOURITES", "Herbal favourites,<br><em>for your daily rituals.</em>")
        with b: nav_button("EXPLORE THE EDIT  ↗", "shop", "favourites_all")
        product_grid([p for p in get_products() if p.featured], "home")
    founders_section()
    editorial_section()
    from pages.journal import journal_cards
    with st.container(key="homejournal"):
        heading("SISTERSKESA’S JOURNAL", "A little inspiration.<br><em>A moment for you.</em>")
        journal_cards("home")
    newsletter()
