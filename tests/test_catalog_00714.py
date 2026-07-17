"""Tests for catalog_00714."""

import pytest

from cartservice.generated.catalog_00714 import (
    Product_00714,
    bucket_by_tag_00714,
    is_valid_sku_00714,
    price_with_tax_00714,
)


def test_price_with_tax_00714():
    assert price_with_tax_00714(1000, 500) == 1050


def test_price_with_tax_negative_00714():
    with pytest.raises(ValueError):
        price_with_tax_00714(1000, -1)


def test_is_valid_sku_00714():
    assert is_valid_sku_00714("abc123")
    assert not is_valid_sku_00714("")


def test_bucket_by_tag_00714():
    p = Product_00714("s1", 100, ["a"])
    assert bucket_by_tag_00714([p]) == {"a": ["s1"]}
