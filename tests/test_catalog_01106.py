"""Tests for catalog_01106."""

import pytest

from cartservice.generated.catalog_01106 import (
    Product_01106,
    bucket_by_tag_01106,
    is_valid_sku_01106,
    price_with_tax_01106,
)


def test_price_with_tax_01106():
    assert price_with_tax_01106(1000, 500) == 1050


def test_price_with_tax_negative_01106():
    with pytest.raises(ValueError):
        price_with_tax_01106(1000, -1)


def test_is_valid_sku_01106():
    assert is_valid_sku_01106("abc123")
    assert not is_valid_sku_01106("")


def test_bucket_by_tag_01106():
    p = Product_01106("s1", 100, ["a"])
    assert bucket_by_tag_01106([p]) == {"a": ["s1"]}
