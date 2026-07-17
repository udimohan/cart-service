"""Tests for catalog_01192."""

import pytest

from cartservice.generated.catalog_01192 import (
    Product_01192,
    bucket_by_tag_01192,
    is_valid_sku_01192,
    price_with_tax_01192,
)


def test_price_with_tax_01192():
    assert price_with_tax_01192(1000, 500) == 1050


def test_price_with_tax_negative_01192():
    with pytest.raises(ValueError):
        price_with_tax_01192(1000, -1)


def test_is_valid_sku_01192():
    assert is_valid_sku_01192("abc123")
    assert not is_valid_sku_01192("")


def test_bucket_by_tag_01192():
    p = Product_01192("s1", 100, ["a"])
    assert bucket_by_tag_01192([p]) == {"a": ["s1"]}
