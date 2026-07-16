"""Tests for catalog_00227."""

import pytest

from cartservice.generated.catalog_00227 import (
    Product_00227,
    bucket_by_tag_00227,
    is_valid_sku_00227,
    price_with_tax_00227,
)


def test_price_with_tax_00227():
    assert price_with_tax_00227(1000, 500) == 1050


def test_price_with_tax_negative_00227():
    with pytest.raises(ValueError):
        price_with_tax_00227(1000, -1)


def test_is_valid_sku_00227():
    assert is_valid_sku_00227("abc123")
    assert not is_valid_sku_00227("")


def test_bucket_by_tag_00227():
    p = Product_00227("s1", 100, ["a"])
    assert bucket_by_tag_00227([p]) == {"a": ["s1"]}
