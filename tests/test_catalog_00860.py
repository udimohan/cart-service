"""Tests for catalog_00860."""

import pytest

from cartservice.generated.catalog_00860 import (
    Product_00860,
    bucket_by_tag_00860,
    is_valid_sku_00860,
    price_with_tax_00860,
)


def test_price_with_tax_00860():
    assert price_with_tax_00860(1000, 500) == 1050


def test_price_with_tax_negative_00860():
    with pytest.raises(ValueError):
        price_with_tax_00860(1000, -1)


def test_is_valid_sku_00860():
    assert is_valid_sku_00860("abc123")
    assert not is_valid_sku_00860("")


def test_bucket_by_tag_00860():
    p = Product_00860("s1", 100, ["a"])
    assert bucket_by_tag_00860([p]) == {"a": ["s1"]}
