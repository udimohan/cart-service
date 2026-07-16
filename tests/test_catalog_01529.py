"""Tests for catalog_01529."""

import pytest

from cartservice.generated.catalog_01529 import (
    Product_01529,
    bucket_by_tag_01529,
    is_valid_sku_01529,
    price_with_tax_01529,
)


def test_price_with_tax_01529():
    assert price_with_tax_01529(1000, 500) == 1050


def test_price_with_tax_negative_01529():
    with pytest.raises(ValueError):
        price_with_tax_01529(1000, -1)


def test_is_valid_sku_01529():
    assert is_valid_sku_01529("abc123")
    assert not is_valid_sku_01529("")


def test_bucket_by_tag_01529():
    p = Product_01529("s1", 100, ["a"])
    assert bucket_by_tag_01529([p]) == {"a": ["s1"]}
