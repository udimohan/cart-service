"""Tests for catalog_00110."""

import pytest

from cartservice.generated.catalog_00110 import (
    Product_00110,
    bucket_by_tag_00110,
    is_valid_sku_00110,
    price_with_tax_00110,
)


def test_price_with_tax_00110():
    assert price_with_tax_00110(1000, 500) == 1050


def test_price_with_tax_negative_00110():
    with pytest.raises(ValueError):
        price_with_tax_00110(1000, -1)


def test_is_valid_sku_00110():
    assert is_valid_sku_00110("abc123")
    assert not is_valid_sku_00110("")


def test_bucket_by_tag_00110():
    p = Product_00110("s1", 100, ["a"])
    assert bucket_by_tag_00110([p]) == {"a": ["s1"]}
