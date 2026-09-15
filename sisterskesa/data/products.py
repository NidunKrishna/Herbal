"""Fictional botanical demonstration catalogue. Prices are USD; ratings are sample data."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    id: str
    slug: str
    brand: str
    name: str
    category: str
    subcategory: str
    description: str
    long_description: str
    price: float
    sale_price: float | None
    sizes: tuple[str, ...]
    rating: float
    review_count: int
    badges: tuple[str, ...]
    ingredients: tuple[str, ...]
    benefits: tuple[str, ...]
    how_to_use: str
    texture: str
    fragrance_profile: str
    values: tuple[str, ...]
    care_goals: tuple[str, ...]
    availability: str
    featured: bool
    new_arrival: bool
    bestseller: bool
    sisters_pick: bool
    image: str
    gallery_images: tuple[str, ...]
    tags: tuple[str, ...]


# Stable ID, name, category, type, price, sizes, texture, fragrance, ingredients,
# ritual, descriptor, usage, image. Retired IDs p009-p012 are intentionally unused.
ROWS = [
    ("p001", "Manjal & Rose Face Powder", "skincare", "Face Powder", 41.50, ("50 g", "30 g"), "Powder", "Floral", ("Kasturi turmeric", "Rose petals", "Green gram"), ("Face Ritual", "Fresh Start"), "A little rose. A little manjal. A moment for you.", "Mix a small amount with water into a paste. Massage lightly onto wet skin and rinse. Mix fresh each time and keep the jar dry.", "product_balm"),
    ("p002", "Hibiscus Face Oil", "skincare", "Face Oil", 68, ("30 ml", "15 ml"), "Oil", "Herbal", ("Sesame oil", "Hibiscus flowers"), ("Face Ritual",), "A flower-led ritual for unhurried evenings.", "Warm one or two drops between palms and press onto clean skin, avoiding the eye area.", "product_serum"),
    ("p003", "Green Gram Face Cleanser", "skincare", "Powder Cleanser", 32, ("100 g", "50 g"), "Powder", "Earthy", ("Green gram", "Rose petals", "Vetiver root"), ("Face Ritual", "Fresh Start"), "An earthy beginning, with petals in the mix.", "Combine a small spoonful with water. Massage lightly onto wet skin, then rinse. Prepare only what you need and keep the jar dry.", "product_soak"),
    ("p004", "Rose Hydrosol Mist", "skincare", "Face Mist", 28, ("100 ml", "50 ml"), "Mist / Spray", "Floral", ("Rose hydrosol",), ("Face Ritual",), "The quiet beauty of a rose-water pause.", "Close eyes and mist lightly from a comfortable distance. Store as directed on the final product label.", "product_mist"),
    ("p005", "Rosehip & Sesame Face Oil", "skincare", "Face Oil", 54, ("30 ml", "15 ml"), "Oil", "Nutty", ("Rosehip seed oil", "Sesame oil"), ("Face Ritual",), "Two botanical oils, one slow evening ritual.", "Press one or two drops onto clean skin with fingertips, avoiding the eye area.", "product_oil"),
    ("p006", "Oat & Rose Cleansing Powder", "skincare", "Powder Cleanser", 29, ("100 g", "50 g"), "Powder", "Floral", ("Oat flour", "Rose petals", "Green gram"), ("Face Ritual", "Fresh Start"), "Petal pink meets the simplicity of oats.", "Mix a small spoonful with water immediately before use. Massage lightly onto wet skin and rinse. Keep the remaining powder dry.", "product_balm"),
    ("p007", "Neem & Tulsi Face Mask", "skincare", "Powder Mask", 46, ("60 g", "30 g"), "Powder", "Herbal", ("Neem leaves", "Tulsi leaves", "Green gram"), ("Face Ritual", "Slow Evenings"), "Leaf by leaf, a moment to slow down.", "Mix a little powder with water and spread a thin layer over clean skin. Rinse before it dries completely. Use the mixed paste immediately.", "product_balm"),
    ("p008", "Sandalwood Ritual Powder", "skincare", "Face Powder", 38, ("50 g", "25 g"), "Powder", "Woody", ("Sandalwood", "Rose petals", "Green gram"), ("Face Ritual", "Slow Evenings"), "A woody, floral note for your evening shelf.", "Mix a small amount with water. Apply briefly to clean skin and rinse before dry. Prepare fresh for each use; keep the jar dry.", "product_soak"),
    ("p013", "Hibiscus & Coconut Hair Oil", "hair-care", "Hair Oil", 39, ("100 ml", "50 ml"), "Oil", "Herbal", ("Coconut oil", "Hibiscus flowers", "Curry leaves"), ("Hair Ritual",), "A familiar flower, a favourite hair-oiling ritual.", "Work a small amount through hair lengths before washing. Comb through and wash out with your usual hair cleanser.", "product_oil"),
    ("p014", "Bhringraj & Amla Scalp Oil", "hair-care", "Scalp Oil", 48, ("100 ml", "50 ml"), "Oil", "Herbal", ("Sesame oil", "Bhringraj", "Amla"), ("Hair Ritual", "Scalp Ritual"), "Rooted in the ritual of an unhurried head massage.", "Part hair and massage a small amount onto the scalp before washing. Avoid broken or irritated skin and wash out thoroughly.", "product_serum"),
    ("p015", "Shikakai Hair Wash", "hair-care", "Herbal Hair Wash", 27, ("150 g", "75 g"), "Powder", "Earthy", ("Shikakai", "Soapnut", "Amla"), ("Hair Ritual", "Fresh Start"), "A powder ritual with shikakai at its heart.", "Mix with water into a loose paste immediately before use. Work through wet hair and rinse thoroughly, keeping the mixture away from eyes.", "product_soak"),
    ("p016", "Fenugreek & Hibiscus Hair Mask", "hair-care", "Hair Mask", 30, ("150 g", "75 g"), "Powder", "Herbal", ("Fenugreek seeds", "Hibiscus flowers", "Amla"), ("Hair Ritual", "Slow Evenings"), "A bowl, a few herbs, a little time for yourself.", "Mix with water into a paste. Apply to wet hair lengths before washing and rinse thoroughly. Discard any leftover mixed paste.", "product_balm"),
    ("p017", "Vetiver Body Oil", "body-rituals", "Body Oil", 44, ("100 ml", "50 ml"), "Oil", "Woody", ("Sesame oil", "Vetiver root"), ("Body Ritual", "Slow Evenings"), "Earthy vetiver for the pause after a bath.", "Massage a small amount over damp body skin after bathing. Allow to absorb before dressing.", "product_oil"),
    ("p018", "Sesame & Coconut Hand Oil", "body-rituals", "Hand Oil", 19, ("50 ml", "30 ml"), "Oil", "Nutty", ("Sesame oil", "Coconut oil"), ("Body Ritual",), "A small everyday ritual for busy hands.", "Massage a drop or two into hands and cuticles as needed.", "product_oil"),
    ("p019", "Rose & Green Gram Bath Powder", "body-rituals", "Bath Powder", 36, ("200 g", "100 g"), "Powder", "Floral", ("Rose petals", "Green gram", "Vetiver root"), ("Body Ritual", "Bathing Ritual"), "Petals and earth, ready for your bathing bowl.", "Mix with water immediately before bathing. Massage lightly onto wet body skin and rinse thoroughly. Keep the jar dry.", "product_balm"),
    ("p020", "Nalangu Bath Powder", "body-rituals", "Bath Powder", 25, ("200 g", "100 g"), "Powder", "Herbal", ("Green gram", "Kasturi turmeric", "Vetiver root", "Rose petals"), ("Body Ritual", "Bathing Ritual"), "An everyday bathing ritual, inspired by home.", "Mix a small handful with water into a paste. Massage lightly over wet body skin and rinse well. Use fresh and discard any mixed remainder.", "product_soak"),
    ("p021", "Vetiver & Rose Bath Blend", "wellness", "Botanical Bath Blend", 24, ("100 g", "50 g"), "Dried Botanicals", "Floral", ("Vetiver root", "Rose petals", "Tulsi leaves"), ("Bathing Ritual", "Slow Evenings"), "Let the bath become a little botanical ceremony.", "Place a small handful inside a muslin pouch and steep in warm bath water. Remove the pouch after use. For external use only.", "product_soak"),
    ("p022", "Rose Linen Mist", "wellness", "Linen Mist", 28, ("100 ml", "50 ml"), "Mist / Spray", "Floral", ("Rose hydrosol",), ("Slow Evenings",), "A floral finishing touch for your favourite corner.", "Mist linen lightly and allow to dry before use. Test a hidden fabric patch first. Avoid spraying directly onto the face.", "product_mist"),
    ("p023", "Vetiver Cupboard Sachet", "wellness", "Botanical Sachet", 45, ("40 g", "20 g"), "Dried Botanicals", "Woody", ("Vetiver root", "Rose petals", "Tulsi leaves"), ("Slow Evenings",), "A little garden of botanicals for your cupboard.", "Place the closed sachet in a dry cupboard or drawer, away from direct contact with delicate fabrics. Keep the contents dry.", "product_soak"),
    ("p024", "Sesame & Vetiver Bath Oil", "wellness", "Bath Oil", 38, ("150 ml", "75 ml"), "Oil", "Woody", ("Sesame oil", "Coconut oil", "Vetiver root"), ("Bathing Ritual", "Slow Evenings"), "An earthy companion to a slow evening bath.", "Add a small amount to warm bath water. Take care: oil can make the bath slippery. Clean the bath after use.", "product_oil"),
    ("p025", "Oat & Rose Body Polish", "body-rituals", "Body Polish", 33, ("200 g", "100 g"), "Powder", "Floral", ("Oat flour", "Rose petals", "Green gram"), ("Body Ritual", "Bathing Ritual"), "A petal-filled pause, from shoulders to toes.", "Mix a little powder with water. Massage lightly onto wet body skin and rinse well. Avoid broken or irritated skin; prepare fresh each time.", "product_soak"),
]


def _build(row: tuple) -> Product:
    product_id, name, category, sub, price, sizes, texture, fragrance, ingredients, goals, desc, use, image = row
    i = int(product_id[1:]) - 1
    featured = product_id in ("p001", "p002", "p003", "p004", "p013", "p017", "p020", "p021")
    new = product_id in ("p004", "p008", "p014", "p024")
    best = product_id in ("p001", "p002", "p013", "p017", "p021")
    pick = product_id in ("p001", "p005", "p020", "p023")
    badges = tuple(x for x, yes in (("BESTSELLER", best), ("NEW", new), ("FOUNDERS’ PICK", pick), ("LIMITED", product_id == "p023")) if yes)
    ingredient_note = ", ".join(ingredients[:-1]).lower() + " and " + ingredients[-1].lower() if len(ingredients) > 1 else ingredients[0].lower()
    form_value = {"Powder": "Herbal Powders", "Oil": "Botanical Oils", "Mist / Spray": "Hydrosols", "Dried Botanicals": "Dried Herbs & Flowers"}[texture]
    return Product(
        id=product_id, slug=name.lower().replace(" & ", "-").replace(" ", "-"),
        brand="SISTERSKESA", name=name, category=category, subcategory=sub, description=desc,
        long_description=f"{desc} This botanical composition brings together {ingredient_note}. {use}",
        price=price, sale_price=round(price * .9, 2) if product_id in ("p006", "p016", "p025") else None,
        sizes=sizes, rating=round(4.6+(i % 4)*.1, 1), review_count=173 if i == 0 else 34+i*7,
        badges=badges, ingredients=ingredients,
        benefits=tuple({"Face Ritual": "Make a little space for your daily face-care ritual.", "Fresh Start": "Begin the day with a botanical cleansing ritual.", "Hair Ritual": "Bring familiar herbs into your hair-care routine.", "Scalp Ritual": "Take time for an unhurried head massage.", "Body Ritual": "Make everyday body care a moment for yourself.", "Bathing Ritual": "Bring a botanical touch to your bathing bowl.", "Slow Evenings": "Make space for an unhurried evening ritual."}[g] for g in goals),
        how_to_use=use, texture=texture, fragrance_profile=fragrance,
        values=("Botanical Ingredients", form_value),
        care_goals=goals, availability="Out of Stock" if product_id == "p014" else "Limited Edition" if product_id == "p023" else "In Stock",
        featured=featured, new_arrival=new, bestseller=best, sisters_pick=pick,
        image=image, gallery_images=(image, "editorial_texture", "ingredient_botanical"),
        tags=(sub, "herbal rituals", *(('new',) if new else ())),
    )


PRODUCTS = tuple(_build(row) for row in ROWS)
