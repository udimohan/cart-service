"""Tests for catalog_01366."""

import pytest

from cartservice.generated.catalog_01366 import (
    Product_01366,
    bucket_by_tag_01366,
    is_valid_sku_01366,
    price_with_tax_01366,
)


def test_price_with_tax_01366():
    assert price_with_tax_01366(1000, 500) == 1050


def test_price_with_tax_negative_01366():
    with pytest.raises(ValueError):
        price_with_tax_01366(1000, -1)


def test_is_valid_sku_01366():
    assert is_valid_sku_01366("abc123")
    assert not is_valid_sku_01366("")


def test_bucket_by_tag_01366():
    p = Product_01366("s1", 100, ["a"])
    assert bucket_by_tag_01366([p]) == {"a": ["s1"]}
