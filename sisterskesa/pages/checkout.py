import json
import streamlit as st
from components.ui import html, e
from components.breadcrumbs import breadcrumbs
from components.order_summary import order_summary
from services.checkout_service import place_demo_order
from utils.navigation import nav_button
from utils.formatting import money

def render() -> None:
    with st.container(key="checkoutpage"):
        breadcrumbs("Demo checkout")
        if st.session_state.order and not st.session_state.cart:
            order = st.session_state.order
            html(f'<div class="order-success"><p class="eyebrow">YOUR DEMO ORDER IS COMPLETE</p><h1>A lovely choice,<br><em>{e(order["first_name"])}.</em></h1><p>Reference: {e(order["id"])}<br>Demo total: {money(order["totals"]["total"])}</p><p>No payment was taken. Nothing will be shipped.<br>No subscription or confirmation email has been created.</p></div>')
            st.download_button("DOWNLOAD DEMO RECEIPT", json.dumps(order,indent=2), file_name=order["id"]+".json", mime="application/json", use_container_width=True)
            nav_button("BACK TO THE EDIT  ↗", "shop", "order_shop", primary=True)
            return
        if not st.session_state.cart:
            st.info("Add something to your bag before checking out.")
            nav_button("Explore the edit", "shop", "checkout_empty")
            return
        html('<h1>The final <em>little step.</em></h1><div class="checkout-note"><p>Demo checkout — use sample details. No payment is collected, nothing is shipped, and subscriptions are not activated.</p></div>')
        a, b = st.columns([1.5,1], gap="large")
        with a:
            with st.form("checkout_form"):
                st.subheader("Where would your discoveries go?")
                details = {"email": st.text_input("Email", placeholder="you@example.com", max_chars=254), "name": st.text_input("Full name", max_chars=200), "address": st.text_input("Street address", max_chars=200), "city": st.text_input("City", max_chars=200), "postal": st.text_input("Postal code", max_chars=30), "country": st.selectbox("Country", ("United States", "United Kingdom", "Canada", "Australia", "India"))}
                consent = st.checkbox("I understand this is a demo and no order will be fulfilled.")
                submit = st.form_submit_button("PLACE DEMO ORDER  ↗", use_container_width=True)
            if submit:
                try:
                    st.session_state.order = place_demo_order(st.session_state.cart, details, consent)
                except ValueError as error:
                    st.error(str(error))
                else:
                    st.session_state.cart = {}
                    st.rerun()
        with b:
            order_summary()
            nav_button("RETURN TO YOUR BAG", "cart", "checkout_back")
