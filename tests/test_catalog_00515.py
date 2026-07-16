"""Tests for catalog_00515."""

import pytest

from cartservice.generated.catalog_00515 import (
    Product_00515,
    bucket_by_tag_00515,
    is_valid_sku_00515,
    price_with_tax_00515,
)


def test_price_with_tax_00515():
    assert price_with_tax_00515(1000, 500) == 1050


def test_price_with_tax_negative_00515():
    with pytest.raises(ValueError):
        price_with_tax_00515(1000, -1)


def test_is_valid_sku_00515():
    assert is_valid_sku_00515("abc123")
    assert not is_valid_sku_00515("")


def test_bucket_by_tag_00515():
    p = Product_00515("s1", 100, ["a"])
    assert bucket_by_tag_00515([p]) == {"a": ["s1"]}
