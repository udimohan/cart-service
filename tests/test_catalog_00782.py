"""Tests for catalog_00782."""

import pytest

from cartservice.generated.catalog_00782 import (
    Product_00782,
    bucket_by_tag_00782,
    is_valid_sku_00782,
    price_with_tax_00782,
)


def test_price_with_tax_00782():
    assert price_with_tax_00782(1000, 500) == 1050


def test_price_with_tax_negative_00782():
    with pytest.raises(ValueError):
        price_with_tax_00782(1000, -1)


def test_is_valid_sku_00782():
    assert is_valid_sku_00782("abc123")
    assert not is_valid_sku_00782("")


def test_bucket_by_tag_00782():
    p = Product_00782("s1", 100, ["a"])
    assert bucket_by_tag_00782([p]) == {"a": ["s1"]}
