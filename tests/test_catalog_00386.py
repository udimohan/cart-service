"""Tests for catalog_00386."""

import pytest

from cartservice.generated.catalog_00386 import (
    Product_00386,
    bucket_by_tag_00386,
    is_valid_sku_00386,
    price_with_tax_00386,
)


def test_price_with_tax_00386():
    assert price_with_tax_00386(1000, 500) == 1050


def test_price_with_tax_negative_00386():
    with pytest.raises(ValueError):
        price_with_tax_00386(1000, -1)


def test_is_valid_sku_00386():
    assert is_valid_sku_00386("abc123")
    assert not is_valid_sku_00386("")


def test_bucket_by_tag_00386():
    p = Product_00386("s1", 100, ["a"])
    assert bucket_by_tag_00386([p]) == {"a": ["s1"]}
