from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parent
st.set_page_config(page_title="sisterskesa | Authentic herbal care", page_icon=str(ROOT/"assets/icons/favicon.svg"), layout="wide", initial_sidebar_state="collapsed")
from utils.session import initialize
from components.navbar import navbar
from components.footer import footer

initialize()
css_files = ("globals", "typography", "navbar", "home", "products", "product_detail", "filters", "cart", "animations", "responsive")
st.html("<style>"+"\n".join((ROOT/"styles"/(name+".css")).read_text(encoding="utf-8") for name in css_files)+"</style>")
navbar()
route = st.query_params.get("view", "home").strip("/") or "home"
if route == "home":
    from pages.home import render
    render()
elif route == "shop":
    from pages.shop import render
    render()
elif route.startswith("category/"):
    from pages.category import render
    render(route.split("/",1)[1])
elif route.startswith("product/"):
    from pages.product_detail import render
    render(route.split("/",1)[1])
elif route == "about":
    from pages.about import render
    render()
elif route == "journal" or route.startswith("journal/"):
    from pages.journal import render
    render(route.split("/",1)[1] if "/" in route else "")
elif route == "cart":
    from pages.cart import render
    render()
elif route == "checkout":
    from pages.checkout import render
    render()
elif route == "search":
    from components.search import search_contents
    with st.container(key="searchpage"):
        st.title("Find your next favourite")
        search_contents()
elif route.startswith("help/"):
    from pages.help import render
    render(route.split("/",1)[1])
else:
    st.title("This page is off the shelf.")
    from utils.navigation import nav_button
    nav_button("Return home", "home", "not_found_home")
footer()
