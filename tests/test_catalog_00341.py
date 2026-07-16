"""Tests for catalog_00341."""

import pytest

from cartservice.generated.catalog_00341 import (
    Product_00341,
    bucket_by_tag_00341,
    is_valid_sku_00341,
    price_with_tax_00341,
)


def test_price_with_tax_00341():
    assert price_with_tax_00341(1000, 500) == 1050


def test_price_with_tax_negative_00341():
    with pytest.raises(ValueError):
        price_with_tax_00341(1000, -1)


def test_is_valid_sku_00341():
    assert is_valid_sku_00341("abc123")
    assert not is_valid_sku_00341("")


def test_bucket_by_tag_00341():
    p = Product_00341("s1", 100, ["a"])
    assert bucket_by_tag_00341([p]) == {"a": ["s1"]}
