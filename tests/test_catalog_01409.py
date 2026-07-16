"""Tests for catalog_01409."""

import pytest

from cartservice.generated.catalog_01409 import (
    Product_01409,
    bucket_by_tag_01409,
    is_valid_sku_01409,
    price_with_tax_01409,
)


def test_price_with_tax_01409():
    assert price_with_tax_01409(1000, 500) == 1050


def test_price_with_tax_negative_01409():
    with pytest.raises(ValueError):
        price_with_tax_01409(1000, -1)


def test_is_valid_sku_01409():
    assert is_valid_sku_01409("abc123")
    assert not is_valid_sku_01409("")


def test_bucket_by_tag_01409():
    p = Product_01409("s1", 100, ["a"])
    assert bucket_by_tag_01409([p]) == {"a": ["s1"]}
