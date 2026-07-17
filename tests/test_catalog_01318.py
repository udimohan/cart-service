"""Tests for catalog_01318."""

import pytest

from cartservice.generated.catalog_01318 import (
    Product_01318,
    bucket_by_tag_01318,
    is_valid_sku_01318,
    price_with_tax_01318,
)


def test_price_with_tax_01318():
    assert price_with_tax_01318(1000, 500) == 1050


def test_price_with_tax_negative_01318():
    with pytest.raises(ValueError):
        price_with_tax_01318(1000, -1)


def test_is_valid_sku_01318():
    assert is_valid_sku_01318("abc123")
    assert not is_valid_sku_01318("")


def test_bucket_by_tag_01318():
    p = Product_01318("s1", 100, ["a"])
    assert bucket_by_tag_01318([p]) == {"a": ["s1"]}
