"""Tests for catalog_01295."""

import pytest

from cartservice.generated.catalog_01295 import (
    Product_01295,
    bucket_by_tag_01295,
    is_valid_sku_01295,
    price_with_tax_01295,
)


def test_price_with_tax_01295():
    assert price_with_tax_01295(1000, 500) == 1050


def test_price_with_tax_negative_01295():
    with pytest.raises(ValueError):
        price_with_tax_01295(1000, -1)


def test_is_valid_sku_01295():
    assert is_valid_sku_01295("abc123")
    assert not is_valid_sku_01295("")


def test_bucket_by_tag_01295():
    p = Product_01295("s1", 100, ["a"])
    assert bucket_by_tag_01295([p]) == {"a": ["s1"]}
