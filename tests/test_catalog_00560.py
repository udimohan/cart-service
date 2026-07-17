"""Tests for catalog_00560."""

import pytest

from cartservice.generated.catalog_00560 import (
    Product_00560,
    bucket_by_tag_00560,
    is_valid_sku_00560,
    price_with_tax_00560,
)


def test_price_with_tax_00560():
    assert price_with_tax_00560(1000, 500) == 1050


def test_price_with_tax_negative_00560():
    with pytest.raises(ValueError):
        price_with_tax_00560(1000, -1)


def test_is_valid_sku_00560():
    assert is_valid_sku_00560("abc123")
    assert not is_valid_sku_00560("")


def test_bucket_by_tag_00560():
    p = Product_00560("s1", 100, ["a"])
    assert bucket_by_tag_00560([p]) == {"a": ["s1"]}
