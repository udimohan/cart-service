"""Tests for catalog_00267."""

import pytest

from cartservice.generated.catalog_00267 import (
    Product_00267,
    bucket_by_tag_00267,
    is_valid_sku_00267,
    price_with_tax_00267,
)


def test_price_with_tax_00267():
    assert price_with_tax_00267(1000, 500) == 1050


def test_price_with_tax_negative_00267():
    with pytest.raises(ValueError):
        price_with_tax_00267(1000, -1)


def test_is_valid_sku_00267():
    assert is_valid_sku_00267("abc123")
    assert not is_valid_sku_00267("")


def test_bucket_by_tag_00267():
    p = Product_00267("s1", 100, ["a"])
    assert bucket_by_tag_00267([p]) == {"a": ["s1"]}
