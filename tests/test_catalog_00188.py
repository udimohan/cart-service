"""Tests for catalog_00188."""

import pytest

from cartservice.generated.catalog_00188 import (
    Product_00188,
    bucket_by_tag_00188,
    is_valid_sku_00188,
    price_with_tax_00188,
)


def test_price_with_tax_00188():
    assert price_with_tax_00188(1000, 500) == 1050


def test_price_with_tax_negative_00188():
    with pytest.raises(ValueError):
        price_with_tax_00188(1000, -1)


def test_is_valid_sku_00188():
    assert is_valid_sku_00188("abc123")
    assert not is_valid_sku_00188("")


def test_bucket_by_tag_00188():
    p = Product_00188("s1", 100, ["a"])
    assert bucket_by_tag_00188([p]) == {"a": ["s1"]}
