import os
from urllib.parse import urlencode, urlparse, parse_qs, urlunparse
from dotenv import load_dotenv

load_dotenv()


AMAZON_TAG = os.getenv("AMAZON_AFFILIATE_TAG", "yourtag-20")


def build_amazon_affiliate_url(product_url: str) -> str:
    product_url = str(product_url)
    parsed = urlparse(product_url)
    query = parse_qs(parsed.query)

    query["tag"] = AMAZON_TAG

    new_query = urlencode(query, doseq=True)
    return urlunparse(parsed._replace(query=new_query))


def build_affiliate_url(product_url: str, source: str) -> str:
    source = source.lower()

    if source == "amazon":
        return build_amazon_affiliate_url(product_url)

    # Future sources
    # elif source == "walmart":
    # elif source == "etsy":
    # elif source == "ebay":

    return product_url
