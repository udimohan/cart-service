"""Tests for catalog_01560."""

import pytest

from cartservice.generated.catalog_01560 import (
    Product_01560,
    bucket_by_tag_01560,
    is_valid_sku_01560,
    price_with_tax_01560,
)


def test_price_with_tax_01560():
    assert price_with_tax_01560(1000, 500) == 1050


def test_price_with_tax_negative_01560():
    with pytest.raises(ValueError):
        price_with_tax_01560(1000, -1)


def test_is_valid_sku_01560():
    assert is_valid_sku_01560("abc123")
    assert not is_valid_sku_01560("")


def test_bucket_by_tag_01560():
    p = Product_01560("s1", 100, ["a"])
    assert bucket_by_tag_01560([p]) == {"a": ["s1"]}
