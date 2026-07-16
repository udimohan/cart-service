"""Tests for catalog_00504."""

import pytest

from cartservice.generated.catalog_00504 import (
    Product_00504,
    bucket_by_tag_00504,
    is_valid_sku_00504,
    price_with_tax_00504,
)


def test_price_with_tax_00504():
    assert price_with_tax_00504(1000, 500) == 1050


def test_price_with_tax_negative_00504():
    with pytest.raises(ValueError):
        price_with_tax_00504(1000, -1)


def test_is_valid_sku_00504():
    assert is_valid_sku_00504("abc123")
    assert not is_valid_sku_00504("")


def test_bucket_by_tag_00504():
    p = Product_00504("s1", 100, ["a"])
    assert bucket_by_tag_00504([p]) == {"a": ["s1"]}
