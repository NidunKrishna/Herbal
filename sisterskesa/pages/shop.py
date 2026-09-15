import streamlit as st
from components.ui import html, e
from components.breadcrumbs import breadcrumbs
from components.filters import filter_drawer
from components.product_grid import product_grid
from services.catalog_service import get_products
from services.filter_service import filter_products, sort_products, active_count
from data.categories import CATEGORIES
from utils.navigation import nav_button

def render(category: str = "all") -> None:
    if category != "all" and category not in CATEGORIES:
        st.warning("This category is not in our edit.")
        nav_button("Explore all products", "shop", "category_notfound")
        return
    st.session_state.active_category = category
    new_only = st.query_params.get("edit") == "new"
    st.session_state.new_only = new_only
    with st.container(key="shop"):
        breadcrumbs(CATEGORIES[category]["name"] if category != "all" else "Products")
        title = "New to <em>the shelf.</em>" if new_only else "A considered <em>edit.</em>" if category == "all" else CATEGORIES[category]["name"]+"<em>, considered.</em>"
        copy = CATEGORIES[category]["copy"] if category != "all" else "Herbs at the heart of skin, hair and body care. Discover your own everyday ritual."
        html(f'<div class="shop-heading"><div><p class="eyebrow">THE HERBAL COLLECTION</p><h1>{title}</h1></div><p>{e(copy)}</p></div>')
        with st.container(key="categorynav"):
            cols = st.columns(len(CATEGORIES) + 1)
            for col, (slug, cat) in zip(cols, [("all", {"name":"All products"}), *CATEGORIES.items()]):
                n = sum(1 for p in get_products() if slug == "all" or p.category == slug)
                with col: nav_button(f"{cat['name']} ({n})", "shop" if slug == "all" else "category/"+slug, "tab_"+slug, primary=slug == category)
        a, b, c = st.columns([1.2, 2.8, 2], vertical_alignment="center")
        with a:
            if st.button(f"Filters ({active_count(st.session_state.filters)})  +", use_container_width=True):
                filter_drawer(category, new_only)
        with c:
            sort = st.selectbox("Sort by", ("Our favourites", "Price: low to high", "Price: high to low", "Top rated", "Newest"), label_visibility="collapsed")
        products = sort_products(filter_products(get_products(), st.session_state.filters, category, new_only), sort)
        with b: st.caption(f"{len(products)} considered discoveries")
        if active_count(st.session_state.filters):
            selected = [str(v) for k, vals in st.session_state.filters.items() if k != "price" for v in vals]
            if tuple(st.session_state.filters.get("price", (10,320))) != (10,320):
                lo, hi = st.session_state.filters["price"]
                selected.append(f"${lo}–${hi}")
            html('<div class="active-filters">'+''.join(f'<span>{e(v)}</span>' for v in selected)+'</div>')
            if st.button("Clear filters", key="clear_shop_filters"):
                st.session_state.filters = {}
                st.session_state.filter_version = st.session_state.get("filter_version", 0)+1
                st.rerun()
        if products:
            product_grid(products, "shop", editorial=True)
        else:
            html('<div class="empty-state"><h2>A little too specific?</h2><p>Try clearing a filter to discover more of the edit.</p></div>')
