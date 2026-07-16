"""Tests for catalog_00450."""

import pytest

from cartservice.generated.catalog_00450 import (
    Product_00450,
    bucket_by_tag_00450,
    is_valid_sku_00450,
    price_with_tax_00450,
)


def test_price_with_tax_00450():
    assert price_with_tax_00450(1000, 500) == 1050


def test_price_with_tax_negative_00450():
    with pytest.raises(ValueError):
        price_with_tax_00450(1000, -1)


def test_is_valid_sku_00450():
    assert is_valid_sku_00450("abc123")
    assert not is_valid_sku_00450("")


def test_bucket_by_tag_00450():
    p = Product_00450("s1", 100, ["a"])
    assert bucket_by_tag_00450([p]) == {"a": ["s1"]}
