"""Tests for catalog_01312."""

import pytest

from cartservice.generated.catalog_01312 import (
    Product_01312,
    bucket_by_tag_01312,
    is_valid_sku_01312,
    price_with_tax_01312,
)


def test_price_with_tax_01312():
    assert price_with_tax_01312(1000, 500) == 1050


def test_price_with_tax_negative_01312():
    with pytest.raises(ValueError):
        price_with_tax_01312(1000, -1)


def test_is_valid_sku_01312():
    assert is_valid_sku_01312("abc123")
    assert not is_valid_sku_01312("")


def test_bucket_by_tag_01312():
    p = Product_01312("s1", 100, ["a"])
    assert bucket_by_tag_01312([p]) == {"a": ["s1"]}
