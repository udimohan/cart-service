"""Tests for catalog_01009."""

import pytest

from cartservice.generated.catalog_01009 import (
    Product_01009,
    bucket_by_tag_01009,
    is_valid_sku_01009,
    price_with_tax_01009,
)


def test_price_with_tax_01009():
    assert price_with_tax_01009(1000, 500) == 1050


def test_price_with_tax_negative_01009():
    with pytest.raises(ValueError):
        price_with_tax_01009(1000, -1)


def test_is_valid_sku_01009():
    assert is_valid_sku_01009("abc123")
    assert not is_valid_sku_01009("")


def test_bucket_by_tag_01009():
    p = Product_01009("s1", 100, ["a"])
    assert bucket_by_tag_01009([p]) == {"a": ["s1"]}
