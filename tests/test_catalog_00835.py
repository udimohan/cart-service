"""Tests for catalog_00835."""

import pytest

from cartservice.generated.catalog_00835 import (
    Product_00835,
    bucket_by_tag_00835,
    is_valid_sku_00835,
    price_with_tax_00835,
)


def test_price_with_tax_00835():
    assert price_with_tax_00835(1000, 500) == 1050


def test_price_with_tax_negative_00835():
    with pytest.raises(ValueError):
        price_with_tax_00835(1000, -1)


def test_is_valid_sku_00835():
    assert is_valid_sku_00835("abc123")
    assert not is_valid_sku_00835("")


def test_bucket_by_tag_00835():
    p = Product_00835("s1", 100, ["a"])
    assert bucket_by_tag_00835([p]) == {"a": ["s1"]}
