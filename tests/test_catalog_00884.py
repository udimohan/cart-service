"""Tests for catalog_00884."""

import pytest

from cartservice.generated.catalog_00884 import (
    Product_00884,
    bucket_by_tag_00884,
    is_valid_sku_00884,
    price_with_tax_00884,
)


def test_price_with_tax_00884():
    assert price_with_tax_00884(1000, 500) == 1050


def test_price_with_tax_negative_00884():
    with pytest.raises(ValueError):
        price_with_tax_00884(1000, -1)


def test_is_valid_sku_00884():
    assert is_valid_sku_00884("abc123")
    assert not is_valid_sku_00884("")


def test_bucket_by_tag_00884():
    p = Product_00884("s1", 100, ["a"])
    assert bucket_by_tag_00884([p]) == {"a": ["s1"]}
