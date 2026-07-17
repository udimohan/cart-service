"""Tests for catalog_00813."""

import pytest

from cartservice.generated.catalog_00813 import (
    Product_00813,
    bucket_by_tag_00813,
    is_valid_sku_00813,
    price_with_tax_00813,
)


def test_price_with_tax_00813():
    assert price_with_tax_00813(1000, 500) == 1050


def test_price_with_tax_negative_00813():
    with pytest.raises(ValueError):
        price_with_tax_00813(1000, -1)


def test_is_valid_sku_00813():
    assert is_valid_sku_00813("abc123")
    assert not is_valid_sku_00813("")


def test_bucket_by_tag_00813():
    p = Product_00813("s1", 100, ["a"])
    assert bucket_by_tag_00813([p]) == {"a": ["s1"]}
