import streamlit as st
from utils.navigation import nav_button
from components.ui import html, e

def breadcrumbs(current: str, product: bool = False) -> None:
    with st.container(key="breadcrumbs"):
        cols = st.columns([1, 1.3, 7.7] if product else [1, 9])
        with cols[0]: nav_button("Home", "home", "crumb_home")
        if product:
            with cols[1]: nav_button("Products", "shop", "crumb_shop")
        with cols[-1]: html(f'<p class="crumb-current">/ &nbsp; {e(current)}</p>')
