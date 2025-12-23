import json
from pathlib import Path
from typing import List
from models.product import Product
from services.slugify import slugify


OUTPUT_DIR = Path("../outputs/data")
CATEGORY_DIR = OUTPUT_DIR / "categories"


def enrich_product(product):
    data = product.model_dump()
    data["slug"] = slugify(product.title)
    data["category_slug"] = slugify(product.category or "general")
    return data


def write_products(products: List[Product]):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    CATEGORY_DIR.mkdir(parents=True, exist_ok=True)

    # All products
    with open(OUTPUT_DIR / "products.json", "w") as f:
        json.dump([enrich_product(p) for p in products], f, indent=2, default=str)

    # Featured (top 10)
    featured = sorted(products, key=lambda p: p.score, reverse=True)[:10]
    with open(OUTPUT_DIR / "featured.json", "w") as f:
        json.dump([enrich_product(p) for p in featured], f, indent=2, default=str)

    # Categories
    categories = {}
    for p in products:
        if not p.category:
            continue
        categories.setdefault(p.category, []).append(p)

    for category, items in categories.items():
        path = CATEGORY_DIR / f"{category}.json"
        with open(path, "w") as f:
            json.dump(
                [enrich_product(p) for p in sorted(items, key=lambda p: p.score, reverse=True)],
                f,
                indent=2,
                default=str
            )
