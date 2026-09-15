import streamlit as st
from components.ui import html, photo, e
from components.breadcrumbs import breadcrumbs
from components.order_summary import order_summary
from services.catalog_service import get_product
from services.cart_service import count, set_quantity, unit_price
from utils.formatting import money
from utils.navigation import nav_button

def render() -> None:
    with st.container(key="cartpage"):
        breadcrumbs("Your bag")
        html(f'<p class="eyebrow">GOOD THINGS, CHOSEN BY YOU</p><h1>Your <em>bag.</em> <span style="font-size:.45em">({count(st.session_state.cart)})</span></h1>')
        if not st.session_state.cart:
            html('<div class="empty-state"><h2>A little room<br><em>for something lovely.</em></h2><p>Your bag is waiting for your next discovery.</p></div>')
            nav_button("EXPLORE THE EDIT  ↗", "shop", "empty_shop", primary=True)
            return
        items, summary = st.columns([1.6,1], gap="large")
        with items:
            for key, item in list(st.session_state.cart.items()):
                p = get_product(item["product_id"])
                html('<div class="cart-line"></div>')
                a, b = st.columns([1, 2.4], gap="medium")
                with a: html(photo(p.image, css="cart-thumb"))
                with b:
                    html(f'<p class="eyebrow">{e(p.brand)}</p><h2 class="cart-name">{e(p.name)}</h2><p class="cart-meta">{e(item["size"])} · {e(item["cadence"])}<br>{"Subscribe & save 15%" if item["subscription"] else "Buy once"}</p><p>{money(unit_price(p,item["size"],item["subscription"])*item["quantity"])}</p>')
                    qkey = "cartqty_"+key
                    def update_quantity(cart_key=key, widget_key=qkey):
                        set_quantity(st.session_state.cart, cart_key, int(st.session_state[widget_key]))
                    st.number_input("Quantity", 1, 20, item["quantity"], key=qkey, on_change=update_quantity)
                    def remove(cart_key=key):
                        st.session_state.cart.pop(cart_key,None)
                    st.button("Remove", key="remove_"+key, on_click=remove)
        with summary:
            order_summary()
            nav_button("CONTINUE TO DEMO CHECKOUT  ↗", "checkout", "checkout_button", primary=True)
            nav_button("KEEP EXPLORING", "shop", "continue_shop")
