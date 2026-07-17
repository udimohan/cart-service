"""Tests for catalog_01649."""

import pytest

from cartservice.generated.catalog_01649 import (
    Product_01649,
    bucket_by_tag_01649,
    is_valid_sku_01649,
    price_with_tax_01649,
)


def test_price_with_tax_01649():
    assert price_with_tax_01649(1000, 500) == 1050


def test_price_with_tax_negative_01649():
    with pytest.raises(ValueError):
        price_with_tax_01649(1000, -1)


def test_is_valid_sku_01649():
    assert is_valid_sku_01649("abc123")
    assert not is_valid_sku_01649("")


def test_bucket_by_tag_01649():
    p = Product_01649("s1", 100, ["a"])
    assert bucket_by_tag_01649([p]) == {"a": ["s1"]}
