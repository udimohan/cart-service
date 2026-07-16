"""Tests for catalog_01389."""

import pytest

from cartservice.generated.catalog_01389 import (
    Product_01389,
    bucket_by_tag_01389,
    is_valid_sku_01389,
    price_with_tax_01389,
)


def test_price_with_tax_01389():
    assert price_with_tax_01389(1000, 500) == 1050


def test_price_with_tax_negative_01389():
    with pytest.raises(ValueError):
        price_with_tax_01389(1000, -1)


def test_is_valid_sku_01389():
    assert is_valid_sku_01389("abc123")
    assert not is_valid_sku_01389("")


def test_bucket_by_tag_01389():
    p = Product_01389("s1", 100, ["a"])
    assert bucket_by_tag_01389([p]) == {"a": ["s1"]}
