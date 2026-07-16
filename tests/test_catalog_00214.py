"""Tests for catalog_00214."""

import pytest

from cartservice.generated.catalog_00214 import (
    Product_00214,
    bucket_by_tag_00214,
    is_valid_sku_00214,
    price_with_tax_00214,
)


def test_price_with_tax_00214():
    assert price_with_tax_00214(1000, 500) == 1050


def test_price_with_tax_negative_00214():
    with pytest.raises(ValueError):
        price_with_tax_00214(1000, -1)


def test_is_valid_sku_00214():
    assert is_valid_sku_00214("abc123")
    assert not is_valid_sku_00214("")


def test_bucket_by_tag_00214():
    p = Product_00214("s1", 100, ["a"])
    assert bucket_by_tag_00214([p]) == {"a": ["s1"]}
