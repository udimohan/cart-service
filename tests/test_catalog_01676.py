"""Tests for catalog_01676."""

import pytest

from cartservice.generated.catalog_01676 import (
    Product_01676,
    bucket_by_tag_01676,
    is_valid_sku_01676,
    price_with_tax_01676,
)


def test_price_with_tax_01676():
    assert price_with_tax_01676(1000, 500) == 1050


def test_price_with_tax_negative_01676():
    with pytest.raises(ValueError):
        price_with_tax_01676(1000, -1)


def test_is_valid_sku_01676():
    assert is_valid_sku_01676("abc123")
    assert not is_valid_sku_01676("")


def test_bucket_by_tag_01676():
    p = Product_01676("s1", 100, ["a"])
    assert bucket_by_tag_01676([p]) == {"a": ["s1"]}
