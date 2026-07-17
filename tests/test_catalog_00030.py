"""Tests for catalog_00030."""

import pytest

from cartservice.generated.catalog_00030 import (
    Product_00030,
    bucket_by_tag_00030,
    is_valid_sku_00030,
    price_with_tax_00030,
)


def test_price_with_tax_00030():
    assert price_with_tax_00030(1000, 500) == 1050


def test_price_with_tax_negative_00030():
    with pytest.raises(ValueError):
        price_with_tax_00030(1000, -1)


def test_is_valid_sku_00030():
    assert is_valid_sku_00030("abc123")
    assert not is_valid_sku_00030("")


def test_bucket_by_tag_00030():
    p = Product_00030("s1", 100, ["a"])
    assert bucket_by_tag_00030([p]) == {"a": ["s1"]}
