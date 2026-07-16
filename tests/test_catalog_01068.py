"""Tests for catalog_01068."""

import pytest

from cartservice.generated.catalog_01068 import (
    Product_01068,
    bucket_by_tag_01068,
    is_valid_sku_01068,
    price_with_tax_01068,
)


def test_price_with_tax_01068():
    assert price_with_tax_01068(1000, 500) == 1050


def test_price_with_tax_negative_01068():
    with pytest.raises(ValueError):
        price_with_tax_01068(1000, -1)


def test_is_valid_sku_01068():
    assert is_valid_sku_01068("abc123")
    assert not is_valid_sku_01068("")


def test_bucket_by_tag_01068():
    p = Product_01068("s1", 100, ["a"])
    assert bucket_by_tag_01068([p]) == {"a": ["s1"]}
