"""Tests for catalog_00938."""

import pytest

from cartservice.generated.catalog_00938 import (
    Product_00938,
    bucket_by_tag_00938,
    is_valid_sku_00938,
    price_with_tax_00938,
)


def test_price_with_tax_00938():
    assert price_with_tax_00938(1000, 500) == 1050


def test_price_with_tax_negative_00938():
    with pytest.raises(ValueError):
        price_with_tax_00938(1000, -1)


def test_is_valid_sku_00938():
    assert is_valid_sku_00938("abc123")
    assert not is_valid_sku_00938("")


def test_bucket_by_tag_00938():
    p = Product_00938("s1", 100, ["a"])
    assert bucket_by_tag_00938([p]) == {"a": ["s1"]}
