"""Tests for catalog_01551."""

import pytest

from cartservice.generated.catalog_01551 import (
    Product_01551,
    bucket_by_tag_01551,
    is_valid_sku_01551,
    price_with_tax_01551,
)


def test_price_with_tax_01551():
    assert price_with_tax_01551(1000, 500) == 1050


def test_price_with_tax_negative_01551():
    with pytest.raises(ValueError):
        price_with_tax_01551(1000, -1)


def test_is_valid_sku_01551():
    assert is_valid_sku_01551("abc123")
    assert not is_valid_sku_01551("")


def test_bucket_by_tag_01551():
    p = Product_01551("s1", 100, ["a"])
    assert bucket_by_tag_01551([p]) == {"a": ["s1"]}
