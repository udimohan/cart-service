"""Tests for catalog_00611."""

import pytest

from cartservice.generated.catalog_00611 import (
    Product_00611,
    bucket_by_tag_00611,
    is_valid_sku_00611,
    price_with_tax_00611,
)


def test_price_with_tax_00611():
    assert price_with_tax_00611(1000, 500) == 1050


def test_price_with_tax_negative_00611():
    with pytest.raises(ValueError):
        price_with_tax_00611(1000, -1)


def test_is_valid_sku_00611():
    assert is_valid_sku_00611("abc123")
    assert not is_valid_sku_00611("")


def test_bucket_by_tag_00611():
    p = Product_00611("s1", 100, ["a"])
    assert bucket_by_tag_00611([p]) == {"a": ["s1"]}
