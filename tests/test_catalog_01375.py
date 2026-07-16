"""Tests for catalog_01375."""

import pytest

from cartservice.generated.catalog_01375 import (
    Product_01375,
    bucket_by_tag_01375,
    is_valid_sku_01375,
    price_with_tax_01375,
)


def test_price_with_tax_01375():
    assert price_with_tax_01375(1000, 500) == 1050


def test_price_with_tax_negative_01375():
    with pytest.raises(ValueError):
        price_with_tax_01375(1000, -1)


def test_is_valid_sku_01375():
    assert is_valid_sku_01375("abc123")
    assert not is_valid_sku_01375("")


def test_bucket_by_tag_01375():
    p = Product_01375("s1", 100, ["a"])
    assert bucket_by_tag_01375([p]) == {"a": ["s1"]}
