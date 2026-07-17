"""Tests for catalog_00516."""

import pytest

from cartservice.generated.catalog_00516 import (
    Product_00516,
    bucket_by_tag_00516,
    is_valid_sku_00516,
    price_with_tax_00516,
)


def test_price_with_tax_00516():
    assert price_with_tax_00516(1000, 500) == 1050


def test_price_with_tax_negative_00516():
    with pytest.raises(ValueError):
        price_with_tax_00516(1000, -1)


def test_is_valid_sku_00516():
    assert is_valid_sku_00516("abc123")
    assert not is_valid_sku_00516("")


def test_bucket_by_tag_00516():
    p = Product_00516("s1", 100, ["a"])
    assert bucket_by_tag_00516([p]) == {"a": ["s1"]}
