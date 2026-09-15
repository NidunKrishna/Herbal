from html import escape
import streamlit as st
from services.media_service import get_media, media_alt

def html(value: str) -> None:
    st.html(value)

def e(value: object) -> str:
    return escape(str(value), quote=True)

def photo(asset_id: str, *, css: str = "editorial-photo", eager: bool = False) -> str:
    return f'<img class="{e(css)}" src="{e(get_media(asset_id))}" alt="{e(media_alt(asset_id))}" loading="{"eager" if eager else "lazy"}" decoding="async" />'

def heading(label: str, title: str, copy: str = "") -> None:
    html(f'<div class="section-heading"><p class="eyebrow">{e(label)}</p><h2>{title}</h2>{f"<p>{e(copy)}</p>" if copy else ""}</div>')
