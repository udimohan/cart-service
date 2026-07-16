"""Tests for catalog_00596."""

import pytest

from cartservice.generated.catalog_00596 import (
    Product_00596,
    bucket_by_tag_00596,
    is_valid_sku_00596,
    price_with_tax_00596,
)


def test_price_with_tax_00596():
    assert price_with_tax_00596(1000, 500) == 1050


def test_price_with_tax_negative_00596():
    with pytest.raises(ValueError):
        price_with_tax_00596(1000, -1)


def test_is_valid_sku_00596():
    assert is_valid_sku_00596("abc123")
    assert not is_valid_sku_00596("")


def test_bucket_by_tag_00596():
    p = Product_00596("s1", 100, ["a"])
    assert bucket_by_tag_00596([p]) == {"a": ["s1"]}
