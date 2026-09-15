import streamlit as st
from components.ui import html
from services.cart_service import totals, FREE_SHIPPING
from utils.formatting import money

def order_summary() -> None:
    t = totals(st.session_state.cart)
    progress = min(100,float(t["subtotal"]/FREE_SHIPPING*100))
    message = f"You’re {money(t['remaining'])} away from complimentary shipping." if t["remaining"] else "Your order qualifies for complimentary shipping."
    html(f'<div class="order-summary"><h2>Your summary</h2><p class="shipping-note">{message}</p><div class="shipping-track"><span style="width:{progress}%"></span></div><div class="total-row"><span>Subtotal</span><span>{money(t["subtotal"])}</span></div><div class="total-row"><span>You save</span><span>{money(t["savings"])}</span></div><div class="total-row"><span>Shipping</span><span>{money(t["shipping"]) if t["shipping"] else "Complimentary"}</span></div><div class="total-row total"><span>Total</span><span>{money(t["total"])}</span></div><p class="fineprint">USD · Demo total. Tax is not calculated.</p></div>')
