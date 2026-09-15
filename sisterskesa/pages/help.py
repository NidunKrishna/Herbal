import streamlit as st
from components.ui import html, e
from components.breadcrumbs import breadcrumbs
from utils.navigation import nav_button

CONTENT = {
 "shipping": ("A little closer to your shelf.", "In this demo, standard shipping is $6 and is complimentary on orders of $85 or more after discounts. These are sample rates in USD. No orders are shipped; delivery timing and real rates will be confirmed before launch."),
 "returns": ("Care, beyond the shelf.", "This is a demonstration storefront, so no purchases or returns are processed. A complete returns policy will be published before real orders are accepted."),
 "privacy": ("A little care for your information.", "This demo stores your bag, checkout selections and preview newsletter signup only in the current Streamlit session. No payment details are requested. No email is sent. Reloading or closing the session may clear this information. Bundled images load locally; Google Fonts may contact Google, and remote image fallbacks may contact Pexels if a local file is removed. Use sample information while exploring checkout."),
 "contact": ("We’re glad you’re here.", "sisterskesa is a preview storefront. A contact address has not been configured yet. Contact details for Bhuvana and Radhika will be added before launch."),
 "social": ("Good things, shared.", "Our social profiles will be linked here when sisterskesa launches. For now, explore the journal for rituals and discoveries from our shared shelf."),
}

def render(topic: str) -> None:
    with st.container(key="helppage"):
        breadcrumbs(topic.title())
        if topic == "faq":
            html('<h1>A few <em>good questions.</em></h1>')
            for q, a in [("Can I place a real order?", "This is a demo. You can explore the complete shopping flow, but no payment is taken or product shipped."),("How do subscriptions work?", "Choose a size, subscribe to save 15%, and select every month, six weeks or two months. These selections are saved in your session bag. No recurring charges are created."),("Will my bag be saved?", "Your bag stays with you while navigating within this browser session using the site’s buttons. A full reload or new tab starts a new session."),("Are the products and reviews real?", "The products, brands, ingredient lists and review counts are fictional demonstration content. Photographs are illustrative licensed stock imagery."),("How is travel-size pricing calculated?", "The second size uses 65% of the full-size price, rounded to cents. Subscription savings apply after any sale and size adjustment.")]:
                with st.expander(q): st.write(a)
        else:
            title, body = CONTENT.get(topic, ("Off the shelf.", "We couldn’t find that page."))
            html(f'<div class="article-section"><p class="eyebrow">SISTERSKESA / {e(topic.upper())}</p><h1>{e(title)}</h1><p>{e(body)}</p></div>')
        nav_button("BACK TO THE EDIT  ↗", "shop", "help_shop")
