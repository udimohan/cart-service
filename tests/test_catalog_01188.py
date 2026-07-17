"""Tests for catalog_01188."""

import pytest

from cartservice.generated.catalog_01188 import (
    Product_01188,
    bucket_by_tag_01188,
    is_valid_sku_01188,
    price_with_tax_01188,
)


def test_price_with_tax_01188():
    assert price_with_tax_01188(1000, 500) == 1050


def test_price_with_tax_negative_01188():
    with pytest.raises(ValueError):
        price_with_tax_01188(1000, -1)


def test_is_valid_sku_01188():
    assert is_valid_sku_01188("abc123")
    assert not is_valid_sku_01188("")


def test_bucket_by_tag_01188():
    p = Product_01188("s1", 100, ["a"])
    assert bucket_by_tag_01188([p]) == {"a": ["s1"]}
