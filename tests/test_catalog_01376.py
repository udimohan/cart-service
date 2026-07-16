"""Tests for catalog_01376."""

import pytest

from cartservice.generated.catalog_01376 import (
    Product_01376,
    bucket_by_tag_01376,
    is_valid_sku_01376,
    price_with_tax_01376,
)


def test_price_with_tax_01376():
    assert price_with_tax_01376(1000, 500) == 1050


def test_price_with_tax_negative_01376():
    with pytest.raises(ValueError):
        price_with_tax_01376(1000, -1)


def test_is_valid_sku_01376():
    assert is_valid_sku_01376("abc123")
    assert not is_valid_sku_01376("")


def test_bucket_by_tag_01376():
    p = Product_01376("s1", 100, ["a"])
    assert bucket_by_tag_01376([p]) == {"a": ["s1"]}
