"""Tests for catalog_00366."""

import pytest

from cartservice.generated.catalog_00366 import (
    Product_00366,
    bucket_by_tag_00366,
    is_valid_sku_00366,
    price_with_tax_00366,
)


def test_price_with_tax_00366():
    assert price_with_tax_00366(1000, 500) == 1050


def test_price_with_tax_negative_00366():
    with pytest.raises(ValueError):
        price_with_tax_00366(1000, -1)


def test_is_valid_sku_00366():
    assert is_valid_sku_00366("abc123")
    assert not is_valid_sku_00366("")


def test_bucket_by_tag_00366():
    p = Product_00366("s1", 100, ["a"])
    assert bucket_by_tag_00366([p]) == {"a": ["s1"]}
