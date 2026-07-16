"""Tests for catalog_00872."""

import pytest

from cartservice.generated.catalog_00872 import (
    Product_00872,
    bucket_by_tag_00872,
    is_valid_sku_00872,
    price_with_tax_00872,
)


def test_price_with_tax_00872():
    assert price_with_tax_00872(1000, 500) == 1050


def test_price_with_tax_negative_00872():
    with pytest.raises(ValueError):
        price_with_tax_00872(1000, -1)


def test_is_valid_sku_00872():
    assert is_valid_sku_00872("abc123")
    assert not is_valid_sku_00872("")


def test_bucket_by_tag_00872():
    p = Product_00872("s1", 100, ["a"])
    assert bucket_by_tag_00872([p]) == {"a": ["s1"]}
