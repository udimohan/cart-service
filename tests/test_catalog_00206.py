"""Tests for catalog_00206."""

import pytest

from cartservice.generated.catalog_00206 import (
    Product_00206,
    bucket_by_tag_00206,
    is_valid_sku_00206,
    price_with_tax_00206,
)


def test_price_with_tax_00206():
    assert price_with_tax_00206(1000, 500) == 1050


def test_price_with_tax_negative_00206():
    with pytest.raises(ValueError):
        price_with_tax_00206(1000, -1)


def test_is_valid_sku_00206():
    assert is_valid_sku_00206("abc123")
    assert not is_valid_sku_00206("")


def test_bucket_by_tag_00206():
    p = Product_00206("s1", 100, ["a"])
    assert bucket_by_tag_00206([p]) == {"a": ["s1"]}
