"""Tests for catalog_00798."""

import pytest

from cartservice.generated.catalog_00798 import (
    Product_00798,
    bucket_by_tag_00798,
    is_valid_sku_00798,
    price_with_tax_00798,
)


def test_price_with_tax_00798():
    assert price_with_tax_00798(1000, 500) == 1050


def test_price_with_tax_negative_00798():
    with pytest.raises(ValueError):
        price_with_tax_00798(1000, -1)


def test_is_valid_sku_00798():
    assert is_valid_sku_00798("abc123")
    assert not is_valid_sku_00798("")


def test_bucket_by_tag_00798():
    p = Product_00798("s1", 100, ["a"])
    assert bucket_by_tag_00798([p]) == {"a": ["s1"]}
