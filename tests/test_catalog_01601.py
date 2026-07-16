"""Tests for catalog_01601."""

import pytest

from cartservice.generated.catalog_01601 import (
    Product_01601,
    bucket_by_tag_01601,
    is_valid_sku_01601,
    price_with_tax_01601,
)


def test_price_with_tax_01601():
    assert price_with_tax_01601(1000, 500) == 1050


def test_price_with_tax_negative_01601():
    with pytest.raises(ValueError):
        price_with_tax_01601(1000, -1)


def test_is_valid_sku_01601():
    assert is_valid_sku_01601("abc123")
    assert not is_valid_sku_01601("")


def test_bucket_by_tag_01601():
    p = Product_01601("s1", 100, ["a"])
    assert bucket_by_tag_01601([p]) == {"a": ["s1"]}
