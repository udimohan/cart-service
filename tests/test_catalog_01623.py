"""Tests for catalog_01623."""

import pytest

from cartservice.generated.catalog_01623 import (
    Product_01623,
    bucket_by_tag_01623,
    is_valid_sku_01623,
    price_with_tax_01623,
)


def test_price_with_tax_01623():
    assert price_with_tax_01623(1000, 500) == 1050


def test_price_with_tax_negative_01623():
    with pytest.raises(ValueError):
        price_with_tax_01623(1000, -1)


def test_is_valid_sku_01623():
    assert is_valid_sku_01623("abc123")
    assert not is_valid_sku_01623("")


def test_bucket_by_tag_01623():
    p = Product_01623("s1", 100, ["a"])
    assert bucket_by_tag_01623([p]) == {"a": ["s1"]}
