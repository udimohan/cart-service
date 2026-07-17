"""Tests for catalog_01549."""

import pytest

from cartservice.generated.catalog_01549 import (
    Product_01549,
    bucket_by_tag_01549,
    is_valid_sku_01549,
    price_with_tax_01549,
)


def test_price_with_tax_01549():
    assert price_with_tax_01549(1000, 500) == 1050


def test_price_with_tax_negative_01549():
    with pytest.raises(ValueError):
        price_with_tax_01549(1000, -1)


def test_is_valid_sku_01549():
    assert is_valid_sku_01549("abc123")
    assert not is_valid_sku_01549("")


def test_bucket_by_tag_01549():
    p = Product_01549("s1", 100, ["a"])
    assert bucket_by_tag_01549([p]) == {"a": ["s1"]}
