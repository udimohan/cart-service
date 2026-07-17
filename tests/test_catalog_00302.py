"""Tests for catalog_00302."""

import pytest

from cartservice.generated.catalog_00302 import (
    Product_00302,
    bucket_by_tag_00302,
    is_valid_sku_00302,
    price_with_tax_00302,
)


def test_price_with_tax_00302():
    assert price_with_tax_00302(1000, 500) == 1050


def test_price_with_tax_negative_00302():
    with pytest.raises(ValueError):
        price_with_tax_00302(1000, -1)


def test_is_valid_sku_00302():
    assert is_valid_sku_00302("abc123")
    assert not is_valid_sku_00302("")


def test_bucket_by_tag_00302():
    p = Product_00302("s1", 100, ["a"])
    assert bucket_by_tag_00302([p]) == {"a": ["s1"]}
