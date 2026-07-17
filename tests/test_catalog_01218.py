"""Tests for catalog_01218."""

import pytest

from cartservice.generated.catalog_01218 import (
    Product_01218,
    bucket_by_tag_01218,
    is_valid_sku_01218,
    price_with_tax_01218,
)


def test_price_with_tax_01218():
    assert price_with_tax_01218(1000, 500) == 1050


def test_price_with_tax_negative_01218():
    with pytest.raises(ValueError):
        price_with_tax_01218(1000, -1)


def test_is_valid_sku_01218():
    assert is_valid_sku_01218("abc123")
    assert not is_valid_sku_01218("")


def test_bucket_by_tag_01218():
    p = Product_01218("s1", 100, ["a"])
    assert bucket_by_tag_01218([p]) == {"a": ["s1"]}
