import streamlit as st

def initialize() -> None:
    if st.session_state.get("catalogue_version") != "herbal-1":
        st.session_state.update(cart={}, filters={}, order=None, search_query="", catalogue_version="herbal-1")
    defaults = {"cart": {}, "filters": {}, "active_category": "all", "current_product": None, "search_open": False, "search_query": "", "new_only": False, "newsletter_emails": [], "order": None}
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
