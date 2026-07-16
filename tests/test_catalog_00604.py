"""Tests for catalog_00604."""

import pytest

from cartservice.generated.catalog_00604 import (
    Product_00604,
    bucket_by_tag_00604,
    is_valid_sku_00604,
    price_with_tax_00604,
)


def test_price_with_tax_00604():
    assert price_with_tax_00604(1000, 500) == 1050


def test_price_with_tax_negative_00604():
    with pytest.raises(ValueError):
        price_with_tax_00604(1000, -1)


def test_is_valid_sku_00604():
    assert is_valid_sku_00604("abc123")
    assert not is_valid_sku_00604("")


def test_bucket_by_tag_00604():
    p = Product_00604("s1", 100, ["a"])
    assert bucket_by_tag_00604([p]) == {"a": ["s1"]}
