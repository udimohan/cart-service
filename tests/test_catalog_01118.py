"""Tests for catalog_01118."""

import pytest

from cartservice.generated.catalog_01118 import (
    Product_01118,
    bucket_by_tag_01118,
    is_valid_sku_01118,
    price_with_tax_01118,
)


def test_price_with_tax_01118():
    assert price_with_tax_01118(1000, 500) == 1050


def test_price_with_tax_negative_01118():
    with pytest.raises(ValueError):
        price_with_tax_01118(1000, -1)


def test_is_valid_sku_01118():
    assert is_valid_sku_01118("abc123")
    assert not is_valid_sku_01118("")


def test_bucket_by_tag_01118():
    p = Product_01118("s1", 100, ["a"])
    assert bucket_by_tag_01118([p]) == {"a": ["s1"]}
