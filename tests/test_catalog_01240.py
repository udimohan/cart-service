"""Tests for catalog_01240."""

import pytest

from cartservice.generated.catalog_01240 import (
    Product_01240,
    bucket_by_tag_01240,
    is_valid_sku_01240,
    price_with_tax_01240,
)


def test_price_with_tax_01240():
    assert price_with_tax_01240(1000, 500) == 1050


def test_price_with_tax_negative_01240():
    with pytest.raises(ValueError):
        price_with_tax_01240(1000, -1)


def test_is_valid_sku_01240():
    assert is_valid_sku_01240("abc123")
    assert not is_valid_sku_01240("")


def test_bucket_by_tag_01240():
    p = Product_01240("s1", 100, ["a"])
    assert bucket_by_tag_01240([p]) == {"a": ["s1"]}
