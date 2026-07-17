"""Tests for catalog_01214."""

import pytest

from cartservice.generated.catalog_01214 import (
    Product_01214,
    bucket_by_tag_01214,
    is_valid_sku_01214,
    price_with_tax_01214,
)


def test_price_with_tax_01214():
    assert price_with_tax_01214(1000, 500) == 1050


def test_price_with_tax_negative_01214():
    with pytest.raises(ValueError):
        price_with_tax_01214(1000, -1)


def test_is_valid_sku_01214():
    assert is_valid_sku_01214("abc123")
    assert not is_valid_sku_01214("")


def test_bucket_by_tag_01214():
    p = Product_01214("s1", 100, ["a"])
    assert bucket_by_tag_01214([p]) == {"a": ["s1"]}
