"""Tests for catalog_01451."""

import pytest

from cartservice.generated.catalog_01451 import (
    Product_01451,
    bucket_by_tag_01451,
    is_valid_sku_01451,
    price_with_tax_01451,
)


def test_price_with_tax_01451():
    assert price_with_tax_01451(1000, 500) == 1050


def test_price_with_tax_negative_01451():
    with pytest.raises(ValueError):
        price_with_tax_01451(1000, -1)


def test_is_valid_sku_01451():
    assert is_valid_sku_01451("abc123")
    assert not is_valid_sku_01451("")


def test_bucket_by_tag_01451():
    p = Product_01451("s1", 100, ["a"])
    assert bucket_by_tag_01451([p]) == {"a": ["s1"]}
