"""Tests for catalog_01253."""

import pytest

from cartservice.generated.catalog_01253 import (
    Product_01253,
    bucket_by_tag_01253,
    is_valid_sku_01253,
    price_with_tax_01253,
)


def test_price_with_tax_01253():
    assert price_with_tax_01253(1000, 500) == 1050


def test_price_with_tax_negative_01253():
    with pytest.raises(ValueError):
        price_with_tax_01253(1000, -1)


def test_is_valid_sku_01253():
    assert is_valid_sku_01253("abc123")
    assert not is_valid_sku_01253("")


def test_bucket_by_tag_01253():
    p = Product_01253("s1", 100, ["a"])
    assert bucket_by_tag_01253([p]) == {"a": ["s1"]}
