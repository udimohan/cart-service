"""Tests for catalog_01566."""

import pytest

from cartservice.generated.catalog_01566 import (
    Product_01566,
    bucket_by_tag_01566,
    is_valid_sku_01566,
    price_with_tax_01566,
)


def test_price_with_tax_01566():
    assert price_with_tax_01566(1000, 500) == 1050


def test_price_with_tax_negative_01566():
    with pytest.raises(ValueError):
        price_with_tax_01566(1000, -1)


def test_is_valid_sku_01566():
    assert is_valid_sku_01566("abc123")
    assert not is_valid_sku_01566("")


def test_bucket_by_tag_01566():
    p = Product_01566("s1", 100, ["a"])
    assert bucket_by_tag_01566([p]) == {"a": ["s1"]}
