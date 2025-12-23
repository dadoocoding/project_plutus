import logging
import json
from pathlib import Path

# These are intentionally broad — the engine refines later
SEED_CATEGORIES = [
    "gadgets",
    "home decor",
    "office accessories",
    "kitchen tools",
    "outdoor gear",
    "fitness accessories",
    "tech accessories",
    "novelty gifts",
]


def expand_category(category: str):
    """
    Expand a broad category into storefront-friendly niche phrases.
    This is deterministic, not LLM-based (cheap & repeatable).
    """
    modifiers = [
        "for men",
        "for women",
        "for engineers",
        "for gamers",
        "under $50",
        "under $25",
        "unique",
        "cool",
        "weird",
    ]

    return [f"{category} {m}" for m in modifiers]


def run_niche_research(config):
    logging.info("🔍 Running niche discovery")

    candidates = []

    for category in SEED_CATEGORIES:
        expanded = expand_category(category)
        for phrase in expanded:
            candidates.append({
                "niche": phrase,
                "base_category": category,
            })

    output_path = Path(config["paths"]["processed_data"]) / "niches_raw.json"
    with open(output_path, "w") as f:
        json.dump(candidates, f, indent=2)

    logging.info(f"📁 Generated {len(candidates)} raw niche candidates")
