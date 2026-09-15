import streamlit as st
from components.ui import html
from utils.navigation import nav_button
from data.categories import CATEGORIES

def footer() -> None:
    with st.container(key="footer"):
        a, b, c, d = st.columns([2, 1, 1, 1])
        with a:
            html('<h2 class="footer-logo">SISTERSKESA</h2><p>Rooted in herbs.<br>From Kumbakonam, with care.</p><p class="eyebrow">AUTHENTIC HERBAL CARE.</p>')
        with b:
            html('<p class="eyebrow">SHOP</p>')
            for slug, cat in CATEGORIES.items():
                nav_button(cat["name"], "category/"+slug, "foot_"+slug)
        with c:
            html('<p class="eyebrow">ABOUT</p>')
            for name, route in [("Our Story", "about"), ("Journal", "journal"), ("Contact", "help/contact")]:
                nav_button(name, route, "foot_"+name)
            for name in ("Instagram", "Pinterest", "TikTok"):
                nav_button(name+" ↗", "help/social", "foot_"+name)
        with d:
            html('<p class="eyebrow">HERE TO HELP</p>')
            for name in ("Shipping", "Returns", "FAQ", "Privacy"):
                nav_button(name, "help/"+name.lower(), "foot_"+name)
        html('<div class="footer-bottom"><span>© 2026 SISTERSKESA</span><span>Demo storefront · Fictional products, sample prices & reviews · USD</span><span>Made with intention.</span></div>')
