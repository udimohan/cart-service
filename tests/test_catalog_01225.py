"""Tests for catalog_01225."""

import pytest

from cartservice.generated.catalog_01225 import (
    Product_01225,
    bucket_by_tag_01225,
    is_valid_sku_01225,
    price_with_tax_01225,
)


def test_price_with_tax_01225():
    assert price_with_tax_01225(1000, 500) == 1050


def test_price_with_tax_negative_01225():
    with pytest.raises(ValueError):
        price_with_tax_01225(1000, -1)


def test_is_valid_sku_01225():
    assert is_valid_sku_01225("abc123")
    assert not is_valid_sku_01225("")


def test_bucket_by_tag_01225():
    p = Product_01225("s1", 100, ["a"])
    assert bucket_by_tag_01225([p]) == {"a": ["s1"]}
