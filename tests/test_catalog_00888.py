"""Tests for catalog_00888."""

import pytest

from cartservice.generated.catalog_00888 import (
    Product_00888,
    bucket_by_tag_00888,
    is_valid_sku_00888,
    price_with_tax_00888,
)


def test_price_with_tax_00888():
    assert price_with_tax_00888(1000, 500) == 1050


def test_price_with_tax_negative_00888():
    with pytest.raises(ValueError):
        price_with_tax_00888(1000, -1)


def test_is_valid_sku_00888():
    assert is_valid_sku_00888("abc123")
    assert not is_valid_sku_00888("")


def test_bucket_by_tag_00888():
    p = Product_00888("s1", 100, ["a"])
    assert bucket_by_tag_00888([p]) == {"a": ["s1"]}
