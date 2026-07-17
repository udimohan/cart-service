"""Tests for catalog_00583."""

import pytest

from cartservice.generated.catalog_00583 import (
    Product_00583,
    bucket_by_tag_00583,
    is_valid_sku_00583,
    price_with_tax_00583,
)


def test_price_with_tax_00583():
    assert price_with_tax_00583(1000, 500) == 1050


def test_price_with_tax_negative_00583():
    with pytest.raises(ValueError):
        price_with_tax_00583(1000, -1)


def test_is_valid_sku_00583():
    assert is_valid_sku_00583("abc123")
    assert not is_valid_sku_00583("")


def test_bucket_by_tag_00583():
    p = Product_00583("s1", 100, ["a"])
    assert bucket_by_tag_00583([p]) == {"a": ["s1"]}
