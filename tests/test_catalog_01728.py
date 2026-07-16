"""Tests for catalog_01728."""

import pytest

from cartservice.generated.catalog_01728 import (
    Product_01728,
    bucket_by_tag_01728,
    is_valid_sku_01728,
    price_with_tax_01728,
)


def test_price_with_tax_01728():
    assert price_with_tax_01728(1000, 500) == 1050


def test_price_with_tax_negative_01728():
    with pytest.raises(ValueError):
        price_with_tax_01728(1000, -1)


def test_is_valid_sku_01728():
    assert is_valid_sku_01728("abc123")
    assert not is_valid_sku_01728("")


def test_bucket_by_tag_01728():
    p = Product_01728("s1", 100, ["a"])
    assert bucket_by_tag_01728([p]) == {"a": ["s1"]}
