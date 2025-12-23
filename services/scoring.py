import math


def compute_product_score(
    rating: float | None,
    review_count: int | None,
    price: float
) -> float:
    rating = rating or 0
    review_count = review_count or 0

    social_proof = math.log(review_count + 1)
    price_penalty = price / 100  # simple dampener

    score = (rating * 2) + social_proof - price_penalty
    return round(score, 4)
