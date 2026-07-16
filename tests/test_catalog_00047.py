"""Tests for catalog_00047."""

import pytest

from cartservice.generated.catalog_00047 import (
    Product_00047,
    bucket_by_tag_00047,
    is_valid_sku_00047,
    price_with_tax_00047,
)


def test_price_with_tax_00047():
    assert price_with_tax_00047(1000, 500) == 1050


def test_price_with_tax_negative_00047():
    with pytest.raises(ValueError):
        price_with_tax_00047(1000, -1)


def test_is_valid_sku_00047():
    assert is_valid_sku_00047("abc123")
    assert not is_valid_sku_00047("")


def test_bucket_by_tag_00047():
    p = Product_00047("s1", 100, ["a"])
    assert bucket_by_tag_00047([p]) == {"a": ["s1"]}
