"""Tests for catalog_01532."""

import pytest

from cartservice.generated.catalog_01532 import (
    Product_01532,
    bucket_by_tag_01532,
    is_valid_sku_01532,
    price_with_tax_01532,
)


def test_price_with_tax_01532():
    assert price_with_tax_01532(1000, 500) == 1050


def test_price_with_tax_negative_01532():
    with pytest.raises(ValueError):
        price_with_tax_01532(1000, -1)


def test_is_valid_sku_01532():
    assert is_valid_sku_01532("abc123")
    assert not is_valid_sku_01532("")


def test_bucket_by_tag_01532():
    p = Product_01532("s1", 100, ["a"])
    assert bucket_by_tag_01532([p]) == {"a": ["s1"]}
