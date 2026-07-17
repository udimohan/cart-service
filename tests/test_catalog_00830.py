"""Tests for catalog_00830."""

import pytest

from cartservice.generated.catalog_00830 import (
    Product_00830,
    bucket_by_tag_00830,
    is_valid_sku_00830,
    price_with_tax_00830,
)


def test_price_with_tax_00830():
    assert price_with_tax_00830(1000, 500) == 1050


def test_price_with_tax_negative_00830():
    with pytest.raises(ValueError):
        price_with_tax_00830(1000, -1)


def test_is_valid_sku_00830():
    assert is_valid_sku_00830("abc123")
    assert not is_valid_sku_00830("")


def test_bucket_by_tag_00830():
    p = Product_00830("s1", 100, ["a"])
    assert bucket_by_tag_00830([p]) == {"a": ["s1"]}
