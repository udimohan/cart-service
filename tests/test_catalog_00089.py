"""Tests for catalog_00089."""

import pytest

from cartservice.generated.catalog_00089 import (
    Product_00089,
    bucket_by_tag_00089,
    is_valid_sku_00089,
    price_with_tax_00089,
)


def test_price_with_tax_00089():
    assert price_with_tax_00089(1000, 500) == 1050


def test_price_with_tax_negative_00089():
    with pytest.raises(ValueError):
        price_with_tax_00089(1000, -1)


def test_is_valid_sku_00089():
    assert is_valid_sku_00089("abc123")
    assert not is_valid_sku_00089("")


def test_bucket_by_tag_00089():
    p = Product_00089("s1", 100, ["a"])
    assert bucket_by_tag_00089([p]) == {"a": ["s1"]}
