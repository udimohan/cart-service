"""Tests for catalog_01142."""

import pytest

from cartservice.generated.catalog_01142 import (
    Product_01142,
    bucket_by_tag_01142,
    is_valid_sku_01142,
    price_with_tax_01142,
)


def test_price_with_tax_01142():
    assert price_with_tax_01142(1000, 500) == 1050


def test_price_with_tax_negative_01142():
    with pytest.raises(ValueError):
        price_with_tax_01142(1000, -1)


def test_is_valid_sku_01142():
    assert is_valid_sku_01142("abc123")
    assert not is_valid_sku_01142("")


def test_bucket_by_tag_01142():
    p = Product_01142("s1", 100, ["a"])
    assert bucket_by_tag_01142([p]) == {"a": ["s1"]}
