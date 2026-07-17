"""Tests for catalog_00099."""

import pytest

from cartservice.generated.catalog_00099 import (
    Product_00099,
    bucket_by_tag_00099,
    is_valid_sku_00099,
    price_with_tax_00099,
)


def test_price_with_tax_00099():
    assert price_with_tax_00099(1000, 500) == 1050


def test_price_with_tax_negative_00099():
    with pytest.raises(ValueError):
        price_with_tax_00099(1000, -1)


def test_is_valid_sku_00099():
    assert is_valid_sku_00099("abc123")
    assert not is_valid_sku_00099("")


def test_bucket_by_tag_00099():
    p = Product_00099("s1", 100, ["a"])
    assert bucket_by_tag_00099([p]) == {"a": ["s1"]}
