"""Tests for catalog_00886."""

import pytest

from cartservice.generated.catalog_00886 import (
    Product_00886,
    bucket_by_tag_00886,
    is_valid_sku_00886,
    price_with_tax_00886,
)


def test_price_with_tax_00886():
    assert price_with_tax_00886(1000, 500) == 1050


def test_price_with_tax_negative_00886():
    with pytest.raises(ValueError):
        price_with_tax_00886(1000, -1)


def test_is_valid_sku_00886():
    assert is_valid_sku_00886("abc123")
    assert not is_valid_sku_00886("")


def test_bucket_by_tag_00886():
    p = Product_00886("s1", 100, ["a"])
    assert bucket_by_tag_00886([p]) == {"a": ["s1"]}
