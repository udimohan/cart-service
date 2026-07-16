"""Tests for catalog_00451."""

import pytest

from cartservice.generated.catalog_00451 import (
    Product_00451,
    bucket_by_tag_00451,
    is_valid_sku_00451,
    price_with_tax_00451,
)


def test_price_with_tax_00451():
    assert price_with_tax_00451(1000, 500) == 1050


def test_price_with_tax_negative_00451():
    with pytest.raises(ValueError):
        price_with_tax_00451(1000, -1)


def test_is_valid_sku_00451():
    assert is_valid_sku_00451("abc123")
    assert not is_valid_sku_00451("")


def test_bucket_by_tag_00451():
    p = Product_00451("s1", 100, ["a"])
    assert bucket_by_tag_00451([p]) == {"a": ["s1"]}
