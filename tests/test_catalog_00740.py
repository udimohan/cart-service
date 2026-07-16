"""Tests for catalog_00740."""

import pytest

from cartservice.generated.catalog_00740 import (
    Product_00740,
    bucket_by_tag_00740,
    is_valid_sku_00740,
    price_with_tax_00740,
)


def test_price_with_tax_00740():
    assert price_with_tax_00740(1000, 500) == 1050


def test_price_with_tax_negative_00740():
    with pytest.raises(ValueError):
        price_with_tax_00740(1000, -1)


def test_is_valid_sku_00740():
    assert is_valid_sku_00740("abc123")
    assert not is_valid_sku_00740("")


def test_bucket_by_tag_00740():
    p = Product_00740("s1", 100, ["a"])
    assert bucket_by_tag_00740([p]) == {"a": ["s1"]}
