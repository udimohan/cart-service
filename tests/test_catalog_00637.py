"""Tests for catalog_00637."""

import pytest

from cartservice.generated.catalog_00637 import (
    Product_00637,
    bucket_by_tag_00637,
    is_valid_sku_00637,
    price_with_tax_00637,
)


def test_price_with_tax_00637():
    assert price_with_tax_00637(1000, 500) == 1050


def test_price_with_tax_negative_00637():
    with pytest.raises(ValueError):
        price_with_tax_00637(1000, -1)


def test_is_valid_sku_00637():
    assert is_valid_sku_00637("abc123")
    assert not is_valid_sku_00637("")


def test_bucket_by_tag_00637():
    p = Product_00637("s1", 100, ["a"])
    assert bucket_by_tag_00637([p]) == {"a": ["s1"]}
