"""Tests for catalog_00802."""

import pytest

from cartservice.generated.catalog_00802 import (
    Product_00802,
    bucket_by_tag_00802,
    is_valid_sku_00802,
    price_with_tax_00802,
)


def test_price_with_tax_00802():
    assert price_with_tax_00802(1000, 500) == 1050


def test_price_with_tax_negative_00802():
    with pytest.raises(ValueError):
        price_with_tax_00802(1000, -1)


def test_is_valid_sku_00802():
    assert is_valid_sku_00802("abc123")
    assert not is_valid_sku_00802("")


def test_bucket_by_tag_00802():
    p = Product_00802("s1", 100, ["a"])
    assert bucket_by_tag_00802([p]) == {"a": ["s1"]}
