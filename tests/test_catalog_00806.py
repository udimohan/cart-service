"""Tests for catalog_00806."""

import pytest

from cartservice.generated.catalog_00806 import (
    Product_00806,
    bucket_by_tag_00806,
    is_valid_sku_00806,
    price_with_tax_00806,
)


def test_price_with_tax_00806():
    assert price_with_tax_00806(1000, 500) == 1050


def test_price_with_tax_negative_00806():
    with pytest.raises(ValueError):
        price_with_tax_00806(1000, -1)


def test_is_valid_sku_00806():
    assert is_valid_sku_00806("abc123")
    assert not is_valid_sku_00806("")


def test_bucket_by_tag_00806():
    p = Product_00806("s1", 100, ["a"])
    assert bucket_by_tag_00806([p]) == {"a": ["s1"]}
