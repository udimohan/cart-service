"""Tests for catalog_00317."""

import pytest

from cartservice.generated.catalog_00317 import (
    Product_00317,
    bucket_by_tag_00317,
    is_valid_sku_00317,
    price_with_tax_00317,
)


def test_price_with_tax_00317():
    assert price_with_tax_00317(1000, 500) == 1050


def test_price_with_tax_negative_00317():
    with pytest.raises(ValueError):
        price_with_tax_00317(1000, -1)


def test_is_valid_sku_00317():
    assert is_valid_sku_00317("abc123")
    assert not is_valid_sku_00317("")


def test_bucket_by_tag_00317():
    p = Product_00317("s1", 100, ["a"])
    assert bucket_by_tag_00317([p]) == {"a": ["s1"]}
