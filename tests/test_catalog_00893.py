"""Tests for catalog_00893."""

import pytest

from cartservice.generated.catalog_00893 import (
    Product_00893,
    bucket_by_tag_00893,
    is_valid_sku_00893,
    price_with_tax_00893,
)


def test_price_with_tax_00893():
    assert price_with_tax_00893(1000, 500) == 1050


def test_price_with_tax_negative_00893():
    with pytest.raises(ValueError):
        price_with_tax_00893(1000, -1)


def test_is_valid_sku_00893():
    assert is_valid_sku_00893("abc123")
    assert not is_valid_sku_00893("")


def test_bucket_by_tag_00893():
    p = Product_00893("s1", 100, ["a"])
    assert bucket_by_tag_00893([p]) == {"a": ["s1"]}
