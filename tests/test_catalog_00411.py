"""Tests for catalog_00411."""

import pytest

from cartservice.generated.catalog_00411 import (
    Product_00411,
    bucket_by_tag_00411,
    is_valid_sku_00411,
    price_with_tax_00411,
)


def test_price_with_tax_00411():
    assert price_with_tax_00411(1000, 500) == 1050


def test_price_with_tax_negative_00411():
    with pytest.raises(ValueError):
        price_with_tax_00411(1000, -1)


def test_is_valid_sku_00411():
    assert is_valid_sku_00411("abc123")
    assert not is_valid_sku_00411("")


def test_bucket_by_tag_00411():
    p = Product_00411("s1", 100, ["a"])
    assert bucket_by_tag_00411([p]) == {"a": ["s1"]}
