"""Tests for catalog_00193."""

import pytest

from cartservice.generated.catalog_00193 import (
    Product_00193,
    bucket_by_tag_00193,
    is_valid_sku_00193,
    price_with_tax_00193,
)


def test_price_with_tax_00193():
    assert price_with_tax_00193(1000, 500) == 1050


def test_price_with_tax_negative_00193():
    with pytest.raises(ValueError):
        price_with_tax_00193(1000, -1)


def test_is_valid_sku_00193():
    assert is_valid_sku_00193("abc123")
    assert not is_valid_sku_00193("")


def test_bucket_by_tag_00193():
    p = Product_00193("s1", 100, ["a"])
    assert bucket_by_tag_00193([p]) == {"a": ["s1"]}
