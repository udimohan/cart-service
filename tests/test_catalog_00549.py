"""Tests for catalog_00549."""

import pytest

from cartservice.generated.catalog_00549 import (
    Product_00549,
    bucket_by_tag_00549,
    is_valid_sku_00549,
    price_with_tax_00549,
)


def test_price_with_tax_00549():
    assert price_with_tax_00549(1000, 500) == 1050


def test_price_with_tax_negative_00549():
    with pytest.raises(ValueError):
        price_with_tax_00549(1000, -1)


def test_is_valid_sku_00549():
    assert is_valid_sku_00549("abc123")
    assert not is_valid_sku_00549("")


def test_bucket_by_tag_00549():
    p = Product_00549("s1", 100, ["a"])
    assert bucket_by_tag_00549([p]) == {"a": ["s1"]}
