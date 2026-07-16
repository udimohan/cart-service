"""Tests for catalog_00719."""

import pytest

from cartservice.generated.catalog_00719 import (
    Product_00719,
    bucket_by_tag_00719,
    is_valid_sku_00719,
    price_with_tax_00719,
)


def test_price_with_tax_00719():
    assert price_with_tax_00719(1000, 500) == 1050


def test_price_with_tax_negative_00719():
    with pytest.raises(ValueError):
        price_with_tax_00719(1000, -1)


def test_is_valid_sku_00719():
    assert is_valid_sku_00719("abc123")
    assert not is_valid_sku_00719("")


def test_bucket_by_tag_00719():
    p = Product_00719("s1", 100, ["a"])
    assert bucket_by_tag_00719([p]) == {"a": ["s1"]}
