"""Tests for catalog_00408."""

import pytest

from cartservice.generated.catalog_00408 import (
    Product_00408,
    bucket_by_tag_00408,
    is_valid_sku_00408,
    price_with_tax_00408,
)


def test_price_with_tax_00408():
    assert price_with_tax_00408(1000, 500) == 1050


def test_price_with_tax_negative_00408():
    with pytest.raises(ValueError):
        price_with_tax_00408(1000, -1)


def test_is_valid_sku_00408():
    assert is_valid_sku_00408("abc123")
    assert not is_valid_sku_00408("")


def test_bucket_by_tag_00408():
    p = Product_00408("s1", 100, ["a"])
    assert bucket_by_tag_00408([p]) == {"a": ["s1"]}
