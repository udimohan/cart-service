"""Tests for catalog_00256."""

import pytest

from cartservice.generated.catalog_00256 import (
    Product_00256,
    bucket_by_tag_00256,
    is_valid_sku_00256,
    price_with_tax_00256,
)


def test_price_with_tax_00256():
    assert price_with_tax_00256(1000, 500) == 1050


def test_price_with_tax_negative_00256():
    with pytest.raises(ValueError):
        price_with_tax_00256(1000, -1)


def test_is_valid_sku_00256():
    assert is_valid_sku_00256("abc123")
    assert not is_valid_sku_00256("")


def test_bucket_by_tag_00256():
    p = Product_00256("s1", 100, ["a"])
    assert bucket_by_tag_00256([p]) == {"a": ["s1"]}
