import streamlit as st
from components.ui import html, photo, e
from components.breadcrumbs import breadcrumbs
from components.newsletter import newsletter
from data.founders import STORY, BHUVANA_NOTE, RADHIKA_NOTE
from utils.navigation import nav_button

def render() -> None:
    with st.container(key="aboutpage"):
        breadcrumbs("Our story")
        a, b = st.columns([1,1.05], gap="large", vertical_alignment="center")
        with a:
            html(f'<p class="eyebrow">BHUVANA &amp; RADHIKA · KUMBAKONAM</p><h1>Two women,<br><em>one herbal vision.</em></h1><p class="intro">{e(STORY)}</p>')
        with b:
            html(f'<figure>{photo("founders")}<figcaption>Herbs, care and intention. Illustrative photography.</figcaption></figure>')
        html('<section class="story-statement"><p class="eyebrow">OUR ROOTS · TAMIL NADU</p><h2>From Kumbakonam,<br><em>with care.</em></h2><p>Bhuvana and Radhika’s vision begins in Kumbakonam, Tamil Nadu. They want to create authentic products centred on herbs, bringing a thoughtful connection with nature into the everyday.</p></section>')
        cols = st.columns(2, gap="large")
        with cols[0]:
            html('<div class="story-note"><p class="eyebrow">01 / OUR INTENTION</p><h2>Herbs at heart.<br><em>Authenticity in spirit.</em></h2><p>sisterskesa is a shared intention to keep herbal ingredients at the centre of care. Earthy textures, botanical aromas and simple rituals shape the brand’s point of view.</p></div>')
        with cols[1]:
            html('<div class="story-note"><p class="eyebrow">02 / EVERYDAY RITUALS</p><h2>Closer to nature.<br><em>Closer to yourself.</em></h2><p>From a quiet hair-oiling ritual to a little time for skin and body, the collection is imagined around familiar moments of care. Thoughtful ingredients, with room to slow down.</p></div>')
        a, b = st.columns(2, gap="large")
        with a: html(f'<div class="founder-note"><p class="eyebrow">BHUVANA / AUTHENTICITY</p><p>{e(BHUVANA_NOTE)}</p><span class="signature">Bhuvana</span></div>')
        with b: html(f'<div class="founder-note"><p class="eyebrow">RADHIKA / EVERYDAY CARE</p><p>{e(RADHIKA_NOTE)}</p><span class="signature">Radhika</span></div>')
        nav_button("EXPLORE OUR HERBAL COLLECTION  ↗", "shop", "about_shop", primary=True)
    newsletter()
