"""Tests for catalog_00146."""

import pytest

from cartservice.generated.catalog_00146 import (
    Product_00146,
    bucket_by_tag_00146,
    is_valid_sku_00146,
    price_with_tax_00146,
)


def test_price_with_tax_00146():
    assert price_with_tax_00146(1000, 500) == 1050


def test_price_with_tax_negative_00146():
    with pytest.raises(ValueError):
        price_with_tax_00146(1000, -1)


def test_is_valid_sku_00146():
    assert is_valid_sku_00146("abc123")
    assert not is_valid_sku_00146("")


def test_bucket_by_tag_00146():
    p = Product_00146("s1", 100, ["a"])
    assert bucket_by_tag_00146([p]) == {"a": ["s1"]}
