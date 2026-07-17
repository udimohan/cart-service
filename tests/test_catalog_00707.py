"""Tests for catalog_00707."""

import pytest

from cartservice.generated.catalog_00707 import (
    Product_00707,
    bucket_by_tag_00707,
    is_valid_sku_00707,
    price_with_tax_00707,
)


def test_price_with_tax_00707():
    assert price_with_tax_00707(1000, 500) == 1050


def test_price_with_tax_negative_00707():
    with pytest.raises(ValueError):
        price_with_tax_00707(1000, -1)


def test_is_valid_sku_00707():
    assert is_valid_sku_00707("abc123")
    assert not is_valid_sku_00707("")


def test_bucket_by_tag_00707():
    p = Product_00707("s1", 100, ["a"])
    assert bucket_by_tag_00707([p]) == {"a": ["s1"]}
