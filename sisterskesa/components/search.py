import streamlit as st
from services.catalog_service import get_products
from services.search_service import search_products
from components.ui import html, e
from utils.navigation import go

def search_contents() -> None:
    query = st.text_input("Find something for your shelf", value=st.session_state.search_query, placeholder="Try hibiscus, tulsi or hair oil", key="search_input")
    st.session_state.search_query = query
    results = search_products(get_products(), query) if query.strip() else []
    if not query.strip():
        html('<p class="muted">A few good places to start: hibiscus, tulsi, hair oil, herbal baths.</p>')
    elif not results:
        st.info("No discoveries just yet. Try a product, ingredient or care goal.")
    else:
        st.caption(f"{len(results)} discoveries")
        for p in results:
            if st.button(f"{p.name} — {p.brand}  ↗", key="search_"+p.id, use_container_width=True):
                go("product/"+p.slug)

@st.dialog("Find your next favourite", width="large")
def search_dialog() -> None:
    st.session_state.search_open = True
    search_contents()
