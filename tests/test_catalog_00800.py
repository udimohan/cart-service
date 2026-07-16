"""Tests for catalog_00800."""

import pytest

from cartservice.generated.catalog_00800 import (
    Product_00800,
    bucket_by_tag_00800,
    is_valid_sku_00800,
    price_with_tax_00800,
)


def test_price_with_tax_00800():
    assert price_with_tax_00800(1000, 500) == 1050


def test_price_with_tax_negative_00800():
    with pytest.raises(ValueError):
        price_with_tax_00800(1000, -1)


def test_is_valid_sku_00800():
    assert is_valid_sku_00800("abc123")
    assert not is_valid_sku_00800("")


def test_bucket_by_tag_00800():
    p = Product_00800("s1", 100, ["a"])
    assert bucket_by_tag_00800([p]) == {"a": ["s1"]}
