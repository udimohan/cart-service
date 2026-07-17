"""Tests for catalog_01136."""

import pytest

from cartservice.generated.catalog_01136 import (
    Product_01136,
    bucket_by_tag_01136,
    is_valid_sku_01136,
    price_with_tax_01136,
)


def test_price_with_tax_01136():
    assert price_with_tax_01136(1000, 500) == 1050


def test_price_with_tax_negative_01136():
    with pytest.raises(ValueError):
        price_with_tax_01136(1000, -1)


def test_is_valid_sku_01136():
    assert is_valid_sku_01136("abc123")
    assert not is_valid_sku_01136("")


def test_bucket_by_tag_01136():
    p = Product_01136("s1", 100, ["a"])
    assert bucket_by_tag_01136([p]) == {"a": ["s1"]}
