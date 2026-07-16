"""Tests for catalog_01541."""

import pytest

from cartservice.generated.catalog_01541 import (
    Product_01541,
    bucket_by_tag_01541,
    is_valid_sku_01541,
    price_with_tax_01541,
)


def test_price_with_tax_01541():
    assert price_with_tax_01541(1000, 500) == 1050


def test_price_with_tax_negative_01541():
    with pytest.raises(ValueError):
        price_with_tax_01541(1000, -1)


def test_is_valid_sku_01541():
    assert is_valid_sku_01541("abc123")
    assert not is_valid_sku_01541("")


def test_bucket_by_tag_01541():
    p = Product_01541("s1", 100, ["a"])
    assert bucket_by_tag_01541([p]) == {"a": ["s1"]}
