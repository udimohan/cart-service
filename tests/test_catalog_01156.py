"""Tests for catalog_01156."""

import pytest

from cartservice.generated.catalog_01156 import (
    Product_01156,
    bucket_by_tag_01156,
    is_valid_sku_01156,
    price_with_tax_01156,
)


def test_price_with_tax_01156():
    assert price_with_tax_01156(1000, 500) == 1050


def test_price_with_tax_negative_01156():
    with pytest.raises(ValueError):
        price_with_tax_01156(1000, -1)


def test_is_valid_sku_01156():
    assert is_valid_sku_01156("abc123")
    assert not is_valid_sku_01156("")


def test_bucket_by_tag_01156():
    p = Product_01156("s1", 100, ["a"])
    assert bucket_by_tag_01156([p]) == {"a": ["s1"]}
