"""Tests for catalog_00630."""

import pytest

from cartservice.generated.catalog_00630 import (
    Product_00630,
    bucket_by_tag_00630,
    is_valid_sku_00630,
    price_with_tax_00630,
)


def test_price_with_tax_00630():
    assert price_with_tax_00630(1000, 500) == 1050


def test_price_with_tax_negative_00630():
    with pytest.raises(ValueError):
        price_with_tax_00630(1000, -1)


def test_is_valid_sku_00630():
    assert is_valid_sku_00630("abc123")
    assert not is_valid_sku_00630("")


def test_bucket_by_tag_00630():
    p = Product_00630("s1", 100, ["a"])
    assert bucket_by_tag_00630([p]) == {"a": ["s1"]}
