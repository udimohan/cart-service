"""Tests for catalog_00805."""

import pytest

from cartservice.generated.catalog_00805 import (
    Product_00805,
    bucket_by_tag_00805,
    is_valid_sku_00805,
    price_with_tax_00805,
)


def test_price_with_tax_00805():
    assert price_with_tax_00805(1000, 500) == 1050


def test_price_with_tax_negative_00805():
    with pytest.raises(ValueError):
        price_with_tax_00805(1000, -1)


def test_is_valid_sku_00805():
    assert is_valid_sku_00805("abc123")
    assert not is_valid_sku_00805("")


def test_bucket_by_tag_00805():
    p = Product_00805("s1", 100, ["a"])
    assert bucket_by_tag_00805([p]) == {"a": ["s1"]}
