"""Tests for catalog_00506."""

import pytest

from cartservice.generated.catalog_00506 import (
    Product_00506,
    bucket_by_tag_00506,
    is_valid_sku_00506,
    price_with_tax_00506,
)


def test_price_with_tax_00506():
    assert price_with_tax_00506(1000, 500) == 1050


def test_price_with_tax_negative_00506():
    with pytest.raises(ValueError):
        price_with_tax_00506(1000, -1)


def test_is_valid_sku_00506():
    assert is_valid_sku_00506("abc123")
    assert not is_valid_sku_00506("")


def test_bucket_by_tag_00506():
    p = Product_00506("s1", 100, ["a"])
    assert bucket_by_tag_00506([p]) == {"a": ["s1"]}
