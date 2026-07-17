"""Tests for catalog_01378."""

import pytest

from cartservice.generated.catalog_01378 import (
    Product_01378,
    bucket_by_tag_01378,
    is_valid_sku_01378,
    price_with_tax_01378,
)


def test_price_with_tax_01378():
    assert price_with_tax_01378(1000, 500) == 1050


def test_price_with_tax_negative_01378():
    with pytest.raises(ValueError):
        price_with_tax_01378(1000, -1)


def test_is_valid_sku_01378():
    assert is_valid_sku_01378("abc123")
    assert not is_valid_sku_01378("")


def test_bucket_by_tag_01378():
    p = Product_01378("s1", 100, ["a"])
    assert bucket_by_tag_01378([p]) == {"a": ["s1"]}
