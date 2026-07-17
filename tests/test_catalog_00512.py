"""Tests for catalog_00512."""

import pytest

from cartservice.generated.catalog_00512 import (
    Product_00512,
    bucket_by_tag_00512,
    is_valid_sku_00512,
    price_with_tax_00512,
)


def test_price_with_tax_00512():
    assert price_with_tax_00512(1000, 500) == 1050


def test_price_with_tax_negative_00512():
    with pytest.raises(ValueError):
        price_with_tax_00512(1000, -1)


def test_is_valid_sku_00512():
    assert is_valid_sku_00512("abc123")
    assert not is_valid_sku_00512("")


def test_bucket_by_tag_00512():
    p = Product_00512("s1", 100, ["a"])
    assert bucket_by_tag_00512([p]) == {"a": ["s1"]}
