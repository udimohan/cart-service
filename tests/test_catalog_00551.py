"""Tests for catalog_00551."""

import pytest

from cartservice.generated.catalog_00551 import (
    Product_00551,
    bucket_by_tag_00551,
    is_valid_sku_00551,
    price_with_tax_00551,
)


def test_price_with_tax_00551():
    assert price_with_tax_00551(1000, 500) == 1050


def test_price_with_tax_negative_00551():
    with pytest.raises(ValueError):
        price_with_tax_00551(1000, -1)


def test_is_valid_sku_00551():
    assert is_valid_sku_00551("abc123")
    assert not is_valid_sku_00551("")


def test_bucket_by_tag_00551():
    p = Product_00551("s1", 100, ["a"])
    assert bucket_by_tag_00551([p]) == {"a": ["s1"]}
