"""Tests for catalog_01677."""

import pytest

from cartservice.generated.catalog_01677 import (
    Product_01677,
    bucket_by_tag_01677,
    is_valid_sku_01677,
    price_with_tax_01677,
)


def test_price_with_tax_01677():
    assert price_with_tax_01677(1000, 500) == 1050


def test_price_with_tax_negative_01677():
    with pytest.raises(ValueError):
        price_with_tax_01677(1000, -1)


def test_is_valid_sku_01677():
    assert is_valid_sku_01677("abc123")
    assert not is_valid_sku_01677("")


def test_bucket_by_tag_01677():
    p = Product_01677("s1", 100, ["a"])
    assert bucket_by_tag_01677([p]) == {"a": ["s1"]}
