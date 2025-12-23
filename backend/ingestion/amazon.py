import logging
import json
from pathlib import Path


def run_product_ingestion(config):
    logging.info("🛒 Running product ingestion (stub)")

    products = [
        {
            "id": "TEST-ASIN-1",
            "title": "Ridiculous But Awesome Gadget",
            "price": 29.99,
            "rating": 4.7,
            "category": "gadgets",
            "image": "https://example.com/image.jpg",
        }
    ]

    output_path = Path(config["paths"]["raw_data"]) / "products_raw.json"
    with open(output_path, "w") as f:
        json.dump(products, f, indent=2)

    logging.info(f"📁 Saved raw products to {output_path}")
