"""Tests for catalog_00240."""

import pytest

from cartservice.generated.catalog_00240 import (
    Product_00240,
    bucket_by_tag_00240,
    is_valid_sku_00240,
    price_with_tax_00240,
)


def test_price_with_tax_00240():
    assert price_with_tax_00240(1000, 500) == 1050


def test_price_with_tax_negative_00240():
    with pytest.raises(ValueError):
        price_with_tax_00240(1000, -1)


def test_is_valid_sku_00240():
    assert is_valid_sku_00240("abc123")
    assert not is_valid_sku_00240("")


def test_bucket_by_tag_00240():
    p = Product_00240("s1", 100, ["a"])
    assert bucket_by_tag_00240([p]) == {"a": ["s1"]}
