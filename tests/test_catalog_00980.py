"""Tests for catalog_00980."""

import pytest

from cartservice.generated.catalog_00980 import (
    Product_00980,
    bucket_by_tag_00980,
    is_valid_sku_00980,
    price_with_tax_00980,
)


def test_price_with_tax_00980():
    assert price_with_tax_00980(1000, 500) == 1050


def test_price_with_tax_negative_00980():
    with pytest.raises(ValueError):
        price_with_tax_00980(1000, -1)


def test_is_valid_sku_00980():
    assert is_valid_sku_00980("abc123")
    assert not is_valid_sku_00980("")


def test_bucket_by_tag_00980():
    p = Product_00980("s1", 100, ["a"])
    assert bucket_by_tag_00980([p]) == {"a": ["s1"]}
