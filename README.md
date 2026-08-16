# Sisters Kesa — Herbal Storefront (Streamlit Demo)

A creative, interactive storefront demo for the **Sisters Kesa** herbal hair &
body care line, built entirely in Streamlit.

## Products
- Sisters Kesa Shikkai Powder
- Sisters Kesa Hair Oil
- Sisters Kesa Nalangu Maavu
- Sisters Kesa Hair Pack

Prices, images (emoji/icon placeholders), and descriptions are demo
placeholders — swap them for real data whenever you're ready.

## Features
- Home page with brand story, stats, testimonials, best sellers
- Shop page with search, category filter, and sorting
- "Find Your Herbal Match" interactive quiz
- Persistent shopping cart (add/update qty/remove) via the sidebar
- Demo checkout flow with order confirmation
- About & Contact page with a contact form

## Run it

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the local URL Streamlit prints (usually http://localhost:8501).

## Customize
All product data lives in the `PRODUCTS` list near the top of `app.py` —
update names, prices, descriptions, or add real product photos (swap the
emoji `icon` for `st.image(...)` calls) whenever you have real assets.
