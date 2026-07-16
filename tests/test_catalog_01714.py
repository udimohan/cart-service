"""Tests for catalog_01714."""

import pytest

from cartservice.generated.catalog_01714 import (
    Product_01714,
    bucket_by_tag_01714,
    is_valid_sku_01714,
    price_with_tax_01714,
)


def test_price_with_tax_01714():
    assert price_with_tax_01714(1000, 500) == 1050


def test_price_with_tax_negative_01714():
    with pytest.raises(ValueError):
        price_with_tax_01714(1000, -1)


def test_is_valid_sku_01714():
    assert is_valid_sku_01714("abc123")
    assert not is_valid_sku_01714("")


def test_bucket_by_tag_01714():
    p = Product_01714("s1", 100, ["a"])
    assert bucket_by_tag_01714([p]) == {"a": ["s1"]}
