"""Tests for catalog_00020."""

import pytest

from cartservice.generated.catalog_00020 import (
    Product_00020,
    bucket_by_tag_00020,
    is_valid_sku_00020,
    price_with_tax_00020,
)


def test_price_with_tax_00020():
    assert price_with_tax_00020(1000, 500) == 1050


def test_price_with_tax_negative_00020():
    with pytest.raises(ValueError):
        price_with_tax_00020(1000, -1)


def test_is_valid_sku_00020():
    assert is_valid_sku_00020("abc123")
    assert not is_valid_sku_00020("")


def test_bucket_by_tag_00020():
    p = Product_00020("s1", 100, ["a"])
    assert bucket_by_tag_00020([p]) == {"a": ["s1"]}
