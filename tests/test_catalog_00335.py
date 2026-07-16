"""Tests for catalog_00335."""

import pytest

from cartservice.generated.catalog_00335 import (
    Product_00335,
    bucket_by_tag_00335,
    is_valid_sku_00335,
    price_with_tax_00335,
)


def test_price_with_tax_00335():
    assert price_with_tax_00335(1000, 500) == 1050


def test_price_with_tax_negative_00335():
    with pytest.raises(ValueError):
        price_with_tax_00335(1000, -1)


def test_is_valid_sku_00335():
    assert is_valid_sku_00335("abc123")
    assert not is_valid_sku_00335("")


def test_bucket_by_tag_00335():
    p = Product_00335("s1", 100, ["a"])
    assert bucket_by_tag_00335([p]) == {"a": ["s1"]}
