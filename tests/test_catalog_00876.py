"""Tests for catalog_00876."""

import pytest

from cartservice.generated.catalog_00876 import (
    Product_00876,
    bucket_by_tag_00876,
    is_valid_sku_00876,
    price_with_tax_00876,
)


def test_price_with_tax_00876():
    assert price_with_tax_00876(1000, 500) == 1050


def test_price_with_tax_negative_00876():
    with pytest.raises(ValueError):
        price_with_tax_00876(1000, -1)


def test_is_valid_sku_00876():
    assert is_valid_sku_00876("abc123")
    assert not is_valid_sku_00876("")


def test_bucket_by_tag_00876():
    p = Product_00876("s1", 100, ["a"])
    assert bucket_by_tag_00876([p]) == {"a": ["s1"]}
