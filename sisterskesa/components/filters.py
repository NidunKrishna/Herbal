import streamlit as st
from services.filter_service import FILTER_OPTIONS, FILTER_LABELS, filter_products
from services.catalog_service import get_products

@st.dialog("A more personal edit", width="large")
def filter_drawer(category: str, new_only: bool = False) -> None:
    st.html('<span class="filter-drawer-marker"></span>')
    st.caption("Choose what matters to you. Options within a group match any selection; botanical composition matches all selections.")
    version = st.session_state.get("filter_version", 0)
    draft = {}
    for field, options in FILTER_OPTIONS.items():
        draft[field] = st.multiselect(FILTER_LABELS[field], options, default=st.session_state.filters.get(field, []), key=f"filter_{version}_{field}")
    draft["price"] = st.slider("Price range (USD)", 10, 320, tuple(st.session_state.filters.get("price", (10, 320))), key=f"price_{version}")
    count = len(filter_products(get_products(), draft, category, new_only))
    a, b = st.columns([1, 2])
    with a:
        if st.button("CLEAR ALL", use_container_width=True):
            st.session_state.filters = {}
            st.session_state.filter_version = version+1
            st.rerun()
    with b:
        if st.button(f"SHOW RESULTS ({count})", type="primary", use_container_width=True):
            st.session_state.filters = draft
            st.rerun()
