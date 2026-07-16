"""Tests for catalog_00177."""

import pytest

from cartservice.generated.catalog_00177 import (
    Product_00177,
    bucket_by_tag_00177,
    is_valid_sku_00177,
    price_with_tax_00177,
)


def test_price_with_tax_00177():
    assert price_with_tax_00177(1000, 500) == 1050


def test_price_with_tax_negative_00177():
    with pytest.raises(ValueError):
        price_with_tax_00177(1000, -1)


def test_is_valid_sku_00177():
    assert is_valid_sku_00177("abc123")
    assert not is_valid_sku_00177("")


def test_bucket_by_tag_00177():
    p = Product_00177("s1", 100, ["a"])
    assert bucket_by_tag_00177([p]) == {"a": ["s1"]}
