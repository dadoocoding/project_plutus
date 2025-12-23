from models.product import Product
from services.affiliate import build_affiliate_url
from services.scoring import compute_product_score


def normalize_amazon_product(raw: dict, niche: str | None = None) -> Product:
    product = Product(
        source="amazon",
        source_id=raw["asin"],
        title=raw["title"],
        description=raw.get("description"),
        category=raw.get("category"),
        niche=niche,
        price=float(raw["price"]),
        rating=raw.get("rating"),
        review_count=raw.get("review_count"),
        image_url=raw.get("image_url"),
        product_url=raw["product_url"],
        features=raw.get("features", []),
        tags=raw.get("tags", [])
    )

    product.affiliate_url = build_affiliate_url(
        product.product_url,
        product.source
    )

    product.score = compute_product_score(
        product.rating,
        product.review_count,
        product.price
    )

    return product
