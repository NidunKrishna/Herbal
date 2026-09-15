import streamlit as st
from components.ui import html, photo, e, heading
from components.breadcrumbs import breadcrumbs
from components.product_gallery import product_gallery
from components.product_grid import product_grid
from components.badges import badges
from services.catalog_service import get_product, related_products, get_products
from services.cart_service import unit_price, add_item, CADENCES
from utils.formatting import money
from utils.navigation import nav_button

def render(slug: str) -> None:
    product = get_product(slug)
    if product is None:
        st.warning("That discovery is no longer on the shelf.")
        nav_button("Explore the edit", "shop", "missing_product")
        return
    st.session_state.current_product = product.id
    with st.container(key="productpage"):
        breadcrumbs(product.name, product=True)
        a, b = st.columns([1.3, 1], gap="large")
        with a: product_gallery(product)
        with b:
            with st.container(key="productinfo"):
                html(f'<p class="eyebrow">{e(product.brand)}</p><h1>{e(product.name)}</h1><div>{badges(product.badges)}</div><p class="detail-price">{money(product.sale_price if product.sale_price is not None else product.price)}</p><p class="detail-description">{e(product.long_description)}</p><p class="fineprint">★ {product.rating} / 5 &nbsp; · &nbsp; {product.review_count} sample reviews</p>')
                size = st.radio("Size", product.sizes, horizontal=True, key="size_"+product.id)
                buy_price = unit_price(product, size)
                sub_price = unit_price(product, size, True)
                mode = st.radio("Make it your ritual", ("Buy once", "Subscribe & save 15%"), key="mode_"+product.id, format_func=lambda value: f"{value} — {money(buy_price if value == 'Buy once' else sub_price)}")
                subscription = mode != "Buy once"
                cadence = st.selectbox("Delivery frequency", CADENCES, key="cadence_"+product.id) if subscription else CADENCES[0]
                quantity = st.number_input("Quantity", min_value=1, max_value=20, value=1, step=1, key="qty_"+product.id)
                unavailable = product.availability == "Out of Stock"
                def add_to_bag():
                    try:
                        add_item(st.session_state.cart, product, size, subscription, cadence, quantity)
                        st.session_state["added_product"] = product.id
                    except ValueError as error:
                        st.session_state["bag_error"] = str(error)
                st.button("CURRENTLY OUT OF STOCK" if unavailable else "ADD TO BAG  —  "+money(unit_price(product,size,subscription)*quantity), key="add_to_bag", type="primary", disabled=unavailable, use_container_width=True, on_click=add_to_bag)
                if st.session_state.pop("bag_error", None):
                    st.error("A maximum of 20 of each selection can be added.")
                if st.session_state.pop("added_product", None) == product.id:
                    st.success(f"{product.name} is in your bag.")
                    nav_button("VIEW YOUR BAG  ↗", "cart", "added_view_bag")
                html('<p class="fineprint">Complimentary shipping on orders $85+.<br>Demo purchases only. No payment or recurring charge.</p>')
        title = "Grounded in herbs.<br><em>A moment of care,</em><br>close to nature." if product.id == "p001" else f"A little space for<br><em>{e(product.name.lower())}.</em>"
        html(f'<section class="product-story"><p class="eyebrow">WHY WE LOVE IT</p><h2>{title}</h2></section>')
        with st.container(key="storytabs"):
            about, benefits, ingredients, usage = st.tabs(("About", "Benefits", "Ingredients", "How to Use"))
            with about: st.write(product.long_description)
            with benefits:
                for benefit in product.benefits: st.write("• "+benefit)
            with ingredients:
                st.write(", ".join(product.ingredients))
                st.caption("Illustrative key ingredients for this fictional product, not a complete INCI list.")
            with usage: st.write(product.how_to_use)
        html(f'<section class="detail-editorial">{photo("category_skincare" if product.category == "skincare" else "category_"+{"hair-care":"hair","body-rituals":"body","wellness":"wellness"}.get(product.category,"skincare"))}<div><p class="eyebrow">CONSIDERED FROM THE START</p><h2>Comfort<br><em>in every detail.</em></h2><p>{e(product.description)}</p>{photo("ingredient_botanical",css="ingredient-inset")}</div></section>')
        heading("THE FORMULA, CONSIDERED", "Key <em>ingredients.</em>")
        html('<div class="ingredient-grid">'+''.join(f'<div class="ingredient"><p class="eyebrow">0{i}</p><h3>{e(ingredient)}</h3></div>' for i,ingredient in enumerate(product.ingredients,1))+'</div>')
        html(f'<div class="article-section"><p class="eyebrow">MAKE IT YOUR RITUAL</p><h2>How to use</h2><p>{e(product.how_to_use)}</p></div>')
        note = "Our vision begins with herbs and a simple intention: to bring authentic, thoughtful care into everyday life." if product.id == "p001" else "Herbs at the heart of a ritual that feels like yours. A little time, a little intention, a closer connection with nature."
        html(f'<aside class="sisters-note"><p class="eyebrow">SISTERSKESA’S NOTE</p><blockquote>“{e(note)}”</blockquote><span class="signature">Bhuvana &amp; Radhika</span></aside>')
        heading("BETTER TOGETHER", "Pairs <em>well with.</em>")
        pairs = [p for p in get_products() if p.category == product.category and p.id != product.id and p.subcategory != product.subcategory][:2]
        product_grid(pairs, "pairs", columns=2)
        heading("A FEW MORE DISCOVERIES", "You may <em>also love.</em>")
        product_grid(related_products(product), "related")
