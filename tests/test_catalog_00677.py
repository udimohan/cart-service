"""Tests for catalog_00677."""

import pytest

from cartservice.generated.catalog_00677 import (
    Product_00677,
    bucket_by_tag_00677,
    is_valid_sku_00677,
    price_with_tax_00677,
)


def test_price_with_tax_00677():
    assert price_with_tax_00677(1000, 500) == 1050


def test_price_with_tax_negative_00677():
    with pytest.raises(ValueError):
        price_with_tax_00677(1000, -1)


def test_is_valid_sku_00677():
    assert is_valid_sku_00677("abc123")
    assert not is_valid_sku_00677("")


def test_bucket_by_tag_00677():
    p = Product_00677("s1", 100, ["a"])
    assert bucket_by_tag_00677([p]) == {"a": ["s1"]}
