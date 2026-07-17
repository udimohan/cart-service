"""Tests for catalog_01507."""

import pytest

from cartservice.generated.catalog_01507 import (
    Product_01507,
    bucket_by_tag_01507,
    is_valid_sku_01507,
    price_with_tax_01507,
)


def test_price_with_tax_01507():
    assert price_with_tax_01507(1000, 500) == 1050


def test_price_with_tax_negative_01507():
    with pytest.raises(ValueError):
        price_with_tax_01507(1000, -1)


def test_is_valid_sku_01507():
    assert is_valid_sku_01507("abc123")
    assert not is_valid_sku_01507("")


def test_bucket_by_tag_01507():
    p = Product_01507("s1", 100, ["a"])
    assert bucket_by_tag_01507([p]) == {"a": ["s1"]}
