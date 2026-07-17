"""Tests for catalog_00788."""

import pytest

from cartservice.generated.catalog_00788 import (
    Product_00788,
    bucket_by_tag_00788,
    is_valid_sku_00788,
    price_with_tax_00788,
)


def test_price_with_tax_00788():
    assert price_with_tax_00788(1000, 500) == 1050


def test_price_with_tax_negative_00788():
    with pytest.raises(ValueError):
        price_with_tax_00788(1000, -1)


def test_is_valid_sku_00788():
    assert is_valid_sku_00788("abc123")
    assert not is_valid_sku_00788("")


def test_bucket_by_tag_00788():
    p = Product_00788("s1", 100, ["a"])
    assert bucket_by_tag_00788([p]) == {"a": ["s1"]}
