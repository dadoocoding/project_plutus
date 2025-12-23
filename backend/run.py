import logging
import yaml
from pathlib import Path


from research.niche_finder import run_niche_research
from research.vetting import run_vetting

from ingestion.amazon import run_product_ingestion
from normalize.products import run_normalization
from generate.pages import run_page_generation


def load_config():
    with open("config/settings.yaml", "r") as f:
        return yaml.safe_load(f)


def setup_logging(level="INFO"):
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


def ensure_directories(paths):
    for path in paths.values():
        Path(path).mkdir(parents=True, exist_ok=True)


def main():
    config = load_config()
    setup_logging(config["project"]["log_level"])

    logging.info("🚀 Starting Project Plutus pipeline")

    ensure_directories(config["paths"])

    if config["pipeline"]["research"]:
        run_niche_research(config)
        run_vetting(config)

    if config["pipeline"]["ingestion"]:
        run_product_ingestion(config)

    if config["pipeline"]["normalization"]:
        run_normalization(config)

    if config["pipeline"]["generation"]:
        run_page_generation(config)

    logging.info("✅ Project Plutus pipeline complete")


if __name__ == "__main__":
    main()
