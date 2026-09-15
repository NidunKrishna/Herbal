import streamlit as st
from data.categories import CATEGORIES
from services.cart_service import count
from utils.navigation import nav_button, go

@st.dialog("From our shelf to yours")
def menu() -> None:
    choices = [("Shop all", "shop"), *((c["name"], "category/"+slug) for slug, c in CATEGORIES.items()), ("About Bhuvana & Radhika", "about"), ("Journal", "journal"), ("Search", "search")]
    for i, (label, route) in enumerate(choices):
        if st.button(label, key=f"mobile_menu_{i}", use_container_width=True):
            go(route)

def mobile_nav() -> None:
    with st.container(key="mobilenav"):
        a, b, c = st.columns([6, 3, 1.7], vertical_alignment="center")
        with a: nav_button("SISTERSKESA", "home", "mobile_home")
        with b: nav_button(f"Bag ({count(st.session_state.cart)})", "cart", "mobile_cart")
        with c:
            if st.button("☰", key="mobile_menu", help="Open navigation menu"):
                menu()
