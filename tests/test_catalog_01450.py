"""Tests for catalog_01450."""

import pytest

from cartservice.generated.catalog_01450 import (
    Product_01450,
    bucket_by_tag_01450,
    is_valid_sku_01450,
    price_with_tax_01450,
)


def test_price_with_tax_01450():
    assert price_with_tax_01450(1000, 500) == 1050


def test_price_with_tax_negative_01450():
    with pytest.raises(ValueError):
        price_with_tax_01450(1000, -1)


def test_is_valid_sku_01450():
    assert is_valid_sku_01450("abc123")
    assert not is_valid_sku_01450("")


def test_bucket_by_tag_01450():
    p = Product_01450("s1", 100, ["a"])
    assert bucket_by_tag_01450([p]) == {"a": ["s1"]}
