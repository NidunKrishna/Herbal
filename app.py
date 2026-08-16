"""
Sisters Kesa — Herbal Hair & Body Care
A creative, interactive Streamlit storefront demo.

Run with:  streamlit run app.py
"""

import copy
import random
import string
from datetime import datetime

import streamlit as st

# --------------------------------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------------------------------
st.set_page_config(
    page_title="Sisters Kesa | Herbal Hair Care",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------------------------------
# PRODUCT DATA  (placeholder prices, relevant demo descriptions)
# --------------------------------------------------------------------------
DEFAULT_PRODUCTS = [
    {
        "id": "shikkai",
        "name": "Sisters Kesa Shikkai Powder",
        "category": "Hair Cleanser",
        "price": 249,
        "unit": "200g pack",
        "icon": "🌾",
        "color": "#6B8E4E",
        "tagline": "Nature's gentle alternative to shampoo",
        "description": (
            "A pure, chemical-free herbal hair cleanser made from sun-dried "
            "Shikakai pods, blended with Reetha (soapnut) and Amla. It gently "
            "cleanses the scalp without stripping natural oils, reduces hair "
            "fall, and leaves hair soft, shiny, and naturally fragrant."
        ),
        "ingredients": "Shikakai, Reetha, Amla, Hibiscus leaves",
        "tags": ["Best Seller", "Chemical-Free"],
        "rating": 4.8,
        "reviews": 312,
        "concerns": ["Natural cleansing", "Frizz-prone hair"],
    },
    {
        "id": "oil",
        "name": "Sisters Kesa Hair Oil",
        "category": "Hair Oil",
        "price": 349,
        "unit": "100ml bottle",
        "icon": "🧴",
        "color": "#A85D2A",
        "tagline": "Nourishment rooted in tradition",
        "description": (
            "A rich blend of cold-pressed coconut oil slow-infused with curry "
            "leaves, hibiscus, bhringraj, and fenugreek. Regular massage "
            "strengthens roots, controls hair fall, and promotes thicker, "
            "healthier growth."
        ),
        "ingredients": "Coconut oil, Curry leaves, Hibiscus, Bhringraj, Fenugreek",
        "tags": ["Best Seller", "Cold-Pressed"],
        "rating": 4.9,
        "reviews": 458,
        "concerns": ["Hair fall", "Slow growth"],
    },
    {
        "id": "nalangu",
        "name": "Sisters Kesa Nalangu Maavu",
        "category": "Bath Powder",
        "price": 199,
        "unit": "150g pack",
        "icon": "🛁",
        "color": "#C9962C",
        "tagline": "A traditional ritual for radiant skin",
        "description": (
            "A time-honoured herbal bath powder made from green gram, "
            "turmeric, and fragrant herbs. Used for generations as a gentle "
            "full-body cleanser, it exfoliates softly, brightens skin tone, "
            "and leaves you feeling naturally fresh — no soap needed."
        ),
        "ingredients": "Green gram, Turmeric, Sandalwood, Rose petals",
        "tags": ["Traditional Recipe"],
        "rating": 4.6,
        "reviews": 187,
        "concerns": ["Skin brightening", "Natural cleansing"],
    },
    {
        "id": "haircpack",
        "name": "Sisters Kesa Hair Pack",
        "category": "Hair Mask",
        "price": 279,
        "unit": "200g pack",
        "icon": "🌺",
        "color": "#8A3B5A",
        "tagline": "Deep repair, the herbal way",
        "description": (
            "A nourishing hair mask combining hibiscus, amla, fenugreek, and "
            "neem to deeply condition dry or damaged hair, calm an itchy "
            "scalp, control dandruff, and restore natural softness and "
            "strength."
        ),
        "ingredients": "Hibiscus, Amla, Fenugreek, Neem",
        "tags": ["New", "Anti-Dandruff"],
        "rating": 4.7,
        "reviews": 96,
        "concerns": ["Dandruff", "Dry or damaged hair"],
    },
]

QUIZ_MAP = {
    "Hair fall / thinning hair": "oil",
    "Dandruff / itchy scalp": "haircpack",
    "Dry or damaged hair": "haircpack",
    "I want a natural shampoo alternative": "shikkai",
    "I want a herbal skin/bath ritual": "nalangu",
}

FREE_SHIPPING_THRESHOLD = 499

# --------------------------------------------------------------------------
# CSS
# --------------------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Nunito:wght@400;600;700&display=swap');

    html, body, [class*="css"]  { font-family: 'Nunito', sans-serif; }
    h1, h2, h3, .brand-title { font-family: 'Playfair Display', serif; }

    .stApp { background-color: #FAF6EE; }

    /* Base text color comes from .streamlit/config.toml (textColor).
       Only override color on our own custom elements below — never
       with a blanket selector, so button labels / pill badges keep
       their own readable contrast against colored backgrounds. */

    .brand-title {
        font-size: 2.6rem;
        font-weight: 700;
        color: #111111 !important;
        margin-bottom: 0;
    }
    .brand-subtitle {
        color: #333333 !important;
        font-size: 1.05rem;
        margin-top: 0.2rem;
    }

    .hero {
        background: linear-gradient(135deg, #355E3B 0%, #4C7A4E 100%);
        border-radius: 18px;
        padding: 2.5rem 2.5rem;
        color: #FFFFFF;
        margin-bottom: 1.5rem;
    }
    .hero h1, .hero p { color: #FFFFFF !important; }
    .hero h1 { font-size: 2.4rem; margin-bottom: 0.3rem;}
    .hero p { font-size: 1.1rem; }

    .stat-box {
        background: #FFFFFF;
        border-radius: 14px;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 2px 10px rgba(53,94,59,0.08);
    }
    .stat-box .num { font-size: 1.6rem; font-weight: 700; color: #111111 !important; }
    .stat-box .lbl { color: #333333 !important; font-size: 0.85rem; }

    /* Native bordered st.container(border=True, key="pcard_...") — product cards only */
    div[class*="st-key-pcard_"] {
        background: #FFFFFF;
        border-radius: 16px !important;
        box-shadow: 0 3px 14px rgba(53,94,59,0.10);
        margin-bottom: 1.1rem;
        border-color: #EEE6D6 !important;
    }

    .icon-badge {
        width: 64px; height: 64px;
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 2rem;
        margin-bottom: 0.6rem;
    }

    .pill {
        display: inline-block;
        padding: 2px 10px;
        border-radius: 20px;
        font-size: 0.72rem;
        font-weight: 700;
        margin-right: 6px;
        margin-bottom: 4px;
        background: #E9EFE1;
        color: #355E3B !important;
    }
    .pill.gold { background: #FBF0D9; color: #A5761E !important; }

    .price-tag { font-size: 1.35rem; font-weight: 700; color: #355E3B !important; }
    .unit-text { color: #555555 !important; font-size: 0.85rem; }

    .quote-box {
        background: #FFFFFF;
        border-left: 4px solid #C9962C;
        border-radius: 8px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.8rem;
        font-style: italic;
        color: #111111 !important;
    }

    .badge-count {
        background: #C9962C;
        color: #FFFFFF !important;
        border-radius: 20px;
        padding: 1px 9px;
        font-size: 0.75rem;
        font-weight: 700;
    }

    section[data-testid="stSidebar"] { background-color: #EFE9DA; }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------------------------------
# SESSION STATE
# --------------------------------------------------------------------------
if "products" not in st.session_state:
    st.session_state.products = copy.deepcopy(DEFAULT_PRODUCTS)
if "cart" not in st.session_state:
    st.session_state.cart = {}  # product_id -> qty
if "nav" not in st.session_state:
    st.session_state.nav = "Home"
if "quiz_result" not in st.session_state:
    st.session_state.quiz_result = None
if "last_order" not in st.session_state:
    st.session_state.last_order = None
if "wishlist" not in st.session_state:
    st.session_state.wishlist = set()
if "user_ratings" not in st.session_state:
    st.session_state.user_ratings = {}  # pid -> stars the current user gave
if "recent" not in st.session_state:
    st.session_state.recent = []  # most-recently viewed pids, newest first
if "show_dialog" not in st.session_state:
    st.session_state.show_dialog = None


def get_products():
    return st.session_state.products


def get_product(pid):
    for p in st.session_state.products:
        if p["id"] == pid:
            return p
    return None


def format_price(n):
    return f"₹{n:,.0f}"


def cart_count():
    return sum(st.session_state.cart.values())


def cart_subtotal():
    return sum(get_product(pid)["price"] * qty for pid, qty in st.session_state.cart.items())


def add_to_cart(pid, qty=1):
    st.session_state.cart[pid] = st.session_state.cart.get(pid, 0) + qty
    st.toast(f"Added {get_product(pid)['name']} to cart 🌿", icon="✅")


def toggle_wishlist(pid):
    if pid in st.session_state.wishlist:
        st.session_state.wishlist.discard(pid)
    else:
        st.session_state.wishlist.add(pid)
        st.toast("Added to wishlist ❤️", icon="💚")


def track_recent(pid):
    r = st.session_state.recent
    if pid in r:
        r.remove(pid)
    r.insert(0, pid)
    st.session_state.recent = r[:5]


def rate_product(pid, star_value):
    """Register (or update) the current user's rating for a product."""
    prod = get_product(pid)
    prev = st.session_state.user_ratings.get(pid)
    if prev == star_value:
        return
    if prev is None:
        prod["rating"] = round((prod["rating"] * prod["reviews"] + star_value) / (prod["reviews"] + 1), 2)
        prod["reviews"] += 1
    else:
        prod["rating"] = round((prod["rating"] * prod["reviews"] - prev + star_value) / prod["reviews"], 2)
    st.session_state.user_ratings[pid] = star_value
    st.toast(f"Thanks for rating {star_value}★!", icon="⭐")


def go(page):
    st.session_state.nav = page
    st.rerun()


def open_quick_view(pid):
    track_recent(pid)
    st.session_state.show_dialog = pid


# --------------------------------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🌿 Sisters Kesa")
    st.caption("Herbal Hair & Body Care")
    st.markdown("---")

    pages = ["Home", "Shop", "Hair Care Quiz", "Wishlist", "Cart", "Checkout", "About & Contact"]
    for p in pages:
        label = p
        if p == "Cart":
            label = f"🛒 Cart ({cart_count()})" if cart_count() else "🛒 Cart"
        elif p == "Wishlist":
            label = f"❤️ Wishlist ({len(st.session_state.wishlist)})" if st.session_state.wishlist else "❤️ Wishlist"
        active = st.session_state.nav == p
        if st.button(label, use_container_width=True, key=f"nav_{p}",
                     type="primary" if active else "secondary"):
            go(p)

    st.markdown("---")
    st.markdown("**Your Cart**")
    if cart_count() == 0:
        st.caption("Your cart is empty.")
    else:
        for pid, qty in st.session_state.cart.items():
            p = get_product(pid)
            st.caption(f"{p['icon']} {p['name']} × {qty}")
        st.markdown(f"**Total: {format_price(cart_subtotal())}**")
        remaining = FREE_SHIPPING_THRESHOLD - cart_subtotal()
        if remaining > 0:
            st.progress(min(cart_subtotal() / FREE_SHIPPING_THRESHOLD, 1.0))
            st.caption(f"Add {format_price(remaining)} more for free shipping 🚚")
        else:
            st.progress(1.0)
            st.caption("You've unlocked free shipping! 🎉")


# --------------------------------------------------------------------------
# QUICK VIEW DIALOG
# --------------------------------------------------------------------------
@st.dialog("Quick View", width="large")
def quick_view_dialog(pid):
    p = get_product(pid)
    c1, c2 = st.columns([1, 2])
    with c1:
        st.markdown(
            f'<div class="icon-badge" style="background:{p["color"]}22; width:96px; height:96px; font-size:3rem;">{p["icon"]}</div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(f"### {p['name']}")
        st.caption(p["tagline"])
        tags_html = "".join(
            f'<span class="pill{" gold" if t in ("Best Seller", "New") else ""}">{t}</span>'
            for t in p["tags"]
        )
        st.markdown(tags_html, unsafe_allow_html=True)

    st.write(p["description"])
    st.caption(f"**Ingredients:** {p['ingredients']}")
    st.caption(f"**Good for:** {', '.join(p['concerns'])}")

    st.markdown(f"⭐ **{p['rating']}** average · {p['reviews']} reviews")
    st.caption("Rate this product:")
    idx = st.feedback("stars", key=f"dlg_rate_{pid}")
    if idx is not None:
        rate_product(pid, idx + 1)

    st.markdown("---")
    heart = "💚 In Wishlist" if pid in st.session_state.wishlist else "🤍 Add to Wishlist"
    wc1, wc2 = st.columns([1, 1])
    with wc1:
        if st.button(heart, use_container_width=True, key=f"dlg_wish_{pid}"):
            toggle_wishlist(pid)
            st.rerun()
    with wc2:
        st.markdown(f'<span class="price-tag">{format_price(p["price"])}</span> <span class="unit-text">/ {p["unit"]}</span>', unsafe_allow_html=True)

    qty = st.number_input("Quantity", min_value=1, max_value=10, value=1, key=f"dlg_qty_{pid}")
    if st.button("Add to Cart 🛒", type="primary", use_container_width=True, key=f"dlg_add_{pid}"):
        add_to_cart(pid, qty)
        st.session_state.show_dialog = None
        st.rerun()


if st.session_state.show_dialog:
    quick_view_dialog(st.session_state.show_dialog)


# --------------------------------------------------------------------------
# REUSABLE: PRODUCT CARD
# --------------------------------------------------------------------------
def render_product_card(p, key_prefix=""):
    pid = p["id"]
    with st.container(border=True, key=f"pcard_{key_prefix}_{pid}"):
        top_l, top_r = st.columns([4, 1])
        with top_l:
            st.markdown(
                f'<div class="icon-badge" style="background:{p["color"]}22;">{p["icon"]}</div>',
                unsafe_allow_html=True,
            )
        with top_r:
            liked = pid in st.session_state.wishlist
            if st.button("💚" if liked else "🤍", key=f"{key_prefix}_wish_{pid}", help="Toggle wishlist"):
                toggle_wishlist(pid)
                st.rerun()

        st.markdown(f"#### {p['name']}")
        st.caption(p["tagline"])

        tags_html = "".join(
            f'<span class="pill{" gold" if t in ("Best Seller", "New") else ""}">{t}</span>'
            for t in p["tags"]
        )
        st.markdown(tags_html, unsafe_allow_html=True)
        st.write(p["description"])
        st.caption(f"**Ingredients:** {p['ingredients']}")

        st.caption(f"⭐ {p['rating']} ({p['reviews']} reviews) · {p['category']}")
        idx = st.feedback("stars", key=f"{key_prefix}_rate_{pid}")
        if idx is not None:
            rate_product(pid, idx + 1)

        col_a, col_b = st.columns([1, 1])
        with col_a:
            st.markdown(f'<span class="price-tag">{format_price(p["price"])}</span>', unsafe_allow_html=True)
            st.markdown(f'<span class="unit-text">{p["unit"]}</span>', unsafe_allow_html=True)
        with col_b:
            qty = st.number_input(
                "Qty", min_value=1, max_value=10, value=1, step=1,
                key=f"{key_prefix}_qty_{pid}", label_visibility="collapsed",
            )
            if st.button("Add to Cart 🛒", key=f"{key_prefix}_add_{pid}", use_container_width=True):
                add_to_cart(pid, qty)

        if st.button("🔍 Quick View", key=f"{key_prefix}_qv_{pid}", use_container_width=True):
            open_quick_view(pid)
            st.rerun()


# --------------------------------------------------------------------------
# PAGE: HOME
# --------------------------------------------------------------------------
def page_home():
    st.markdown(
        """
        <div class="hero">
            <h1>Sisters Kesa 🌿</h1>
            <p>Traditional herbal hair &amp; body care, crafted the way our grandmothers made it —
            pure, natural, and made with love.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)
    stats = [
        ("100%", "Natural Ingredients"),
        ("0", "Harmful Chemicals"),
        ("4.8★", "Average Rating"),
        ("1000+", "Happy Customers"),
    ]
    for col, (num, lbl) in zip([c1, c2, c3, c4], stats):
        with col:
            st.markdown(
                f'<div class="stat-box"><div class="num">{num}</div><div class="lbl">{lbl}</div></div>',
                unsafe_allow_html=True,
            )

    st.write("")
    left, right = st.columns([2, 1])
    with left:
        st.markdown("### Our Story")
        st.write(
            "Sisters Kesa began as a small family tradition — herbal powders and oils "
            "hand-mixed at home using recipes passed down through generations. Today, "
            "we bring that same care into every pack, so you can care for your hair and "
            "skin the way nature intended: gently, effectively, and without a single "
            "harsh chemical."
        )
        bcol1, bcol2 = st.columns(2)
        with bcol1:
            if st.button("🛍️ Shop All Products", type="primary", use_container_width=True):
                go("Shop")
        with bcol2:
            if st.button("🧪 Take the Hair Care Quiz", use_container_width=True):
                go("Hair Care Quiz")
    with right:
        st.markdown('<div class="quote-box">"My hair fall reduced within 3 weeks of using the Hair Oil — and it smells amazing!" <br>— Priya, Chennai</div>', unsafe_allow_html=True)
        st.markdown('<div class="quote-box">"Finally a shampoo alternative that doesn\'t dry out my scalp." <br>— Divya, Coimbatore</div>', unsafe_allow_html=True)

    if st.session_state.recent:
        st.markdown("---")
        st.markdown("### 👀 Recently Viewed")
        rcols = st.columns(len(st.session_state.recent))
        for col, pid in zip(rcols, st.session_state.recent):
            p = get_product(pid)
            with col:
                if st.button(f"{p['icon']} {p['name']}", key=f"recent_{pid}", use_container_width=True):
                    open_quick_view(pid)
                    st.rerun()

    st.markdown("---")
    st.markdown("### ⭐ Best Sellers")
    b1, b2 = st.columns(2)
    with b1:
        render_product_card(get_product("shikkai"), key_prefix="home")
    with b2:
        render_product_card(get_product("oil"), key_prefix="home")


# --------------------------------------------------------------------------
# PAGE: SHOP
# --------------------------------------------------------------------------
def page_shop():
    st.markdown('<p class="brand-title">Shop the Collection</p>', unsafe_allow_html=True)
    st.markdown('<p class="brand-subtitle">4 handcrafted herbal essentials</p>', unsafe_allow_html=True)
    st.write("")

    search = st.text_input("🔍 Search products", placeholder="e.g. hair fall, dandruff, oil...")

    categories = ["All"] + sorted({p["category"] for p in get_products()})
    cat = st.pills("Category", categories, default="All", key="shop_cat_pills")

    sort_by = st.segmented_control(
        "Sort by",
        ["Featured", "Price: Low to High", "Price: High to Low", "Rating"],
        default="Featured",
        key="shop_sort",
    )

    filtered = get_products()
    if search:
        s = search.lower()
        filtered = [
            p for p in filtered
            if s in p["name"].lower()
            or s in p["description"].lower()
            or any(s in c.lower() for c in p["concerns"])
        ]
    if cat and cat != "All":
        filtered = [p for p in filtered if p["category"] == cat]

    if sort_by == "Price: Low to High":
        filtered = sorted(filtered, key=lambda p: p["price"])
    elif sort_by == "Price: High to Low":
        filtered = sorted(filtered, key=lambda p: -p["price"])
    elif sort_by == "Rating":
        filtered = sorted(filtered, key=lambda p: -p["rating"])

    st.write("")
    if not filtered:
        st.info("No products match your search. Try clearing the filters.")
        return

    cols = st.columns(2)
    for i, p in enumerate(filtered):
        with cols[i % 2]:
            render_product_card(p, key_prefix="shop")


# --------------------------------------------------------------------------
# PAGE: HAIR CARE QUIZ
# --------------------------------------------------------------------------
def page_quiz():
    st.markdown('<p class="brand-title">Find Your Herbal Match 🌱</p>', unsafe_allow_html=True)
    st.markdown('<p class="brand-subtitle">Answer one question and we\'ll recommend the right product for you.</p>', unsafe_allow_html=True)
    st.write("")

    choice = st.pills("What's your biggest hair or skin concern right now?", list(QUIZ_MAP.keys()), key="quiz_pills")

    if st.button("✨ Reveal My Match", type="primary", disabled=not choice):
        st.session_state.quiz_result = QUIZ_MAP[choice]
        st.snow()

    if st.session_state.quiz_result:
        p = get_product(st.session_state.quiz_result)
        st.success(f"Your match: **{p['name']}**")
        render_product_card(p, key_prefix="quiz")


# --------------------------------------------------------------------------
# PAGE: WISHLIST
# --------------------------------------------------------------------------
def page_wishlist():
    st.markdown('<p class="brand-title">Your Wishlist ❤️</p>', unsafe_allow_html=True)
    st.write("")

    if not st.session_state.wishlist:
        st.info("Nothing here yet — tap the 🤍 on any product to save it.")
        if st.button("🛍️ Go to Shop"):
            go("Shop")
        return

    cols = st.columns(2)
    for i, pid in enumerate(st.session_state.wishlist):
        with cols[i % 2]:
            render_product_card(get_product(pid), key_prefix="wish")


# --------------------------------------------------------------------------
# PAGE: CART
# --------------------------------------------------------------------------
def page_cart():
    st.markdown('<p class="brand-title">Your Cart 🛒</p>', unsafe_allow_html=True)
    st.write("")

    if cart_count() == 0:
        st.info("Your cart is empty. Head to the shop to add some herbal goodness!")
        if st.button("🛍️ Go to Shop"):
            go("Shop")
        return

    to_remove = None
    for pid, qty in list(st.session_state.cart.items()):
        p = get_product(pid)
        c1, c2, c3, c4 = st.columns([0.6, 3, 1.3, 1])
        with c1:
            st.markdown(f"<div style='font-size:2rem'>{p['icon']}</div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"**{p['name']}**")
            st.caption(f"{format_price(p['price'])} · {p['unit']}")
        with c3:
            new_qty = st.number_input(
                "Qty", min_value=1, max_value=10, value=qty, step=1,
                key=f"cart_qty_{pid}", label_visibility="collapsed",
            )
            if new_qty != qty:
                st.session_state.cart[pid] = new_qty
                st.rerun()
        with c4:
            st.markdown(f"**{format_price(p['price'] * qty)}**")
            if st.button("Remove", key=f"remove_{pid}"):
                to_remove = pid
        st.markdown("---")

    if to_remove:
        del st.session_state.cart[to_remove]
        st.rerun()

    subtotal = cart_subtotal()
    shipping = 0 if subtotal >= FREE_SHIPPING_THRESHOLD else 49
    total = subtotal + shipping

    s1, s2 = st.columns([2, 1])
    with s1:
        st.markdown("#### Free Shipping Progress")
        remaining = FREE_SHIPPING_THRESHOLD - subtotal
        st.progress(min(subtotal / FREE_SHIPPING_THRESHOLD, 1.0))
        if remaining > 0:
            st.caption(f"Add {format_price(remaining)} more to unlock free shipping 🚚")
        else:
            st.caption("You've unlocked free shipping! 🎉")
    with s2:
        st.markdown("#### Order Summary")
        st.write(f"Subtotal: {format_price(subtotal)}")
        st.write(f"Shipping: {'FREE 🎉' if shipping == 0 else format_price(shipping)}")
        st.markdown(f"### Total: {format_price(total)}")
        if st.button("Proceed to Checkout →", type="primary", use_container_width=True):
            go("Checkout")


# --------------------------------------------------------------------------
# PAGE: CHECKOUT
# --------------------------------------------------------------------------
def page_checkout():
    st.markdown('<p class="brand-title">Checkout 🌿</p>', unsafe_allow_html=True)
    st.write("")

    if cart_count() == 0 and not st.session_state.last_order:
        st.info("Your cart is empty.")
        if st.button("🛍️ Go to Shop"):
            go("Shop")
        return

    if cart_count() > 0:
        with st.form("checkout_form"):
            st.markdown("#### Delivery Details")
            c1, c2 = st.columns(2)
            with c1:
                name = st.text_input("Full Name *")
                phone = st.text_input("Phone Number *")
                pincode = st.text_input("Pincode *")
            with c2:
                email = st.text_input("Email")
                city = st.text_input("City *")
                address = st.text_area("Address *", height=70)

            st.markdown("#### Payment Method")
            payment = st.radio("Choose payment method", ["Cash on Delivery", "UPI", "Card"], horizontal=True)

            st.markdown("#### Order Summary")
            subtotal = cart_subtotal()
            shipping = 0 if subtotal >= FREE_SHIPPING_THRESHOLD else 49
            total = subtotal + shipping
            for pid, qty in st.session_state.cart.items():
                p = get_product(pid)
                st.write(f"{p['icon']} {p['name']} × {qty} — {format_price(p['price'] * qty)}")
            st.write(f"Shipping: {'FREE' if shipping == 0 else format_price(shipping)}")
            st.markdown(f"**Total: {format_price(total)}**")

            submitted = st.form_submit_button("✅ Place Order", type="primary", use_container_width=True)

            if submitted:
                if not (name and phone and pincode and city and address):
                    st.error("Please fill in all required fields (*).")
                else:
                    order_id = "SK-" + "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
                    st.session_state.last_order = {
                        "id": order_id,
                        "name": name,
                        "total": total,
                        "items": dict(st.session_state.cart),
                        "date": datetime.now().strftime("%d %b %Y, %I:%M %p"),
                        "payment": payment,
                    }
                    st.session_state.cart = {}
                    st.rerun()

    if st.session_state.last_order:
        order = st.session_state.last_order
        st.balloons()
        st.success(f"🎉 Order placed successfully! Order ID: **{order['id']}**")
        st.write(f"Thank you, **{order['name']}**! Your herbal goodies are on their way.")
        st.caption(f"Placed on {order['date']} · Paying via {order['payment']}")
        st.markdown(f"### Total Paid: {format_price(order['total'])}")
        if st.button("Continue Shopping"):
            st.session_state.last_order = None
            go("Shop")


# --------------------------------------------------------------------------
# PAGE: ABOUT & CONTACT
# --------------------------------------------------------------------------
def page_about():
    st.markdown('<p class="brand-title">About Sisters Kesa 🌿</p>', unsafe_allow_html=True)
    st.write("")

    st.write(
        "Sisters Kesa is a small herbal care brand built on a simple belief: your "
        "hair and skin deserve ingredients you can actually recognize. Every "
        "product we make follows traditional South Indian recipes — Shikakai, "
        "Reetha, Amla, Hibiscus, Bhringraj — sourced naturally and blended in "
        "small batches, with no sulphates, parabens, or synthetic fragrance."
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 🌱 100% Natural")
        st.caption("No chemicals, no shortcuts — just herbs, the way it's always been done.")
    with c2:
        st.markdown("#### 👵 Traditional Recipes")
        st.caption("Formulas passed down through generations of home remedies.")
    with c3:
        st.markdown("#### 🤝 Small Batch, Made with Care")
        st.caption("Freshly prepared, not mass-manufactured.")

    st.markdown("---")
    st.markdown("### Get in Touch")
    with st.form("contact_form"):
        c1, c2 = st.columns(2)
        with c1:
            cname = st.text_input("Your Name")
        with c2:
            cemail = st.text_input("Your Email")
        message = st.text_area("Message", height=100)
        sent = st.form_submit_button("Send Message", type="primary")
        if sent:
            if cname and message:
                st.success("Thank you for reaching out! We'll get back to you soon. 🌿")
            else:
                st.error("Please add your name and a message.")

    st.markdown("---")
    st.caption("📍 Tamil Nadu, India  ·  📞 +91 00000 00000  ·  ✉️ hello@sisterskesa.demo")
    st.caption("This is a demo storefront built with Streamlit — product data is illustrative.")


# --------------------------------------------------------------------------
# ROUTER
# --------------------------------------------------------------------------
PAGES = {
    "Home": page_home,
    "Shop": page_shop,
    "Hair Care Quiz": page_quiz,
    "Wishlist": page_wishlist,
    "Cart": page_cart,
    "Checkout": page_checkout,
    "About & Contact": page_about,
}

PAGES[st.session_state.nav]()
