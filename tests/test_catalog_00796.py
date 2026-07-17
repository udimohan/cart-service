"""Tests for catalog_00796."""

import pytest

from cartservice.generated.catalog_00796 import (
    Product_00796,
    bucket_by_tag_00796,
    is_valid_sku_00796,
    price_with_tax_00796,
)


def test_price_with_tax_00796():
    assert price_with_tax_00796(1000, 500) == 1050


def test_price_with_tax_negative_00796():
    with pytest.raises(ValueError):
        price_with_tax_00796(1000, -1)


def test_is_valid_sku_00796():
    assert is_valid_sku_00796("abc123")
    assert not is_valid_sku_00796("")


def test_bucket_by_tag_00796():
    p = Product_00796("s1", 100, ["a"])
    assert bucket_by_tag_00796([p]) == {"a": ["s1"]}
