# SISTERSKESA

A complete Python-first editorial herbal-care storefront for Bhuvana and Radhika from Kumbakonam, Tamil Nadu. Built with Streamlit, custom CSS, a typed fictional catalogue, and locally bundled Pexels photography.

## Quick start

Requires Python 3.11 or later (tested with Python 3.12 and Streamlit 1.43.1).

```sh
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```bat
.venv\Scripts\activate
```

macOS / Linux:

```sh
source .venv/bin/activate
```

Install and launch from this project folder:

```sh
pip install -r requirements.txt
streamlit run app.py
```

Open the local URL printed by Streamlit, usually http://localhost:8501.

## What works

- Editorial homepage with full photographic hero, philosophy, expandable categories, eight favourites, founder story, body edit, three journal stories and newsletter form.
- 21 fictional herbal products across skincare, hair care, body rituals and wellness.
- Category browsing, new arrivals, price/rating sorting, search, and a right-side filter drawer that becomes full width on mobile.
- Search matches product name, brand, category, care goals, ingredients and tags; multiple words must all match.
- Filtering uses OR within most groups and AND between groups. Selected botanical composition tags must all match. In Stock includes Limited Edition.
- Product galleries, size choices, 15% subscription savings and delivery frequency, quantity selection, product tabs, key ingredients, how-to sections, cross-sells and related products.
- Session bag with variant-specific lines, quantity changes, removal, subtotal, savings and shipping progress.
- Validated demo checkout and downloadable JSON receipt. Completing it clears the bag and retains the demo confirmation in the same session.
- Readable mobile navigation, intentional image crops, single-column phone products, two-column intermediate grids, keyboard controls, visible focus and reduced-motion support.
- Empty states, unavailable products, invalid routes, search with no results and form validation.

## Demonstration boundaries

The storefront experience is complete; this is **not a live commerce backend**. Checkout does not collect card information, charge money, activate subscriptions, send email, calculate tax, reserve inventory or arrange shipping. The newsletter confirms a session-only preview signup and does not connect to a mailing service. Contact/social destinations clearly indicate that brand details have not yet been configured.

The brand name and founder hometown follow the supplied story. Product formulas, reviews, prices, ingredient tags and commercial terms remain fictional sample content until approved by the brand. Ingredient lists are illustrative, not full INCI disclosures. All photographs are illustrative stock images. Herbal preparation photographs do not depict the actual founders or their production facility. Founder notes are draft brand copy based on the supplied narrative, not verified quotations. Some products share representative botanical photography. Herbal preparations are illustrative; they do not show the actual founders or production facility.

Navigation uses native Streamlit button callbacks so the WebSocket session—and bag—survives in-app navigation. A full browser reload, direct URL navigation, new tab, or server restart can create a new session and reset the bag. The app does not use persistent browser storage or a database. Demo personal details stay in session memory; use sample details while testing.

Before accepting real orders, integrate a payment provider with verified webhooks, durable order/inventory storage, genuine product and ingredient data, transactional email, newsletter consent storage and unsubscribe handling, taxes and shipping, reviewed policies and brand contact/social links. Configure HTTPS and a Python host with WebSocket support. The supplied Dockerfile can run this Streamlit application; static-only hosting cannot run it.

## Architecture

`app.py` is a small shell that loads the theme, initializes state, renders the header/footer and dispatches a view. Pages compose reusable components. Services own catalogue, filtering, search, media, pricing and checkout behavior. Data stays separate from presentation.

```text
sisterskesa/
├── app.py
├── requirements.txt
├── README.md
├── Dockerfile
├── .streamlit/config.toml
├── assets/
│   ├── MEDIA_GUIDE.md
│   ├── CREDITS.md
│   ├── images/{hero,products,categories,editorial,founders,journal,ingredients,backgrounds}/
│   ├── video/{hero,products,editorial}/
│   ├── icons/favicon.svg
│   ├── logos/
│   ├── fonts/
│   └── placeholders/image.svg
├── data/{products,categories,journal,founders,media_manifest}.py
│   └── media.json
├── pages/{home,shop,product_detail,category,about,journal,cart,checkout,help}.py
├── components/
│   ├── navbar.py, mobile_nav.py, hero.py, category_strip.py
│   ├── product_card.py, product_grid.py, product_gallery.py
│   ├── filters.py, search.py, cart_drawer.py, order_summary.py
│   └── newsletter.py, editorial_section.py, footer.py, breadcrumbs.py, badges.py, ui.py
├── services/{catalog,cart,search,filter,media,checkout}_service.py
├── utils/{navigation,formatting,session,helpers}.py
├── styles/{globals,typography,navbar,home,products,product_detail,filters,cart,responsive,animations}.css
├── scripts/fetch_media.py
└── tests/{test_services,test_app}.py
```

The optional mini-bag component is available in `components/cart_drawer.py`; the main interface uses the full bag route and inline add confirmation.

### Routing

Streamlit uses query parameters rather than a separate server framework:

| Requested view | URL |
| --- | --- |
| Home | `/?view=home` or `/` |
| Shop | `/?view=shop` |
| New arrivals | `/?view=shop&edit=new` |
| Category | `/?view=category/skincare` (also hair-care, body-rituals, wellness) |
| Product | `/?view=product/manjal-rose-face-powder` |
| About | `/?view=about` |
| Journal | `/?view=journal` |
| Article | `/?view=journal/the-morning-shelf` |
| Search | `/?view=search` |
| Bag | `/?view=cart` |
| Checkout | `/?view=checkout` |

Use `nav_button()` or `navigate()` from `utils/navigation.py` for new in-app routes. Avoid HTML/Markdown navigation links, which reset Streamlit session state.

### Add or edit products

Edit `data/products.py`. `Product` is a frozen dataclass with every requested field. The `ROWS` seed tuples populate the typed objects; field order is documented immediately above the rows. `_build()` provides sample ratings, flags and badges from explicit stable IDs. For a live catalogue replace the seed builder with explicit verified product records, retaining the dataclass interface. Ensure IDs and slugs remain unique; keep existing stable IDs when changing the collection.

To add a product, add one row with an existing category slug, valid image ID, both size labels and all content. Update `FILTER_OPTIONS` when introducing a new product type or texture. Availability may be `In Stock`, `Limited Edition`, or `Out of Stock`.

### Prices and subscriptions

Prices use USD. `services/cart_service.py` calculates money with Decimal and half-up rounding. The second size is a sample travel size priced at 65% of the full-size price. Subscription discount is 15% after the sale price and size adjustment. For example, $41.50 × 85% rounds to **$35.28**. Sale and subscription discounts combine. Free shipping starts at $85 after discounts; below that shipping is $6. Savings are measured against the selected size's full retail price. Edit these rules centrally in that service.

### Replace photographs

See `assets/MEDIA_GUIDE.md`. All mappings and URLs live in `data/media.json`, loaded through `data/media_manifest.py`. Replace the local file or change its manifest path and alt text. Pages request IDs through `get_media()`, never raw URLs. The helper prefers a local WebP sibling, then the configured local image, then its HTTPS fallback, then the local placeholder. Local image data is cached using modification times and delivered as data URLs. No image downloads occur on application reruns.

Bundled images are already downloaded. To restore missing files:

```sh
python scripts/fetch_media.py
```

This opt-in script needs network access. It skips existing files. Remove only the specific file you intend to replace before fetching again. Credit and source links are recorded in both the manifest and `assets/CREDITS.md`.

### Add categories

Add the slug, display name, copy and image ID to `data/categories.py`; associate product rows with that slug. Header/footer/category selectors derive from these definitions. If increasing the number of categories, the selector in `pages/shop.py` derives its column count automatically; check the mobile layout in `styles/responsive.css`.

### Add journal articles

Append a dictionary to `ARTICLES` in `data/journal.py`: `slug`, `title`, `category`, `minutes`, `image`, `intro` and a list of `(heading, body)` sections. The journal currently shows three cards using three columns; update `journal_cards()` to iterate in rows when adding more articles.

### Colours, fonts and spacing

Core CSS variables live in `styles/globals.css`; keep `.streamlit/config.toml` aligned. Headlines use Cormorant Garamond and body copy uses DM Sans. Google Fonts loads the fonts, with Georgia/Arial fallbacks. For completely offline typography, supply licensed WOFF2 files under `assets/fonts/`, serve them with a trusted static configuration, and replace the Google import with `@font-face` rules. Images already work offline.

Responsive styles cover 1440, 1200, 992, 768 and 480 pixels. Typography uses `clamp()`. Styling targets stable Streamlit test IDs and explicit container keys where available. Recheck the UI before changing the pinned Streamlit version, since generated markup may change.

## Verification

From the project root:

```sh
python -m unittest discover -s tests -v
```

15 tests cover the catalogue, pricing/rounding, variants, stock validation, quantities, shipping, savings, search, filters, sorting, media availability, route rendering, newsletter validation and demo checkout. The route test includes all main route variants. Streamlit's AppTest does not reproduce browser fragment reruns; the filter test uses a small direct-dialog harness, and the actual drawer was also tested in-browser.

Browser QA covered a 1440-pixel desktop homepage and filter drawer, and a 390-pixel mobile homepage, navigation, category, product selection and bag. Both inspected mobile views reported no horizontal overflow. The oil texture filter updates to match the herbal catalogue. The mobile add-to-bag flow updated the bag count and navigated to the correct item.

## Container run

```sh
docker build -t sisterskesa .
docker run --rm -p 8501:8501 sisterskesa
```

The container uses Python 3.12, a non-root user, and a Streamlit health check. Keep the app behind HTTPS for a real deployment. For local development, use the normal Streamlit command above.

## Herbal brand direction

sisterskesa is presented as the authentic herbal-care vision of Bhuvana and Radhika from Kumbakonam, Tamil Nadu. The copy uses botanical and herbal language without claiming that natural ingredients are chemical-free, automatically safe, certified, or clinically effective. The previous colour-cosmetics category and its products have been removed.

Latest verification: herbal rebrand checked at 1440px desktop and 390px phone width; homepage contained no previous founder names or colour-cosmetics category. All 15 tests passed from a fresh Python environment installed from requirements.txt.
