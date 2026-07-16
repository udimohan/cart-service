"""Tests for catalog_01335."""

import pytest

from cartservice.generated.catalog_01335 import (
    Product_01335,
    bucket_by_tag_01335,
    is_valid_sku_01335,
    price_with_tax_01335,
)


def test_price_with_tax_01335():
    assert price_with_tax_01335(1000, 500) == 1050


def test_price_with_tax_negative_01335():
    with pytest.raises(ValueError):
        price_with_tax_01335(1000, -1)


def test_is_valid_sku_01335():
    assert is_valid_sku_01335("abc123")
    assert not is_valid_sku_01335("")


def test_bucket_by_tag_01335():
    p = Product_01335("s1", 100, ["a"])
    assert bucket_by_tag_01335([p]) == {"a": ["s1"]}
