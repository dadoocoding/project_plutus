import logging
import json
from pathlib import Path


def run_normalization(config):
    logging.info("🧼 Normalizing products (stub)")

    raw_path = Path(config["paths"]["raw_data"]) / "products_raw.json"
    processed_path = Path(config["paths"]["processed_data"]) / "products.json"

    if not raw_path.exists():
        logging.warning("⚠️ No raw products found — skipping normalization")
        return

    with open(raw_path, "r") as f:
        products = json.load(f)

    # In future: dedupe, enrich, score
    normalized = products

    with open(processed_path, "w") as f:
        json.dump(normalized, f, indent=2)

    logging.info(f"📁 Saved normalized products to {processed_path}")
