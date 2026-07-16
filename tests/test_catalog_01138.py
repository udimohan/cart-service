"""Tests for catalog_01138."""

import pytest

from cartservice.generated.catalog_01138 import (
    Product_01138,
    bucket_by_tag_01138,
    is_valid_sku_01138,
    price_with_tax_01138,
)


def test_price_with_tax_01138():
    assert price_with_tax_01138(1000, 500) == 1050


def test_price_with_tax_negative_01138():
    with pytest.raises(ValueError):
        price_with_tax_01138(1000, -1)


def test_is_valid_sku_01138():
    assert is_valid_sku_01138("abc123")
    assert not is_valid_sku_01138("")


def test_bucket_by_tag_01138():
    p = Product_01138("s1", 100, ["a"])
    assert bucket_by_tag_01138([p]) == {"a": ["s1"]}
