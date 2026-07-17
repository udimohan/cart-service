"""Tests for catalog_00255."""

import pytest

from cartservice.generated.catalog_00255 import (
    Product_00255,
    bucket_by_tag_00255,
    is_valid_sku_00255,
    price_with_tax_00255,
)


def test_price_with_tax_00255():
    assert price_with_tax_00255(1000, 500) == 1050


def test_price_with_tax_negative_00255():
    with pytest.raises(ValueError):
        price_with_tax_00255(1000, -1)


def test_is_valid_sku_00255():
    assert is_valid_sku_00255("abc123")
    assert not is_valid_sku_00255("")


def test_bucket_by_tag_00255():
    p = Product_00255("s1", 100, ["a"])
    assert bucket_by_tag_00255([p]) == {"a": ["s1"]}
