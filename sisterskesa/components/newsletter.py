import re
import streamlit as st
from components.ui import html

def newsletter() -> None:
    with st.container(key="newsletter"):
        a, b = st.columns([1.2, 1], gap="large", vertical_alignment="center")
        with a:
            html('<p class="eyebrow">A LETTER, EVERY NOW AND THEN</p><h2>Notes from <em>sisterskesa.</em></h2><p>Herbal discoveries, everyday rituals and notes from Kumbakonam.</p>')
        with b:
            with st.form("newsletter_form", clear_on_submit=True):
                email = st.text_input("Your email address", placeholder="Your email address", max_chars=254)
                consent = st.checkbox("I agree to receive Notes from sisterskesa.")
                submitted = st.form_submit_button("JOIN THE LIST  ↗", use_container_width=True)
            if submitted:
                if not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email.strip()):
                    st.error("Please enter a valid email address.")
                elif not consent:
                    st.error("Please confirm that you’d like to join the list.")
                else:
                    if email.strip().lower() not in st.session_state.newsletter_emails:
                        st.session_state.newsletter_emails.append(email.strip().lower())
                    st.success("You’re on the preview list. This demo saves your signup for this session; no email is sent.")
            html('<p class="fineprint">A little inspiration. Never a crowded inbox. Preview signup only.</p>')
