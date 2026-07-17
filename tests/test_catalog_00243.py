"""Tests for catalog_00243."""

import pytest

from cartservice.generated.catalog_00243 import (
    Product_00243,
    bucket_by_tag_00243,
    is_valid_sku_00243,
    price_with_tax_00243,
)


def test_price_with_tax_00243():
    assert price_with_tax_00243(1000, 500) == 1050


def test_price_with_tax_negative_00243():
    with pytest.raises(ValueError):
        price_with_tax_00243(1000, -1)


def test_is_valid_sku_00243():
    assert is_valid_sku_00243("abc123")
    assert not is_valid_sku_00243("")


def test_bucket_by_tag_00243():
    p = Product_00243("s1", 100, ["a"])
    assert bucket_by_tag_00243([p]) == {"a": ["s1"]}
