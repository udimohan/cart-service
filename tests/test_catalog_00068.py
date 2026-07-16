"""Tests for catalog_00068."""

import pytest

from cartservice.generated.catalog_00068 import (
    Product_00068,
    bucket_by_tag_00068,
    is_valid_sku_00068,
    price_with_tax_00068,
)


def test_price_with_tax_00068():
    assert price_with_tax_00068(1000, 500) == 1050


def test_price_with_tax_negative_00068():
    with pytest.raises(ValueError):
        price_with_tax_00068(1000, -1)


def test_is_valid_sku_00068():
    assert is_valid_sku_00068("abc123")
    assert not is_valid_sku_00068("")


def test_bucket_by_tag_00068():
    p = Product_00068("s1", 100, ["a"])
    assert bucket_by_tag_00068([p]) == {"a": ["s1"]}
