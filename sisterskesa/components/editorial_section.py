import streamlit as st
from components.ui import html, photo
from utils.navigation import nav_button
from data.founders import STORY

def founders_section() -> None:
    with st.container(key="founderssection"):
        a, b = st.columns([1.1, 1], gap="large", vertical_alignment="center")
        with a:
            html(f'<figure class="founders-photo">{photo("founders")}<figcaption>Herbs at the heart of our story. Illustrative photography.</figcaption></figure>')
        with b:
            html(f'<div class="founders-copy"><p class="eyebrow">FROM KUMBAKONAM, WITH CARE</p><h2>Bhuvana &amp; Radhika.<br><em>One herbal vision.</em></h2><p>{STORY}</p><p class="signature">Bhuvana &amp; Radhika</p></div>')
            nav_button("MEET BHUVANA & RADHIKA  ↗", "about", "meet_founders")

def editorial_section() -> None:
    with st.container(key="ritualfeature"):
        html(f'<section class="ritual-feature">{photo("editorial_ritual")}<div><p class="eyebrow">HERBAL BODY & WELLNESS RITUALS</p><h2>Ritual,<br><em>not routine.</em></h2><p>The quiet pleasure of herbs, oils<br>and a little time for yourself.</p></div></section>')
        nav_button("DISCOVER THE EDIT  ↗", "category/body-rituals", "ritual_shop", primary=True)
