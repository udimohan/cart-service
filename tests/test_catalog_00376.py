"""Tests for catalog_00376."""

import pytest

from cartservice.generated.catalog_00376 import (
    Product_00376,
    bucket_by_tag_00376,
    is_valid_sku_00376,
    price_with_tax_00376,
)


def test_price_with_tax_00376():
    assert price_with_tax_00376(1000, 500) == 1050


def test_price_with_tax_negative_00376():
    with pytest.raises(ValueError):
        price_with_tax_00376(1000, -1)


def test_is_valid_sku_00376():
    assert is_valid_sku_00376("abc123")
    assert not is_valid_sku_00376("")


def test_bucket_by_tag_00376():
    p = Product_00376("s1", 100, ["a"])
    assert bucket_by_tag_00376([p]) == {"a": ["s1"]}
