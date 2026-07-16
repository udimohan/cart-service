"""Tests for catalog_00433."""

import pytest

from cartservice.generated.catalog_00433 import (
    Product_00433,
    bucket_by_tag_00433,
    is_valid_sku_00433,
    price_with_tax_00433,
)


def test_price_with_tax_00433():
    assert price_with_tax_00433(1000, 500) == 1050


def test_price_with_tax_negative_00433():
    with pytest.raises(ValueError):
        price_with_tax_00433(1000, -1)


def test_is_valid_sku_00433():
    assert is_valid_sku_00433("abc123")
    assert not is_valid_sku_00433("")


def test_bucket_by_tag_00433():
    p = Product_00433("s1", 100, ["a"])
    assert bucket_by_tag_00433([p]) == {"a": ["s1"]}
