"""Tests for catalog_00949."""

import pytest

from cartservice.generated.catalog_00949 import (
    Product_00949,
    bucket_by_tag_00949,
    is_valid_sku_00949,
    price_with_tax_00949,
)


def test_price_with_tax_00949():
    assert price_with_tax_00949(1000, 500) == 1050


def test_price_with_tax_negative_00949():
    with pytest.raises(ValueError):
        price_with_tax_00949(1000, -1)


def test_is_valid_sku_00949():
    assert is_valid_sku_00949("abc123")
    assert not is_valid_sku_00949("")


def test_bucket_by_tag_00949():
    p = Product_00949("s1", 100, ["a"])
    assert bucket_by_tag_00949([p]) == {"a": ["s1"]}
