"""Tests for catalog_01043."""

import pytest

from cartservice.generated.catalog_01043 import (
    Product_01043,
    bucket_by_tag_01043,
    is_valid_sku_01043,
    price_with_tax_01043,
)


def test_price_with_tax_01043():
    assert price_with_tax_01043(1000, 500) == 1050


def test_price_with_tax_negative_01043():
    with pytest.raises(ValueError):
        price_with_tax_01043(1000, -1)


def test_is_valid_sku_01043():
    assert is_valid_sku_01043("abc123")
    assert not is_valid_sku_01043("")


def test_bucket_by_tag_01043():
    p = Product_01043("s1", 100, ["a"])
    assert bucket_by_tag_01043([p]) == {"a": ["s1"]}
