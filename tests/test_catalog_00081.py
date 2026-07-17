"""Tests for catalog_00081."""

import pytest

from cartservice.generated.catalog_00081 import (
    Product_00081,
    bucket_by_tag_00081,
    is_valid_sku_00081,
    price_with_tax_00081,
)


def test_price_with_tax_00081():
    assert price_with_tax_00081(1000, 500) == 1050


def test_price_with_tax_negative_00081():
    with pytest.raises(ValueError):
        price_with_tax_00081(1000, -1)


def test_is_valid_sku_00081():
    assert is_valid_sku_00081("abc123")
    assert not is_valid_sku_00081("")


def test_bucket_by_tag_00081():
    p = Product_00081("s1", 100, ["a"])
    assert bucket_by_tag_00081([p]) == {"a": ["s1"]}
