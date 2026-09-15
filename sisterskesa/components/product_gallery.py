import streamlit as st
from components.ui import html, photo

def product_gallery(product) -> None:
    selection = st.session_state.get("gallery_"+product.id, "The product")
    labels = ("The product", "Texture study", "Botanical study")
    asset = product.gallery_images[labels.index(selection)]
    html(photo(asset, css="detail-photo", eager=True))
    st.radio("Explore the gallery", labels, horizontal=True, key="gallery_"+product.id, label_visibility="collapsed")
    html('<p class="gallery-caption">Illustrative product photography and texture / botanical studies.</p>')
