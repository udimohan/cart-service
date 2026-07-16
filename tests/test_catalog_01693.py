"""Tests for catalog_01693."""

import pytest

from cartservice.generated.catalog_01693 import (
    Product_01693,
    bucket_by_tag_01693,
    is_valid_sku_01693,
    price_with_tax_01693,
)


def test_price_with_tax_01693():
    assert price_with_tax_01693(1000, 500) == 1050


def test_price_with_tax_negative_01693():
    with pytest.raises(ValueError):
        price_with_tax_01693(1000, -1)


def test_is_valid_sku_01693():
    assert is_valid_sku_01693("abc123")
    assert not is_valid_sku_01693("")


def test_bucket_by_tag_01693():
    p = Product_01693("s1", 100, ["a"])
    assert bucket_by_tag_01693([p]) == {"a": ["s1"]}
