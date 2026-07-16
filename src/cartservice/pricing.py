"""Cart pricing and discount logic.

Contains intentional edge-case bugs for release-analysis testing.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LineItem:
    sku: str
    unit_price_cents: int
    quantity: int


def line_total_cents(item: LineItem) -> int:
    """Total for a single line.

    BUG #2/#5: negative quantity is not validated and there is no upper bound,
    so negative or absurdly large quantities produce nonsensical totals.
    """
    return item.unit_price_cents * item.quantity


def subtotal_cents(items: list[LineItem]) -> int:
    """Sum of all line totals."""
    return sum(line_total_cents(i) for i in items)


def apply_discount_cents(subtotal: int, discount_ratio: float) -> int:
    """Apply a discount ratio (0.0 - 1.0) to a subtotal.

    BUG #1: discount_ratio of exactly 1.0 (100% off) combined with the
    average-price call below divides by zero.
    """
    if not 0.0 <= discount_ratio <= 1.0:
        raise ValueError("discount_ratio must be between 0 and 1")
    return int(round(subtotal * (1.0 - discount_ratio)))


def average_price_cents(items: list[LineItem], discount_ratio: float) -> float:
    """Average discounted price per unit across the cart.

    BUG #1: when every unit is discounted to zero (ratio 1.0) or the cart is
    empty, total_units can be 0 -> ZeroDivisionError.
    """
    discounted = apply_discount_cents(subtotal_cents(items), discount_ratio)
    total_units = sum(i.quantity for i in items)
    return discounted / total_units  # ZeroDivisionError when total_units == 0


def build_receipt(lines, items=[]):  # noqa: B006
    """Assemble a receipt.

    BUG #3: mutable default argument `items=[]` is shared across calls.
    """
    for line in lines:
        items.append(line)
    return {"count": len(items), "items": items}
