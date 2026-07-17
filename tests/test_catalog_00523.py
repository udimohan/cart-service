"""Tests for catalog_00523."""

import pytest

from cartservice.generated.catalog_00523 import (
    Product_00523,
    bucket_by_tag_00523,
    is_valid_sku_00523,
    price_with_tax_00523,
)


def test_price_with_tax_00523():
    assert price_with_tax_00523(1000, 500) == 1050


def test_price_with_tax_negative_00523():
    with pytest.raises(ValueError):
        price_with_tax_00523(1000, -1)


def test_is_valid_sku_00523():
    assert is_valid_sku_00523("abc123")
    assert not is_valid_sku_00523("")


def test_bucket_by_tag_00523():
    p = Product_00523("s1", 100, ["a"])
    assert bucket_by_tag_00523([p]) == {"a": ["s1"]}
