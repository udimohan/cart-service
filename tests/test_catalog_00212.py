"""Tests for catalog_00212."""

import pytest

from cartservice.generated.catalog_00212 import (
    Product_00212,
    bucket_by_tag_00212,
    is_valid_sku_00212,
    price_with_tax_00212,
)


def test_price_with_tax_00212():
    assert price_with_tax_00212(1000, 500) == 1050


def test_price_with_tax_negative_00212():
    with pytest.raises(ValueError):
        price_with_tax_00212(1000, -1)


def test_is_valid_sku_00212():
    assert is_valid_sku_00212("abc123")
    assert not is_valid_sku_00212("")


def test_bucket_by_tag_00212():
    p = Product_00212("s1", 100, ["a"])
    assert bucket_by_tag_00212([p]) == {"a": ["s1"]}
