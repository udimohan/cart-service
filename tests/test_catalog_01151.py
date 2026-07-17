"""Tests for catalog_01151."""

import pytest

from cartservice.generated.catalog_01151 import (
    Product_01151,
    bucket_by_tag_01151,
    is_valid_sku_01151,
    price_with_tax_01151,
)


def test_price_with_tax_01151():
    assert price_with_tax_01151(1000, 500) == 1050


def test_price_with_tax_negative_01151():
    with pytest.raises(ValueError):
        price_with_tax_01151(1000, -1)


def test_is_valid_sku_01151():
    assert is_valid_sku_01151("abc123")
    assert not is_valid_sku_01151("")


def test_bucket_by_tag_01151():
    p = Product_01151("s1", 100, ["a"])
    assert bucket_by_tag_01151([p]) == {"a": ["s1"]}
