"""Tests for catalog_00803."""

import pytest

from cartservice.generated.catalog_00803 import (
    Product_00803,
    bucket_by_tag_00803,
    is_valid_sku_00803,
    price_with_tax_00803,
)


def test_price_with_tax_00803():
    assert price_with_tax_00803(1000, 500) == 1050


def test_price_with_tax_negative_00803():
    with pytest.raises(ValueError):
        price_with_tax_00803(1000, -1)


def test_is_valid_sku_00803():
    assert is_valid_sku_00803("abc123")
    assert not is_valid_sku_00803("")


def test_bucket_by_tag_00803():
    p = Product_00803("s1", 100, ["a"])
    assert bucket_by_tag_00803([p]) == {"a": ["s1"]}
