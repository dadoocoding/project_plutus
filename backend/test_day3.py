from services.normalization import normalize_amazon_product
from backend.generate_outputs import write_products

mock_data = [
    {
        "asin": "B000123",
        "title": "Self-Stirring Coffee Mug",
        "price": 24.99,
        "rating": 4.6,
        "review_count": 1832,
        "image_url": "https://example.com/mug.jpg",
        "product_url": "https://amazon.com/dp/B000123",
        "category": "kitchen",
        "features": ["Self-stirring", "Battery powered"],
        "tags": ["gift", "coffee"]
    }
]

products = [normalize_amazon_product(p, niche="gadgets") for p in mock_data]
write_products(products)

print("Day 3 pipeline complete.")
