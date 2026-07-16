"""Tests for catalog_00795."""

import pytest

from cartservice.generated.catalog_00795 import (
    Product_00795,
    bucket_by_tag_00795,
    is_valid_sku_00795,
    price_with_tax_00795,
)


def test_price_with_tax_00795():
    assert price_with_tax_00795(1000, 500) == 1050


def test_price_with_tax_negative_00795():
    with pytest.raises(ValueError):
        price_with_tax_00795(1000, -1)


def test_is_valid_sku_00795():
    assert is_valid_sku_00795("abc123")
    assert not is_valid_sku_00795("")


def test_bucket_by_tag_00795():
    p = Product_00795("s1", 100, ["a"])
    assert bucket_by_tag_00795([p]) == {"a": ["s1"]}
