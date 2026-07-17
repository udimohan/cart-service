"""Tests for catalog_00939."""

import pytest

from cartservice.generated.catalog_00939 import (
    Product_00939,
    bucket_by_tag_00939,
    is_valid_sku_00939,
    price_with_tax_00939,
)


def test_price_with_tax_00939():
    assert price_with_tax_00939(1000, 500) == 1050


def test_price_with_tax_negative_00939():
    with pytest.raises(ValueError):
        price_with_tax_00939(1000, -1)


def test_is_valid_sku_00939():
    assert is_valid_sku_00939("abc123")
    assert not is_valid_sku_00939("")


def test_bucket_by_tag_00939():
    p = Product_00939("s1", 100, ["a"])
    assert bucket_by_tag_00939([p]) == {"a": ["s1"]}
