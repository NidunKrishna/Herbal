import streamlit as st
from components.ui import html, e
from services.catalog_service import get_product
from services.cart_service import totals, count
from utils.formatting import money
from utils.navigation import go

@st.dialog("A little something for your shelf")
def cart_drawer() -> None:
    st.caption(f"{count(st.session_state.cart)} items in your bag")
    for item in st.session_state.cart.values():
        p = get_product(item["product_id"])
        st.write(f"{p.name} · {item['size']} · ×{item['quantity']}")
    st.write(f"Subtotal: {money(totals(st.session_state.cart)['subtotal'])}")
    if st.button("VIEW YOUR BAG  ↗", type="primary", use_container_width=True):
        go("cart")
    if st.button("KEEP EXPLORING", use_container_width=True):
        st.rerun()
