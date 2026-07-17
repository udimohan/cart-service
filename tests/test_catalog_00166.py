"""Tests for catalog_00166."""

import pytest

from cartservice.generated.catalog_00166 import (
    Product_00166,
    bucket_by_tag_00166,
    is_valid_sku_00166,
    price_with_tax_00166,
)


def test_price_with_tax_00166():
    assert price_with_tax_00166(1000, 500) == 1050


def test_price_with_tax_negative_00166():
    with pytest.raises(ValueError):
        price_with_tax_00166(1000, -1)


def test_is_valid_sku_00166():
    assert is_valid_sku_00166("abc123")
    assert not is_valid_sku_00166("")


def test_bucket_by_tag_00166():
    p = Product_00166("s1", 100, ["a"])
    assert bucket_by_tag_00166([p]) == {"a": ["s1"]}
