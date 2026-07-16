"""Tests for catalog_01260."""

import pytest

from cartservice.generated.catalog_01260 import (
    Product_01260,
    bucket_by_tag_01260,
    is_valid_sku_01260,
    price_with_tax_01260,
)


def test_price_with_tax_01260():
    assert price_with_tax_01260(1000, 500) == 1050


def test_price_with_tax_negative_01260():
    with pytest.raises(ValueError):
        price_with_tax_01260(1000, -1)


def test_is_valid_sku_01260():
    assert is_valid_sku_01260("abc123")
    assert not is_valid_sku_01260("")


def test_bucket_by_tag_01260():
    p = Product_01260("s1", 100, ["a"])
    assert bucket_by_tag_01260([p]) == {"a": ["s1"]}
