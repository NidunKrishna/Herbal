import streamlit as st
from data.journal import ARTICLES
from components.ui import html, photo, heading, e
from components.breadcrumbs import breadcrumbs
from utils.navigation import nav_button

def journal_cards(key: str) -> None:
    with st.container(key="journalcards_"+key):
        cols = st.columns(3, gap="large")
        for col, article in zip(cols, ARTICLES):
            with col:
                html(f'<article class="journal-card">{photo(article["image"])}<p class="eyebrow">{e(article["category"])} · {article["minutes"]} MIN READ</p><h3>{e(article["title"])}</h3></article>')
                nav_button("READ THE STORY  ↗", "journal/"+article["slug"], key+article["slug"])

def render(slug: str = "") -> None:
    with st.container(key="journalpage"):
        if slug:
            article = next((a for a in ARTICLES if a["slug"] == slug), None)
            if not article:
                st.warning("We couldn’t find that story.")
                nav_button("Back to the journal", "journal", "journal_missing")
                return
            breadcrumbs("Journal / "+article["title"])
            html(f'<header class="article-heading"><p class="eyebrow">{e(article["category"])} · {article["minutes"]} MIN READ</p><h1>{e(article["title"])}</h1><p>{e(article["intro"])}</p></header>{photo(article["image"],css="article-image")}')
            for title, body in article["sections"]:
                html(f'<section class="article-section"><h2>{e(title)}</h2><p>{e(body)}</p></section>')
            nav_button("MORE FROM THE JOURNAL  ↗", "journal", "journal_back")
        else:
            breadcrumbs("Journal")
            heading("NOTES FROM OUR SHELF", "sisterskesa’s <em>Journal.</em>", "Rituals, discoveries and a few things worth passing on.")
            journal_cards("journal")
