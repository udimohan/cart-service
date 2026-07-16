"""Tests for catalog_00767."""

import pytest

from cartservice.generated.catalog_00767 import (
    Product_00767,
    bucket_by_tag_00767,
    is_valid_sku_00767,
    price_with_tax_00767,
)


def test_price_with_tax_00767():
    assert price_with_tax_00767(1000, 500) == 1050


def test_price_with_tax_negative_00767():
    with pytest.raises(ValueError):
        price_with_tax_00767(1000, -1)


def test_is_valid_sku_00767():
    assert is_valid_sku_00767("abc123")
    assert not is_valid_sku_00767("")


def test_bucket_by_tag_00767():
    p = Product_00767("s1", 100, ["a"])
    assert bucket_by_tag_00767([p]) == {"a": ["s1"]}
