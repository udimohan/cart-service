"""Tests for catalog_00532."""

import pytest

from cartservice.generated.catalog_00532 import (
    Product_00532,
    bucket_by_tag_00532,
    is_valid_sku_00532,
    price_with_tax_00532,
)


def test_price_with_tax_00532():
    assert price_with_tax_00532(1000, 500) == 1050


def test_price_with_tax_negative_00532():
    with pytest.raises(ValueError):
        price_with_tax_00532(1000, -1)


def test_is_valid_sku_00532():
    assert is_valid_sku_00532("abc123")
    assert not is_valid_sku_00532("")


def test_bucket_by_tag_00532():
    p = Product_00532("s1", 100, ["a"])
    assert bucket_by_tag_00532([p]) == {"a": ["s1"]}
