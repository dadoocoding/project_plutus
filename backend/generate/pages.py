import logging
from pathlib import Path


def run_page_generation(config):
    logging.info("🧱 Generating site pages (stub)")

    output_dir = Path(config["paths"]["site_output"])
    index_file = output_dir / "index.html"

    html = """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Project Plutus</title>
      </head>
      <body>
        <h1>Project Plutus</h1>
        <p>Automated affiliate storefront coming online.</p>
      </body>
    </html>
    """

    index_file.write_text(html.strip(), encoding="utf-8")

    logging.info(f"🌐 Generated {index_file}")
