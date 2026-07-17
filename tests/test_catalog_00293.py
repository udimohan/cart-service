"""Tests for catalog_00293."""

import pytest

from cartservice.generated.catalog_00293 import (
    Product_00293,
    bucket_by_tag_00293,
    is_valid_sku_00293,
    price_with_tax_00293,
)


def test_price_with_tax_00293():
    assert price_with_tax_00293(1000, 500) == 1050


def test_price_with_tax_negative_00293():
    with pytest.raises(ValueError):
        price_with_tax_00293(1000, -1)


def test_is_valid_sku_00293():
    assert is_valid_sku_00293("abc123")
    assert not is_valid_sku_00293("")


def test_bucket_by_tag_00293():
    p = Product_00293("s1", 100, ["a"])
    assert bucket_by_tag_00293([p]) == {"a": ["s1"]}
