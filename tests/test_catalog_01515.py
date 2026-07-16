"""Tests for catalog_01515."""

import pytest

from cartservice.generated.catalog_01515 import (
    Product_01515,
    bucket_by_tag_01515,
    is_valid_sku_01515,
    price_with_tax_01515,
)


def test_price_with_tax_01515():
    assert price_with_tax_01515(1000, 500) == 1050


def test_price_with_tax_negative_01515():
    with pytest.raises(ValueError):
        price_with_tax_01515(1000, -1)


def test_is_valid_sku_01515():
    assert is_valid_sku_01515("abc123")
    assert not is_valid_sku_01515("")


def test_bucket_by_tag_01515():
    p = Product_01515("s1", 100, ["a"])
    assert bucket_by_tag_01515([p]) == {"a": ["s1"]}
