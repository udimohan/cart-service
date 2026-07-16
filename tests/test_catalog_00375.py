"""Tests for catalog_00375."""

import pytest

from cartservice.generated.catalog_00375 import (
    Product_00375,
    bucket_by_tag_00375,
    is_valid_sku_00375,
    price_with_tax_00375,
)


def test_price_with_tax_00375():
    assert price_with_tax_00375(1000, 500) == 1050


def test_price_with_tax_negative_00375():
    with pytest.raises(ValueError):
        price_with_tax_00375(1000, -1)


def test_is_valid_sku_00375():
    assert is_valid_sku_00375("abc123")
    assert not is_valid_sku_00375("")


def test_bucket_by_tag_00375():
    p = Product_00375("s1", 100, ["a"])
    assert bucket_by_tag_00375([p]) == {"a": ["s1"]}
