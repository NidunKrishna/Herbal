import streamlit as st

def navigate(route: str, **query: str) -> None:
    st.query_params.clear()
    st.query_params["view"] = route
    for key, value in query.items():
        st.query_params[key] = value
    st.session_state.search_open = False

def go(route: str, **query: str) -> None:
    navigate(route, **query)
    st.rerun()

def nav_button(label: str, route: str, key: str, *, primary: bool = False, **query: str) -> None:
    st.button(label, key=key, on_click=navigate, args=(route,), kwargs=query, type="primary" if primary else "secondary", use_container_width=True)
