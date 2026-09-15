import streamlit as st
from components.ui import html
from services.cart_service import count
from utils.navigation import nav_button

def navbar() -> None:
    html('<div class="announcement">Herbal care, from Kumbakonam. &nbsp; Complimentary shipping on orders $85+</div>')
    with st.container(key="desktopnav"):
        left, middle, right = st.columns([4, 4, 4], vertical_alignment="center")
        with left:
            a, b, c = st.columns(3)
            with a: nav_button("Products", "shop", "nav_shop")
            with b: nav_button("About", "about", "nav_about")
            with c: nav_button("Journal", "journal", "nav_journal")
        with middle: nav_button("SISTERSKESA", "home", "nav_home")
        with right:
            a, b = st.columns(2)
            with a:
                if st.button("Search  ⌕", key="nav_search", use_container_width=True):
                    from components.search import search_dialog
                    search_dialog()
            with b: nav_button(f"Bag ({count(st.session_state.cart)})", "cart", "nav_cart")
    from components.mobile_nav import mobile_nav
    mobile_nav()
