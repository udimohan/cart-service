"""Tests for catalog_01707."""

import pytest

from cartservice.generated.catalog_01707 import (
    Product_01707,
    bucket_by_tag_01707,
    is_valid_sku_01707,
    price_with_tax_01707,
)


def test_price_with_tax_01707():
    assert price_with_tax_01707(1000, 500) == 1050


def test_price_with_tax_negative_01707():
    with pytest.raises(ValueError):
        price_with_tax_01707(1000, -1)


def test_is_valid_sku_01707():
    assert is_valid_sku_01707("abc123")
    assert not is_valid_sku_01707("")


def test_bucket_by_tag_01707():
    p = Product_01707("s1", 100, ["a"])
    assert bucket_by_tag_01707([p]) == {"a": ["s1"]}
