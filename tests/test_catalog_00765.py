"""Tests for catalog_00765."""

import pytest

from cartservice.generated.catalog_00765 import (
    Product_00765,
    bucket_by_tag_00765,
    is_valid_sku_00765,
    price_with_tax_00765,
)


def test_price_with_tax_00765():
    assert price_with_tax_00765(1000, 500) == 1050


def test_price_with_tax_negative_00765():
    with pytest.raises(ValueError):
        price_with_tax_00765(1000, -1)


def test_is_valid_sku_00765():
    assert is_valid_sku_00765("abc123")
    assert not is_valid_sku_00765("")


def test_bucket_by_tag_00765():
    p = Product_00765("s1", 100, ["a"])
    assert bucket_by_tag_00765([p]) == {"a": ["s1"]}
