"""Tests for catalog_01516."""

import pytest

from cartservice.generated.catalog_01516 import (
    Product_01516,
    bucket_by_tag_01516,
    is_valid_sku_01516,
    price_with_tax_01516,
)


def test_price_with_tax_01516():
    assert price_with_tax_01516(1000, 500) == 1050


def test_price_with_tax_negative_01516():
    with pytest.raises(ValueError):
        price_with_tax_01516(1000, -1)


def test_is_valid_sku_01516():
    assert is_valid_sku_01516("abc123")
    assert not is_valid_sku_01516("")


def test_bucket_by_tag_01516():
    p = Product_01516("s1", 100, ["a"])
    assert bucket_by_tag_01516([p]) == {"a": ["s1"]}
