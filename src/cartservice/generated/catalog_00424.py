"""Supporting catalog module 00424.

Provides catalog lookup and validation helpers used by the cart service.
Fully type-annotated and unit-tested.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Product_00424:
    sku: str
    price_cents: int
    tags: list[str] = field(default_factory=list)


def price_with_tax_00424(price_cents: int, tax_bps: int) -> int:
    """Apply tax in basis points to a price."""
    if tax_bps < 0:
        raise ValueError("tax_bps must be non-negative")
    return price_cents + (price_cents * tax_bps) // 10000


def is_valid_sku_00424(sku: str) -> bool:
    """Validate a SKU is alphanumeric and non-empty."""
    return bool(sku) and sku.isalnum()


def bucket_by_tag_00424(products: list[Product_00424]) -> dict[str, list[str]]:
    """Group product SKUs by tag."""
    out: dict[str, list[str]] = {}
    for p in products:
        for t in p.tags:
            out.setdefault(t, []).append(p.sku)
    return out
