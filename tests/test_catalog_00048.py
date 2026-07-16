"""Tests for catalog_00048."""

import pytest

from cartservice.generated.catalog_00048 import (
    Product_00048,
    bucket_by_tag_00048,
    is_valid_sku_00048,
    price_with_tax_00048,
)


def test_price_with_tax_00048():
    assert price_with_tax_00048(1000, 500) == 1050


def test_price_with_tax_negative_00048():
    with pytest.raises(ValueError):
        price_with_tax_00048(1000, -1)


def test_is_valid_sku_00048():
    assert is_valid_sku_00048("abc123")
    assert not is_valid_sku_00048("")


def test_bucket_by_tag_00048():
    p = Product_00048("s1", 100, ["a"])
    assert bucket_by_tag_00048([p]) == {"a": ["s1"]}
