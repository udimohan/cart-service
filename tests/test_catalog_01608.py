"""Tests for catalog_01608."""

import pytest

from cartservice.generated.catalog_01608 import (
    Product_01608,
    bucket_by_tag_01608,
    is_valid_sku_01608,
    price_with_tax_01608,
)


def test_price_with_tax_01608():
    assert price_with_tax_01608(1000, 500) == 1050


def test_price_with_tax_negative_01608():
    with pytest.raises(ValueError):
        price_with_tax_01608(1000, -1)


def test_is_valid_sku_01608():
    assert is_valid_sku_01608("abc123")
    assert not is_valid_sku_01608("")


def test_bucket_by_tag_01608():
    p = Product_01608("s1", 100, ["a"])
    assert bucket_by_tag_01608([p]) == {"a": ["s1"]}
