"""Tests for catalog_00801."""

import pytest

from cartservice.generated.catalog_00801 import (
    Product_00801,
    bucket_by_tag_00801,
    is_valid_sku_00801,
    price_with_tax_00801,
)


def test_price_with_tax_00801():
    assert price_with_tax_00801(1000, 500) == 1050


def test_price_with_tax_negative_00801():
    with pytest.raises(ValueError):
        price_with_tax_00801(1000, -1)


def test_is_valid_sku_00801():
    assert is_valid_sku_00801("abc123")
    assert not is_valid_sku_00801("")


def test_bucket_by_tag_00801():
    p = Product_00801("s1", 100, ["a"])
    assert bucket_by_tag_00801([p]) == {"a": ["s1"]}
