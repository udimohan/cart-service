"""Tests for catalog_00758."""

import pytest

from cartservice.generated.catalog_00758 import (
    Product_00758,
    bucket_by_tag_00758,
    is_valid_sku_00758,
    price_with_tax_00758,
)


def test_price_with_tax_00758():
    assert price_with_tax_00758(1000, 500) == 1050


def test_price_with_tax_negative_00758():
    with pytest.raises(ValueError):
        price_with_tax_00758(1000, -1)


def test_is_valid_sku_00758():
    assert is_valid_sku_00758("abc123")
    assert not is_valid_sku_00758("")


def test_bucket_by_tag_00758():
    p = Product_00758("s1", 100, ["a"])
    assert bucket_by_tag_00758([p]) == {"a": ["s1"]}
