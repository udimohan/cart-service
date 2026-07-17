"""Tests for catalog_00649."""

import pytest

from cartservice.generated.catalog_00649 import (
    Product_00649,
    bucket_by_tag_00649,
    is_valid_sku_00649,
    price_with_tax_00649,
)


def test_price_with_tax_00649():
    assert price_with_tax_00649(1000, 500) == 1050


def test_price_with_tax_negative_00649():
    with pytest.raises(ValueError):
        price_with_tax_00649(1000, -1)


def test_is_valid_sku_00649():
    assert is_valid_sku_00649("abc123")
    assert not is_valid_sku_00649("")


def test_bucket_by_tag_00649():
    p = Product_00649("s1", 100, ["a"])
    assert bucket_by_tag_00649([p]) == {"a": ["s1"]}
