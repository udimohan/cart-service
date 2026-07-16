"""Tests for catalog_01420."""

import pytest

from cartservice.generated.catalog_01420 import (
    Product_01420,
    bucket_by_tag_01420,
    is_valid_sku_01420,
    price_with_tax_01420,
)


def test_price_with_tax_01420():
    assert price_with_tax_01420(1000, 500) == 1050


def test_price_with_tax_negative_01420():
    with pytest.raises(ValueError):
        price_with_tax_01420(1000, -1)


def test_is_valid_sku_01420():
    assert is_valid_sku_01420("abc123")
    assert not is_valid_sku_01420("")


def test_bucket_by_tag_01420():
    p = Product_01420("s1", 100, ["a"])
    assert bucket_by_tag_01420([p]) == {"a": ["s1"]}
