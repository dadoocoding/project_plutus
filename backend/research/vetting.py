import logging
import json
from pathlib import Path
import random


def score_niche(niche: dict):
    """
    Heuristic scoring model.
    Replace individual signals later with real data.
    """

    # Simulated signals (will be real later)
    avg_price = random.uniform(15, 80)
    product_count = random.randint(20, 500)
    brand_saturation = random.uniform(0, 1)  # lower is better

    score = (
        (avg_price / 80) * 30 +
        (min(product_count, 300) / 300) * 40 +
        ((1 - brand_saturation) * 30)
    )

    return {
        **niche,
        "avg_price": round(avg_price, 2),
        "product_count": product_count,
        "brand_saturation": round(brand_saturation, 2),
        "score": round(score, 2),
    }


def run_vetting(config):
    logging.info("📊 Vetting niche candidates")

    raw_path = Path(config["paths"]["processed_data"]) / "niches_raw.json"
    output_path = Path(config["paths"]["processed_data"]) / "niches_scored.json"

    if not raw_path.exists():
        logging.warning("⚠️ No raw niches found — skipping vetting")
        return

    with open(raw_path, "r") as f:
        niches = json.load(f)

    scored = [score_niche(n) for n in niches]
    scored.sort(key=lambda x: x["score"], reverse=True)

    with open(output_path, "w") as f:
        json.dump(scored, f, indent=2)

    logging.info(f"🏆 Scored {len(scored)} niches")
