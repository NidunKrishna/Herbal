import streamlit as st
from components.ui import html, photo
from utils.navigation import nav_button

def hero() -> None:
    with st.container(key="homehero"):
        html(f'<section class="hero"><div class="hero-image">{photo("home_hero", css="hero-photo", eager=True)}</div><div class="hero-shade"></div><div class="hero-copy"><p class="eyebrow">ROOTED IN KUMBAKONAM, TAMIL NADU</p><h1>Herbal care,<br><em>rooted in<br>nature.</em></h1><p>Authentic herbal rituals for skin, hair and body,<br class="desktop-break"> from Bhuvana and Radhika in Kumbakonam.</p></div><div class="hero-wordmark" aria-hidden="true">SISTERSKESA</div><div class="hero-caption">HERBS AT HEART. &nbsp; CARE WITH INTENTION</div></section>')
        nav_button("SHOP NEW ARRIVALS  ↗", "shop", key="hero_shop", primary=True, edit="new")
