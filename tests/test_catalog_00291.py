"""Tests for catalog_00291."""

import pytest

from cartservice.generated.catalog_00291 import (
    Product_00291,
    bucket_by_tag_00291,
    is_valid_sku_00291,
    price_with_tax_00291,
)


def test_price_with_tax_00291():
    assert price_with_tax_00291(1000, 500) == 1050


def test_price_with_tax_negative_00291():
    with pytest.raises(ValueError):
        price_with_tax_00291(1000, -1)


def test_is_valid_sku_00291():
    assert is_valid_sku_00291("abc123")
    assert not is_valid_sku_00291("")


def test_bucket_by_tag_00291():
    p = Product_00291("s1", 100, ["a"])
    assert bucket_by_tag_00291([p]) == {"a": ["s1"]}
