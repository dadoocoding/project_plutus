from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
from datetime import datetime
from uuid import uuid4


class Product(BaseModel):
    product_id: str = Field(default_factory=lambda: str(uuid4()))
    source: str
    source_id: str

    title: str
    description: Optional[str] = None

    category: Optional[str] = None
    niche: Optional[str] = None

    price: float
    currency: str = "USD"

    rating: Optional[float] = None
    review_count: Optional[int] = None

    image_url: Optional[HttpUrl] = None
    product_url: HttpUrl
    affiliate_url: Optional[HttpUrl] = None

    features: List[str] = []
    tags: List[str] = []

    score: float = 0.0
    last_updated: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        validate_assignment = True
