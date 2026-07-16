"""Tests for catalog_00693."""

import pytest

from cartservice.generated.catalog_00693 import (
    Product_00693,
    bucket_by_tag_00693,
    is_valid_sku_00693,
    price_with_tax_00693,
)


def test_price_with_tax_00693():
    assert price_with_tax_00693(1000, 500) == 1050


def test_price_with_tax_negative_00693():
    with pytest.raises(ValueError):
        price_with_tax_00693(1000, -1)


def test_is_valid_sku_00693():
    assert is_valid_sku_00693("abc123")
    assert not is_valid_sku_00693("")


def test_bucket_by_tag_00693():
    p = Product_00693("s1", 100, ["a"])
    assert bucket_by_tag_00693([p]) == {"a": ["s1"]}
